import time
import random
from playwright.sync_api import sync_playwright

API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def perform_visit(index):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # استفاده از سشن برای هر بازدید
        session_id = f"req_{index}_{random.randint(100000, 999999)}"
        proxy_url = f"http://scrapeops-session={session_id}:{API_KEY}@residential-proxy.scrapeops.io:8181"
        
        context = browser.new_context(
            proxy={"server": proxy_url},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        # مخفی‌سازی ردپای ربات
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        try:
            print(f"درخواست {index}: شروع...")
            # استفاده از commit برای جلوگیری از تایم‌اوت در سایت‌های سنگین
            page.goto("https://www.effectivecpmnetwork.com/k5zpka3k?key=53cbfbb56f98ad1b8c6b83d88f0e0f8a", wait_until="commit")
            
            # صبر برای ثبت بازدید توسط تبلیغ دهنده
            time.sleep(20)
            print(f"درخواست {index}: موفق.")
            
        except Exception as e:
            print(f"خطا در درخواست {index}: {e}")
        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    # اجرای ۵ بازدید در هر مرحله برای کاهش ریسک بلاک شدن
    for i in range(1, 6):
        perform_visit(i)
        time.sleep(10)
