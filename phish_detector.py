print("=== Phish Detector - White Hat Edition ===")
url = input("Paste suspicious link: ").lower()

score = 0
warnings = []

if url.startswith("http://"):
    warnings.append("⚠️  NOT HTTPS! Real FB always https://")
    score += 1

if "@" in url or "-" in url.replace("https://","").replace("http://","")[:20]:
    warnings.append("⚠️  Weird symbols @ or - in domain = fake!")
    score += 1

# Black hat tricks
fake_words = ["faceb00k", "fb-login", "facebook-login", "free-data", "meta-verify", "gift", "secure-login"]
for w in fake_words:
    if w in url:
        warnings.append(f"⚠️  Contains trick word: {w}")
        score += 2

if url.count(".") > 3:
    warnings.append("⚠️  Too many dots = fake subdomain!")
    score += 1

if url.replace(".","").replace("/","").replace(":","").replace("-","").isdigit():
    warnings.append("⚠️  IP address instead of name = 100% fake!")
    score += 3

# Check real domains
if "facebook.com" in url or "fb.com" in url:
    if not url.startswith("https://www.facebook.com") and not url.startswith("https://facebook.com"):
        warnings.append("⚠️  Says facebook but NOT real facebook.com domain!")
        score += 3
else:
    if "facebook" in url:
        warnings.append("⚠️  Mentions facebook but domain is NOT facebook.com = FAKE!")
        score += 3

print("\n--- SCAN RESULT ---")
if warnings:
    for w in warnings:
        print(w)
else:
    print("No obvious tricks found")

if score >= 3:
    print(f"\n🔴 DANGER Score {score}/10 - DO NOT CLICK! Black hat link!")
elif score >= 1:
    print(f"\n🟡 SUSPICIOUS Score {score}/10 - Be careful, verify!")
else:
    print(f"\n🟢 CLEAN Score {score}/10 - Looks okay but still be smart!")
