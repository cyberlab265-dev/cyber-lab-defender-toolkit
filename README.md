# 🛡️ Cyber-Lab Defender Toolkit
Built in Lilongwe, Malawi | Level 2 Graduation Project

> From learning how hackers try 1000 passwords, to building the tools that BLOCK them.

## 👨‍💻 About Me
**John Phiri** - Aspiring SOC Analyst & White Hat Defender
Lilongwe, Malawi | September 2026

I built this toolkit in my cyber-lab to understand and defend against real-world attacks.

## 🧰 Tools Included

### 1. `dashboard.py` - Security Dashboard (Level 1)
My first SOC dashboard. Shows live system health.

### 2. `wifi_watcher.py` - WiFi Intruder Detector (Level 2 - Day 7)
Scans YOUR network only and lists all devices.
- Detects unknown devices stealing WiFi
- Uses ARP table analysis
- 100% white-hat, defensive only

**How to run:** `python3 wifi_watcher.py`

### 3. `login_guard.py` - Brute Force Blocker (Level 2 - Day 8)
This tool PROVES why 1000 password tries fail.
- Locks account after 5 failed attempts
- Same logic used by Facebook, Google, banks
- This is how we stop brute force attacks

**How to run:** `python3 login_guard.py`
> Try 5 wrong passwords -> See `ACCOUNT LOCKED FOR 10 MINUTES!`

### 4. `vault.py` - File Vault Encryption (Level 2 - Day 9) ⭐
Encrypts secret files before sending on WhatsApp.
- LOCK with password -> creates `vault.locked`
- UNLOCK only with correct password
- Tested: Wrong password = ❌ Wrong password!
- Correct password = 🔓 UNLOCKED: my saraly is 5M lilongwe

**How to run:**
```bash
python3 vault.py
# Choose 1 = LOCK, 2 = UNLOCK
