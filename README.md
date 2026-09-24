# 🛡️ Cyber-Lab Defender Toolkit

Built in Lilongwe, Malawi | Level 2 Graduation Project

> From learning how hackers try 1000 passwords, to building the tools that BLOCK them.

## 👨‍💻 About Me

**John Phiri** - Aspiring SOC Analyst & White Hat Hacker
Location: Lilongwe, Malawi 🇲🇼
HackerOne: @cyberlab265

Learning cybersecurity by building defender tools, not attacker tools.

## 🛠️ Tools in this Toolkit

### 1. `password_checker.py`
Checks if password is weak or strong. Prevents weak passwords that brute-force exploits.

### 2. `login_guard.py`
Blocks brute-force attack after 5 failed attempts.
- Blocks IP
- Shows CAPTCHA logic
- Returns 429

This is the fix for the bug I found in the wild!

### 3. `vault.py`
Simple password vault for education.
- LOCK with password -> creates `vault.locked`
- UNLOCK only with correct password
- Tested: Wrong password = ❌ Wrong password!
- Correct password = 🔓 UNLOCKED: my saraly is 5M lilongwe

How to run:
