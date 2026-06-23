import time
import random
from playwright.sync_api import sync_playwright

API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def visit_link_multi():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        for i in range(3): 
            session_id = f"session_{random.randint(10000, 99999)}"
            proxy_url = f"http://scrapeops-session={session_id}:{API_KEY}@residential-proxy.scrapeops.io:8181"
            
            context = browser.new_context(proxy={"server": proxy_url})
            # هر پاپ‌آپی که باز شد، بلافاصله بسته شود (بدون تداخل با صفحه اصلی)
            context.on("page", lambda page: page.close())
            
            page = context.new_page()
            
            try:
                print(f"شروع بازدید شماره {i+1}...")
                page.goto("https://shrinkme.click/Salami221", wait_until="domcontentloaded")
                
                # صبر برای لود شدن عناصر
                time.sleep(12)
                
                # کلیک‌های متوالی
                for step in range(5):
                    for btn in ["Continue", "Next", "Get Link", "Verify", "Click to Verify", "Unlock"]:
                        try:
                            # استفاده از click با delay برای رفتار انسانی
                            page.click(f"text={btn}", timeout=5000)
                            print(f"کلیک در مرحله {step+1} روی دکمه '{btn}'")
                            time.sleep(8)
                            break
                        except:
                            continue
                            
                print(f"بازدید شماره {i+1} به پایان رسید.")
            except Exception as e:
                print(f"خطا در بازدید: {e}")
            finally:
                context.close()
                time.sleep(10)
                
        browser.close()

if __name__ == "__main__":
    visit_link_multi()
