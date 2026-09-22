print("=== Login Guard - Blocks 1000 Tries Attack ===")
correct = "WhiteHat2026!"
tries = 0
max_tries = 5

while tries < max_tries:
    guess = input(f"Attempt {tries+1}/{max_tries} - Enter password: ")
    if guess == correct:
        print("🟢 ACCESS GRANTED - Defender wins!")
        break
    else:
        tries += 1
        print(f"❌ Wrong! {max_tries - tries} tries left")
        
if tries == max_tries:
    print("\n🔴 ACCOUNT LOCKED FOR 10 MINUTES!")
    print("Black hat tried 5 times and got BLOCKED.")
    print("If he tried 1000 times, he would still be blocked after 5.")
    print("This is how Facebook stops brute force!")
