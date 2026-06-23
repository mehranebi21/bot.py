import time
import random
from playwright.sync_api import sync_playwright

API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def visit():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # تنظیمات پروکسی مسکونی
        proxy_url = "http://residential-proxy.scrapeops.io:8181"
        
        context = browser.new_context(
            proxy={
                "server": proxy_url,
                "username": f"scrapeops-session-{random.randint(1000, 9999)}",
                "password": API_KEY
            },
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        
        page = context.new_page()
        # مخفی کردن ربات
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        try:
            print("در حال تلاش برای ورود به سایت...")
            # استفاده از commit برای جلوگیری از گیر کردن
            page.goto("https://www.effectivecpmnetwork.com/k5zpka3k?key=53cbfbb56f98ad1b8c6b83d88f0e0f8a", wait_until="commit")
            
            # گرفتن عکس برای اطمینان از صحت نمایش
            page.screenshot(path="debug_screenshot.png")
            print("عکس از صفحه گرفته شد.")
            
            time.sleep(20) # صبر برای ثبت بازدید
            print("بازدید انجام شد.")
            
        except Exception as e:
            print(f"خطا رخ داد: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    visit()
