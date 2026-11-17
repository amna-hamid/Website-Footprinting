import dns.resolver

def discover_subdomains(domain):

    subdomains = [
        "www",
        "mail",
        "blog",
        "shop",
        "admin",
        "ftp",
        "dev",
        "test",
        "api",
        "webmail"
    ]

    print("\n========== SUBDOMAIN DISCOVERY ==========")
    print("Target Domain:", domain)

    found = []

    for sub in subdomains:
        full_domain = sub + "." + domain

        try:
            answers = dns.resolver.resolve(full_domain, "A")

            for answer in answers:
                result = full_domain + " -> " + str(answer)
                found.append(result)
                print("[FOUND]", result)

        except Exception:
            print("[NOT FOUND]", full_domain)

    print("\n========== SUMMARY ==========")
    print("Total Subdomains Found:", len(found))

    if not found:
        print("No subdomains discovered.")

if __name__ == "__main__":
    website = input("Enter Website Domain: ").strip()
    website = website.replace("https://", "").replace("http://", "").split("/")[0]

    discover_subdomains(website)
