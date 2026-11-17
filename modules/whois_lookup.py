import whois

def whois_lookup(domain):

    try:
        data = whois.whois(domain)

        print("\n========== WHOIS INFORMATION ==========")

        print("Domain Name:", data.domain_name)
        print("Registrar:", data.registrar)
        print("Creation Date:", data.creation_date)
        print("Expiration Date:", data.expiration_date)
        print("Updated Date:", data.updated_date)
        print("Name Servers:", data.name_servers)
        print("Organization:", data.org)

        print("=======================================")

    except Exception as e:
        print("WHOIS Lookup Error:", e)


if __name__ == "__main__":

    website = input("Enter Website Domain: ")

    whois_lookup(website)
