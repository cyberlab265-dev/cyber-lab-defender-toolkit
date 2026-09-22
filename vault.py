import base64

print("=== File Vault - Encrypt Like a Bank ===")
mode = input("1 = LOCK file, 2 = UNLOCK file: ").strip()

if mode == "1":
    text = input("Secret message to LOCK: ")
    pwd = input("Vault password: ")
    # lock it
    combined = f"{pwd}::{text}"
    locked = base64.b64encode(combined.encode()).decode()
    open("vault.locked","w").write(locked)
    print(f"\n🔒 LOCKED! File saved: vault.locked")
    print(f"Code: {locked[:30]}...")
    print("Now you can send vault.locked on WhatsApp!")

elif mode == "2":
    try:
        data = open("vault.locked").read()
        pwd = input("Enter vault password to UNLOCK: ")
        decoded = base64.b64decode(data).decode()
        stored_pwd, secret = decoded.split("::",1)
        if pwd == stored_pwd:
            print(f"\n🔓 UNLOCKED: {secret}")
        else:
            print("\n❌ Wrong password!")
    except FileNotFoundError:
        print("\n❌ No vault.locked found! You must LOCK first with option 1")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Type 1 or 2 only")
