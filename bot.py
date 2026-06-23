import time
import random
from playwright.sync_api import sync_playwright

# تعداد بازدید مورد نظر
TOTAL_REQUESTS = 100 
API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def perform_visit(index):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # هر درخواست = یک Session جدید = یک آی‌پی جدید
        session_id = f"req_{index}_{random.randint(1000, 9999)}"
        proxy_url = f"http://scrapeops-session={session_id}:{API_KEY}@residential-proxy.scrapeops.io:8181"
        
        context = browser.new_context(proxy={"server": proxy_url})
        page = context.new_page()
        
        try:
            print(f"درخواست شماره {index}: شروع بازدید...")
            page.goto("https://www.effectivecpmnetwork.com/k5zpka3k?key=53cbfbb56f98ad1b8c6b83d88f0e0f8a", wait_until="commit")
            
            # زمان حضور در صفحه برای ثبت بازدید (۱۰ ثانیه کافیست)
            time.sleep(10)
            
            # اسکرول کوچک برای تایید انسانی
            page.mouse.wheel(0, 300)
            time.sleep(2)
            
            print(f"درخواست شماره {index}: بازدید موفق ثبت شد.")
        except Exception as e:
            print(f"درخواست شماره {index}: خطا -> {e}")
        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    for i in range(1, TOTAL_REQUESTS + 1):
        perform_visit(i)
        # فاصله بین هر درخواست برای جلوگیری از شناسایی توسط Adsterra
        time.sleep(random.randint(5, 12))
