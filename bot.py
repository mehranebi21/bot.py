import requests

# جایگذاری دقیق API Key
API_KEY = "feb2c1e8-ec74-4fe2-ad35-fc7fc67a74ea"
proxy_url = f"http://scrapeops-session=test_123:{API_KEY}@residential-proxy.scrapeops.io:8181"

proxies = {
    "http": proxy_url,
    "https": proxy_url
}

try:
    print("در حال تست اتصال...")
    response = requests.get("https://ifconfig.me", proxies=proxies, timeout=20)
    print(f"وضعیت پاسخ: {response.status_code}")
    print(f"آی‌پی شناسایی شده: {response.text}")
except Exception as e:
    print(f"خطای اتصال: {e}")
