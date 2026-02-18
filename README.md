# 🔍 Log Analyzer Tool 
This is a beginner-friendly cybersecurity project that analyzes log files for suspicious activities such as brute-force login attempts and sensitive file access. This tool is designed to mimic the early stages of a SIEM/log‑analysis workflow.

## Features
- This tool reads and parses log files
- It extracts timestamps and sorts events in chronological order
- It detects failed login attempts per IP Address and counts them 
- It flags suspicious IP Addresses
- It detects sensitive file access 
- I color-codes alerts for easy visibility
- It creates a summary dashboard at the end of each run

## Example Output
Here’s a sample run of the log analyzer. This screenshot shows the analyzer detecting brute‑force login attempts and sensitive file access. It also demonstrates the color‑coded alerts (red for warnings, yellow for informational events) and the **summary dashboard** at the end of the scan.
<img width="1049" height="535" alt="Example_output" src="https://github.com/user-attachments/assets/30204c4e-8e65-496e-ae8c-11a9fca2eba1" />


## Usage
Run the analyzer with: python analyzer.py sample.log

## How It Works
1. **Timestamp Parsing** -
Every log entry includes a timestamp. The tool uses those timestamps to sort the events in chronological order.

2. **Failed Login Detection** -
The script counts failed login attempts per IP and flags any IP that exceeds the threshold we set. (In my tool, the threshold is the number of failed login attempts an IP address is allowed before the analyzer considers it suspicious. I set this threshold to 3 in my script so if an IP fails to log in 3 or more times, it gets flagged as a potential brute‑force attempt0

3. **Sensitive File Access** -
Any event containing "FILE ACCESSED" is highlighted for review. This is important because in cybersecurity, when sensitive files are accessed unexpectedly it can be a sign that someone is trying to gather information about the system or someone is performing actions that they shouldn't . 

4. **Color‑Coded Alerts** - The logs are color coded in 3 different colors; red, yellow and green.
- 🔴 Red → Suspicious activity
- 🟡 Yellow → Informational events
- 🟢 Green → Summary dashboard

5. **Summary Dashboard**
At the end of each run, the tool prints:
- The total log entries
- The total failed login attempts
- The number of unique suspicious IPs
- A list of flagged IP Addresses




