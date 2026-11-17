import requests

def analyze_headers(domain):
    try:
        if not domain.startswith("http://") and not domain.startswith("https://"):
            domain = "https://" + domain

        response = requests.get(domain, timeout=10)

        print("\n========== HTTP HEADERS ANALYSIS ==========")
        print("Website:", domain)
        print("Status Code:", response.status_code)

        for header, value in response.headers.items():
            print(f"{header}: {value}")

        print("\n========== SECURITY HEADERS ==========")

        security_headers = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy"
        ]

        for header in security_headers:
            if header in response.headers:
                print(f"{header}: Present")
            else:
                print(f"{header}: Not Found")

    except requests.exceptions.RequestException as e:
        print("HTTP Request Error:", e)


if __name__ == "__main__":
    website = input("Enter Website Domain: ")
    analyze_headers(website)
