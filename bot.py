import time
import random
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def visit_link_multi():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # تعداد بازدیدهایی که می‌خواهیم در یک اجرا انجام دهیم
        for i in range(5): 
            # تولید یک ID تصادفی برای نشست (این باعث می‌شود پروکسی آی‌پی را تغییر دهد)
            session_id = f"session_{random.randint(1000, 9999)}"
            proxy_url = f"http://scrapeops-session={session_id}:{API_KEY}@residential-proxy.scrapeops.io:8181"
            
            context = browser.new_context(proxy={"server": proxy_url})
            context.on("page", lambda new_page: new_page.close())
            page = context.new_page()
            stealth_sync(page)
            
            try:
                print(f"شروع بازدید شماره {i+1} با آی‌پی جدید...")
                page.goto("https://shrinkme.click/Salami221", wait_until="domcontentloaded")
                
                # فرآیند کلیک‌های چندمرحله‌ای
                for _ in range(6):
                    time.sleep(5)
                    # پیدا کردن دکمه‌های احتمالی
                    for btn in ["Continue", "Next", "Get Link", "Verify"]:
                        if page.query_selector(f"text={btn}"):
                            page.click(f"text={btn}")
                            break
                            
                print(f"بازدید شماره {i+1} با موفقیت ثبت شد.")
            except Exception as e:
                print(f"خطا در بازدید {i+1}: {e}")
            finally:
                context.close()
                time.sleep(random.randint(10, 20)) # وقفه بین بازدیدها
                
        browser.close()

if __name__ == "__main__":
    visit_link_multi()
