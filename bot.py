import time
import random
from playwright.sync_api import sync_playwright

TOTAL_REQUESTS = 100 
API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def perform_visit(index):
    with sync_playwright() as p:
        # لانچ مرورگر در حالت مخفی
        browser = p.chromium.launch(headless=True)
        
        # هر درخواست یک سشن اختصاصی با آی‌پی مسکونی جدید
        session_id = f"req_{index}_{random.randint(100000, 999999)}"
        proxy_url = f"http://scrapeops-session={session_id}:{API_KEY}@residential-proxy.scrapeops.io:8181"
        
        # تنظیم کانتکست با User-Agent انسانی و رزولوشن صفحه واقعی
        context = browser.new_context(
            proxy={"server": proxy_url},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            viewport={'width': 1366, 'height': 768},
            locale='en-US'
        )
        
        page = context.new_page()
        
        # حذف ردپای ربات (تکنیک پیشرفته)
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        page.add_init_script("window.navigator.chrome = { runtime: {} };")
        
        try:
            print(f"درخواست {index}: ورود به شبکه تبلیغاتی...")
            # استفاده از 'load' برای اطمینان از بارگذاری کامل اسکریپت‌های تبلیغاتی
            page.goto("https://www.effectivecpmnetwork.com/k5zpka3k?key=53cbfbb56f98ad1b8c6b83d88f0e0f8a", wait_until="load", timeout=60000)
            
            # اسکرولِ انسانی برای فعال شدن نمایش تبلیغات
            for i in range(3):
                page.mouse.wheel(0, 300)
                time.sleep(random.uniform(2, 4))
            
            # توقف برای ثبت Impression
            time.sleep(random.uniform(20, 30))
            
            print(f"درخواست {index}: بازدید با موفقیت ثبت شد.")
        except Exception as e:
            print(f"درخواست {index}: خطا در بازدید -> {e}")
        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    for i in range(1, TOTAL_REQUESTS + 1):
        perform_visit(i)
        # وقفه تصادفی بین هر بازدید برای رفتار غیر الگوریتمیک
        time.sleep(random.randint(10, 25))
