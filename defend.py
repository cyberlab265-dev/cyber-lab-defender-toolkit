import random
import string

print("=== White Hat Defender Generator ===")

# Build super strong charset
letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*()_+-=[]{}|"

all_chars = letters + numbers + symbols

length = 20
# Make sure at least 1 of each type
password = [
    random.choice(string.ascii_uppercase),
    random.choice(string.ascii_lowercase),
    random.choice(numbers),
    random.choice(symbols)
]

# Fill rest
for i in range(length - 4):
    password.append(random.choice(all_chars))

random.shuffle(password)
final = "".join(password)

print(f"\nYour UNCRACKABLE password (20 chars):\n{final}")
print(f"\nLength: {len(final)}")
print("Time to crack: BILLIONS of years - Black hat can't touch it!")

# Save to your private file (only YOU)
with open("my_vault.txt", "a") as f:
    f.write(final + "\n")

print("\nSaved to my_vault.txt (keep this secret!)")
