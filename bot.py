import time
import random
from playwright.sync_api import sync_playwright

API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def visit_link():
    with sync_playwright() as p:
        # استفاده از کرومیوم با تنظیمات مخفی‌سازی کامل
        browser = p.chromium.launch(headless=True)
        session_id = f"session_{random.randint(100000, 999999)}"
        proxy_url = f"http://scrapeops-session={session_id}:{API_KEY}@residential-proxy.scrapeops.io:8181"
        
        context = browser.new_context(
            proxy={"server": proxy_url},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080}
        )
        
        page = context.new_page()
        
        # تزریق اسکریپت برای حذف ردپای ربات قبل از ورود به سایت
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        try:
            print("در حال تلاش برای ورود به شبکه تبلیغاتی...")
            # استفاده از 'commit' به جای 'load' برای جلوگیری از تایم‌اوت
            page.goto("https://www.effectivecpmnetwork.com/k5zpka3k?key=53cbfbb56f98ad1b8c6b83d88f0e0f8a", wait_until="commit", timeout=60000)
            
            # اجازه به صفحه برای لود شدن در پس‌زمینه (بدون اینکه ربات گیر کند)
            time.sleep(random.randint(30, 45)) 
            
            print("بازدید ثبت شد (شبیه‌سازی موفق).")
            
        except Exception as e:
            print(f"خطا در حین بازدید: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    visit_link()
