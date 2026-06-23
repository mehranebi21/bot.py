import time
import random
from playwright.sync_api import sync_playwright

API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def visit_link():
    with sync_playwright() as p:
        # لانچ با تنظیمات اختصاصی برای مخفی کردن محیطِ خودکار
        browser = p.chromium.launch(headless=True)
        session_id = f"session_{random.randint(100000, 999999)}"
        proxy_url = f"http://scrapeops-session={session_id}:{API_KEY}@residential-proxy.scrapeops.io:8181"
        
        # تنظیم کانتکست با ویژگی‌های یک کاربر واقعی (ویندوز ۱۰ + کروم)
        context = browser.new_context(
            proxy={"server": proxy_url},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={'width': 1366, 'height': 768},
            locale='en-US'
        )
        
        page = context.new_page()
        
        # مخفی کردن ردپایِ ربات در جاوا اسکریپت
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        try:
            print("در حال بازدید از شبکه تبلیغاتی...")
            # ورود به صفحه
            page.goto("https://www.effectivecpmnetwork.com/k5zpka3k?key=53cbfbb56f98ad1b8c6b83d88f0e0f8a")
            
            # صبر کردن برای لود کامل (تبلیغات شبکه نیاز به زمان دارند)
            time.sleep(random.randint(15, 25))
            
            # اسکرول ملایم برای اینکه سرور فکر کند کاربر در حال مطالعه صفحه است
            page.mouse.wheel(0, 300)
            time.sleep(5)
            
            print("بازدید با رفتار انسانی شبیه‌سازی شد.")
            
        except Exception as e:
            print(f"خطا: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    visit_link()
