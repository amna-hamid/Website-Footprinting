import dns.resolver

def dns_lookup(domain):

    records = ["A", "AAAA", "MX", "NS", "TXT"]

    for record in records:
        print(f"\n{record} Records:")

        try:
            answers = dns.resolver.resolve(domain, record)

            for answer in answers:
                print(answer)

        except dns.resolver.NoAnswer:
            print("No records found")

        except dns.resolver.NXDOMAIN:
            print("Domain does not exist")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    website = input("Enter Website Domain: ")
    dns_lookup(website)
