import random, string, math

def check_pass():
    pwd = input("\nTest a password: ")
    score = 0
    if len(pwd) >= 12: score+=1
    if any(c.isupper() for c in pwd): score+=1
    if any(c.islower() for c in pwd): score+=1
    if any(c.isdigit() for c in pwd): score+=1
    if any(c in "!@#$%^&*()_+-=" for c in pwd): score+=1
    print(f"Score: {score}/5 - {'STRONG 100+ years!' if score==5 else 'MEDIUM - days' if score>=3 else 'WEAK - SECONDS!'}")

def crack_time():
    pwd = input("\nEnter TEST password: ")
    charset = 0
    if any(c.islower() for c in pwd): charset+=26
    if any(c.isupper() for c in pwd): charset+=26
    if any(c.isdigit() for c in pwd): charset+=10
    if any(c in "!@#$%^&*()_+-=" for c in pwd): charset+=32
    if charset==0: return
    seconds = (charset ** len(pwd)) / 1_000_000_000
    years = seconds / 31536000
    print(f"Length: {len(pwd)} - Time to crack: {int(years)} YEARS" if years>1 else f"Time: {int(seconds)} sec")

def gen_pass():
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
    pwd = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase), random.choice(string.digits), random.choice("!@#$%^&*()")]
    for _ in range(16): pwd.append(random.choice(all_chars))
    random.shuffle(pwd)
    final = "".join(pwd)
    print(f"\nGenerated: {final}\nSaved to my_vault.txt")
    open("my_vault.txt","a").write(final+"\n")

def phish():
    url = input("\nPaste link: ").lower()
    score=0
    if "http://" in url: score+=1
    if "facebook-login" in url or "free-data" in url or "faceb00k" in url: score+=5
    if "facebook" in url and "facebook.com" not in url: score+=5
    print(f"\n{'🔴 DANGER '+str(score)+'/10 - DO NOT CLICK!' if score>=3 else '🟢 CLEAN 0/10' if score==0 else '🟡 SUSPICIOUS'}")

while True:
    print("\n=== CYBER-LAB DASHBOARD ===")
    print("1. Check password strength")
    print("2. Calculate crack time")
    print("3. Generate strong password")
    print("4. Phish detector")
    print("5. Exit")
    c = input("Choose 1-5: ")
    if c=="1": check_pass()
    elif c=="2": crack_time()
    elif c=="3": gen_pass()
    elif c=="4": phish()
    elif c=="5": print("Bye White Hat! Stay safe in Lilongwe!"); break
