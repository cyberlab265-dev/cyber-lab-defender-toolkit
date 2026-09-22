# rate_tester.py - By John Phiri - Lilongwe Defender
# Checks if login has rate limiting (White Hat Only!)

import requests
import time

def test_rate_limit(url):
    print(f"🛡️ Testing: {url}")
    print("Trying 10 wrong logins fast...\n")
    
    for i in range(1, 11):
        try:
            data = {"email": "test@test.com", "password": "wrong123"}
            r = requests.post(url, data=data, timeout=5)
            
            print(f"Try {i}: Status {r.status_code} - {len(r.text)} chars")
            
            if "blocked" in r.text.lower() or "too many" in r.text.lower() or r.status_code == 429:
                print(f"\n✅ SECURE! Blocked after {i} tries - Like your login_guard.py!")
                return
            
            time.sleep(0.5)
        except Exception as e:
            print(f"Error: {e}")
    
    print("\n🚨 VULNERABLE! No block after 10 tries - Missing Rate Limiting!")
    print("This is a bug you can report on HackerOne VDP!")

# SAFE LAB ONLY - Change this URL to test
if __name__ == "__main__":
    # Test on OWASP Juice Shop (legal to hack)
    test_url = input("Enter login URL to test (or press Enter for demo): ")
    if not test_url:
        print("Demo: This is how it works - add real VDP URL later")
    else:
        test_rate_limit(test_url)
