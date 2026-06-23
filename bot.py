import os
from playwright.sync_api import sync_playwright
import time
import random

# تنظیمات API
API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"
PROXY_URL = f"http://scrapeops:{API_KEY}@residential-proxy.scrapeops.io:8181"

def visit_link():
    with sync_playwright() as p:
        # لانچ مرورگر در حالت بدون گرافیک (Headless)
        browser = p.chromium.launch(headless=True)
        
        # تنظیم کانتکست با پروکسی و User-Agent انسانی
        context = browser.new_context(
            proxy={"server": PROXY_URL},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        
        page = context.new_page()
        
        try:
            print("در حال شروع بازدید...")
            # لینک هدف را اینجا جایگزین کنید
            page.goto("لینک_کوتاه_شده_خود_را_اینجا_بنویسید", wait_until="networkidle")
            
            # شبیه‌سازی خواندن صفحه
            time.sleep(random.uniform(5, 12)) 
            page.mouse.wheel(0, 800)
            time.sleep(random.uniform(3, 6))
            
            print("بازدید با موفقیت انجام شد.")
            
        except Exception as e:
            print(f"خطا در حین بازدید: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    visit_link()
