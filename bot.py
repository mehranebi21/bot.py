import time
from playwright.sync_api import sync_playwright

# API Key خود را اینجا قرار دهید
API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # تنظیمات پروکسی به‌صورت آبجکت جداگانه (استاندارد پلی‌رایت)
        proxy_config = {
            "server": "http://residential-proxy.scrapeops.io:8181",
            "username": "scrapeops",
            "password": API_KEY
        }
        
        context = browser.new_context(
            proxy=proxy_config,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        # حذف ردپای ربات
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        try:
            print("تلاش برای ورود به سایت تبلیغاتی...")
            # استفاده از commit برای جلوگیری از انتظار بیهوده
            page.goto("https://www.effectivecpmnetwork.com/k5zpka3k?key=53cbfbb56f98ad1b8c6b83d88f0e0f8a", wait_until="commit")
            
            # توقف برای ثبت بازدید واقعی
            time.sleep(25)
            print("بازدید ثبت شد.")
            
        except Exception as e:
            print(f"خطای اتصال: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    run()
