import time
import random
from playwright.sync_api import sync_playwright

API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def visit_link_multi():
    with sync_playwright() as p:
        # لانچ کردن مرورگر فقط یک بار
        browser = p.chromium.launch(headless=True)
        
        for i in range(3): 
            try:
                # ایجاد یک نشست کاملاً جدید برای هر بازدید
                session_id = f"session_{random.randint(100000, 999999)}"
                proxy_url = f"http://scrapeops-session={session_id}:{API_KEY}@residential-proxy.scrapeops.io:8181"
                
                context = browser.new_context(proxy={"server": proxy_url})
                page = context.new_page()
                
                # جلوگیری از بسته شدن پاپ‌آپ‌ها به صورت تهاجمی
                context.on("page", lambda p: p.close())
                
                print(f"شروع بازدید شماره {i+1} با نشست {session_id}...")
                
                # استفاده از wait_until="commit" به جای domcontentloaded برای جلوگیری از مسدود شدن سریع
                page.goto("https://shrinkme.click/Salami221", wait_until="commit")
                
                # صبر برای لود شدن لایه‌های امنیتی
                time.sleep(15)
                
                # چک کردن اینکه آیا صفحه اصلاً باز شده یا نه
                if page.title():
                    print("صفحه با موفقیت لود شد.")
                    # در اینجا می‌توانید کلیک‌ها را اضافه کنید
                
            except Exception as e:
                print(f"خطا در بازدید {i+1}: {e}")
            finally:
                context.close()
                time.sleep(random.randint(10, 20))
                
        browser.close()

if __name__ == "__main__":
    visit_link_multi()
