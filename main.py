
import os
from datetime import datetime

from modules.ip_lookup import get_ip
from modules.dns_lookup import dns_lookup
from modules.whois_lookup import whois_lookup
from modules.header_analysis import analyze_headers
from modules.technology_detection import detect_technology
from modules.subdomain_discovery import discover_subdomains


def capture_output(function, website):
    import io
    from contextlib import redirect_stdout

    output = io.StringIO()

    with redirect_stdout(output):
        function(website)

    return output.getvalue()


def main():
    print("\n====================================")
    print("       WEBSITE FOOTPRINTING TOOL")
    print("====================================")

    website = input("\nEnter Website Domain: ").strip()
    website = website.replace("https://", "")
    website = website.replace("http://", "")
    website = website.split("/")[0]

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. IP Lookup")
        print("2. DNS Lookup")
        print("3. WHOIS Lookup")
        print("4. HTTP Headers Analysis")
        print("5. Technology Detection")
        print("6. Subdomain Discovery")
        print("7. Run All Modules and Save Report")
        print("8. Exit")

        choice = input("\nEnter Your Choice: ")

        functions = {
            "1": ("IP LOOKUP", lambda: print("IP Address:", get_ip(website))),
            "2": ("DNS LOOKUP", lambda: dns_lookup(website)),
            "3": ("WHOIS LOOKUP", lambda: whois_lookup(website)),
            "4": ("HTTP HEADERS ANALYSIS", lambda: analyze_headers(website)),
            "5": ("TECHNOLOGY DETECTION", lambda: detect_technology(website)),
            "6": ("SUBDOMAIN DISCOVERY", lambda: discover_subdomains(website))
        }

        if choice in functions:
            title, function = functions[choice]
            print(f"\n========== {title} ==========")
            print(capture_output(lambda _: function(), website))

        elif choice == "7":
            print("\nRunning All Modules...")

            modules = [
                ("IP LOOKUP", lambda: print("IP Address:", get_ip(website))),
                ("DNS LOOKUP", lambda: dns_lookup(website)),
                ("WHOIS LOOKUP", lambda: whois_lookup(website)),
                ("HTTP HEADERS ANALYSIS", lambda: analyze_headers(website)),
                ("TECHNOLOGY DETECTION", lambda: detect_technology(website)),
                ("SUBDOMAIN DISCOVERY", lambda: discover_subdomains(website))
            ]

            report = []
            report.append("WEBSITE FOOTPRINTING REPORT")
            report.append("=" * 45)
            report.append("Target Website: " + website)
            report.append("Date and Time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            for title, function in modules:
                print(f"\nRunning {title}...")
                result = capture_output(lambda _: function(), website)
                print(result)
                report.append("\n========== " + title + " ==========")
                report.append(result)

            os.makedirs("reports", exist_ok=True)

            filename = "reports/footprinting_report_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"

            with open(filename, "w", encoding="utf-8") as file:
                file.write("\n".join(report))

            print("\nReport saved successfully!")
            print("Report Location:", filename)

        elif choice == "8":
            print("\nThank you for using Website Footprinting Tool!")
            break

        else:
            print("\nInvalid Choice! Please select 1-8.")


if __name__ == "__main__":
    main()
