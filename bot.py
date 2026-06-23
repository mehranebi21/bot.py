import time
from playwright.sync_api import sync_playwright

# API Key خود را اینجا قرار دهید
API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"

def visit():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # تنظیمات پروکسی به صورت تفکیک شده (این روش خطای تونل را برطرف می‌کند)
        proxy_config = {
            "server": "http://residential-proxy.scrapeops.io:8181",
            "username": "scrapeops",
            "password": API_KEY
        }
        
        context = browser.new_context(proxy=proxy_config)
        page = context.new_page()
        
        try:
            print("در حال اتصال به پروکسی و ورود به سایت...")
            # استفاده از یک آدرس ساده‌تر برای تست اولیه
            page.goto("https://httpbin.io/ip", timeout=60000)
            print("پاسخ آی‌پی:")
            print(page.inner_text("body"))
            
            # حالا به سایت اصلی برو
            page.goto("https://www.effectivecpmnetwork.com/k5zpka3k?key=53cbfbb56f98ad1b8c6b83d88f0e0f8a", wait_until="commit")
            time.sleep(15)
            print("بازدید انجام شد.")
            
        except Exception as e:
            print(f"خطای بحرانی در اتصال: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    visit()
