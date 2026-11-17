import requests
from bs4 import BeautifulSoup

def detect_technology(domain):
    try:
        if not domain.startswith(("http://", "https://")):
            domain = "https://" + domain

        response = requests.get(
            domain,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        html = response.text
        headers = response.headers
        soup = BeautifulSoup(html, "html.parser")

        print("\n========== TECHNOLOGY DETECTION ==========")
        print("Website:", domain)
        print("Status Code:", response.status_code)

        detected = []

        # Web Server Detection
        server = headers.get("Server")
        if server:
            detected.append("Web Server: " + server)

        # Programming Language Detection
        powered_by = headers.get("X-Powered-By")
        if powered_by:
            detected.append("Technology: " + powered_by)

        # CMS Detection
        generator = soup.find("meta", attrs={"name": "generator"})
        if generator and generator.get("content"):
            detected.append("CMS/Generator: " + generator["content"])

        if "wp-content" in html or "wp-includes" in html:
            detected.append("CMS: WordPress")

        # Framework Detection
        if "bootstrap" in html.lower():
            detected.append("Framework Indicator: Bootstrap")

        if "jquery" in html.lower():
            detected.append("Library Indicator: jQuery")

        if ".php" in html.lower():
            detected.append("Possible PHP Indicator")

        print("\nDetected Technologies:")

        if detected:
            for item in set(detected):
                print("-", item)
        else:
            print("No clear technology indicators found.")

        print("\nNote: Detection is based on public indicators.")
        print("Results may not identify every technology.")

    except requests.exceptions.RequestException as e:
        print("Technology Detection Error:", e)


if __name__ == "__main__":
    website = input("Enter Website Domain: ")
    detect_technology(website)
