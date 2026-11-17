
# Website Footprinting Tool

## 1. Project Overview
Website Footprinting Tool is a Python-based cybersecurity project developed using Kali Linux. It collects publicly available information about a target website to understand its digital footprint.

## 2. Project Objectives
- Identify website IP addresses.
- Collect DNS records.
- Retrieve WHOIS information.
- Analyze HTTP response headers.
- Detect possible website technologies.
- Discover publicly accessible subdomains.
- Generate an automatic text report.

## 3. Features
1. IP Lookup
2. DNS Lookup
3. WHOIS Lookup
4. HTTP Headers Analysis
5. Technology Detection
6. Subdomain Discovery
7. Automatic Report Generation

## 4. Technologies Used
- Kali Linux
- Python 3
- Requests
- DNSPython
- Python-WHOIS
- BeautifulSoup
- Socket

## 5. Project Structure

Website-Footprinting/
- main.py
- modules/
  - ip_lookup.py
  - dns_lookup.py
  - whois_lookup.py
  - header_analysis.py
  - technology_detection.py
  - subdomain_discovery.py
- reports/
- screenshots/
- requirements.txt
- README.md

## 6. Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Enter the project directory:

```bash
cd Website-Footprinting
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 7. How to Run

Execute:

```bash
python main.py
```

Enter the target domain and select an option from the main menu.

Option 7 runs all modules and generates a text report inside the reports folder.

## 8. Testing and Results

The project was tested using example.com.

All six modules were executed through the main menu. The tool successfully displayed collected information and generated a text report.

## 9. Limitations
- Some websites hide WHOIS information.
- Technology detection is based on publicly visible indicators.
- Subdomain discovery checks a limited predefined list.
- Results depend on internet and DNS availability.

## 10. Future Improvements
- Add graphical user interface.
- Add more passive subdomain sources.
- Generate PDF and HTML reports.
- Improve technology detection accuracy.

## 11. Ethical Considerations
This tool is intended for educational purposes and authorized security reconnaissance only. Users should obtain permission before assessing websites they do not own.

## 12. Conclusion
Website Footprinting Tool demonstrates how Python can be used to collect and analyze publicly available website information. It combines multiple reconnaissance techniques into one simple command-line application.
