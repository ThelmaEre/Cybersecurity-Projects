from datetime import datetime

# Color codes for terminal output
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

# Step 1: Read the log file
with open("sample.log", "r") as file:
    lines = file.readlines()


# Print the lines to confirm it worked
for line in lines:
    print(line.strip())

# Step 2: Count failed login attempts per IP
failed_attempts = {}
for line in lines:
   if "LOGIN FAILED" in line:
      parts = line.split()
      ip = parts[-1].split("=")[1] #extract the IP address

      failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

print("\nFailed login attempts per IP:")
for ip, count in failed_attempts.items():
   print(f"IP: {ip}, Failed Attempts: {count}")

# Step 3: Flag suspicious IPs
print(f"\n{YELLOW}Suspicious IPs (possible brute-force attempts):{RESET}")
for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"{RED}{ip} has {count} failed login attempts — potential brute-force activity{RESET}")

# Step 4: Detect sensitive file access
print(f"\n{YELLOW}Sensitive file access events:{RESET}")
for line in lines:
    if "FILE ACCESSED" in line:
        print(f"{YELLOW}{line.strip()}{RESET}")

# Step 5: Summary Dashboard
print(f"\n{GREEN}==================== SUMMARY DASHBOARD ===================={RESET}")

total_lines = len(lines)
total_failed = sum(failed_attempts.values())
unique_ips = len(failed_attempts)

print(f"{GREEN}Total log entries: {RESET}{total_lines}")
print(f"{GREEN}Total failed login attempts: {RESET}{total_failed}")
print(f"{GREEN}Unique IPs with failed attempts: {RESET}{unique_ips}")

print(f"{GREEN}-----------------------------------------------------------{RESET}")

print(f"{YELLOW}Suspicious IPs (>= 3 failed attempts):{RESET}")
for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"{RED}- {ip}: {count} failed attempts{RESET}")

print(f"{GREEN}===========================================================\n{RESET}")