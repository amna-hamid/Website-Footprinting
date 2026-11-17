import socket

def get_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address

    except socket.gaierror:
        return "IP Address not found"


if __name__ == "__main__":
    website = input("Enter Website Domain: ")

    result = get_ip(website)

    print("\nWebsite:", website)
    print("IP Address:", result)

