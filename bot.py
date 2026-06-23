import time
import random
from playwright.sync_api import sync_playwright

API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def apply_stealth(page):
    # این کد اثر انگشت ربات بودن را کاملاً پاک می‌کند
    page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    page.add_init_script("window.navigator.chrome = { runtime: {} };")
    page.add_init_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});")

def visit_link_multi():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # انجام ۳ بازدید مجزا با آی‌پی‌های متفاوت
        for i in range(3): 
            session_id = f"session_{random.randint(10000, 99999)}"
            proxy_url = f"http://scrapeops-session={session_id}:{API_KEY}@residential-proxy.scrapeops.io:8181"
            
            context = browser.new_context(proxy={"server": proxy_url})
            page = context.new_page()
            apply_stealth(page)
            
            # مجبور کردن پاپ‌آپ‌ها به باز شدن در همان تب اصلی
            page.evaluate("window.open = (url) => { window.location.href = url; }")
            
            try:
                print(f"شروع بازدید شماره {i+1}...")
                page.goto("https://shrinkme.click/Salami221", wait_until="domcontentloaded")
                
                # کلیک‌های متوالی برای عبور از مراحل سایت
                for step in range(7):
                    time.sleep(10) # تاخیر انسانی
                    # جستجو برای دکمه‌های رایج و کلیک روی اولین چیزی که پیدا شد
                    for btn in ["Continue", "Next", "Get Link", "Verify", "Click to Verify", "Unlock"]:
                        try:
                            if page.query_selector(f"text={btn}"):
                                page.click(f"text={btn}")
                                print(f"کلیک در مرحله {step+1} روی دکمه '{btn}'")
                                break
                        except:
                            continue
                            
                print(f"بازدید شماره {i+1} به پایان رسید.")
            except Exception as e:
                print(f"خطا در بازدید: {e}")
            finally:
                context.close()
                time.sleep(15) # وقفه بین هر بازدید
                
        browser.close()

if __name__ == "__main__":
    visit_link_multi()
