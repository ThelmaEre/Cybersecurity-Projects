# 🔍 Log Analyzer Tool 
A beginner-friendly cybersecurity project that analyzes log files for suspicious activity such as brute-force login attempts and sensitive file access. This tool is designed to mimic the early stages of a SIEM/log‑analysis workflow

## Features
- Reads and parses log files
- Extracts timestamps and sorts events in chronological order
- Detects failed login attempts per IP Address and counts them 
- Flags suspicious IPs 
- Detects sensitive file access 
- Color-coded alerts for easy visibility
- Summary dashboard at the end of each run

## Example Output
Here’s a sample run of the log analyzer. This screenshot shows the analyzer detecting brute‑force login attempts and sensitive file access. It also demonstrates the color‑coded alerts (red for warnings, yellow for informational events) and the **summary dashboard** at the end of the scan.

[put screenshot here]

## Usage
Run the analyzer with: python analyzer.py sample.log

How It Works
1. Timestamp Parsing
Each log entry begins with a timestamp.
The tool converts these into Python datetime objects and sorts events chronologically.
2. Failed Login Detection
The script counts failed login attempts per IP and flags any IP that exceeds the threshold.
3. Sensitive File Access
Any event containing FILE ACCESSED is highlighted for review.
4. Color‑Coded Alerts
- 🔴 Red → Suspicious activity
- 🟡 Yellow → Informational events
- 🟢 Green → Summary dashboard
5. Summary Dashboard
At the end of each run, the tool prints:
- Total log entries
- Total failed login attempts
- Number of unique suspicious IPs
- List of flagged IPs

