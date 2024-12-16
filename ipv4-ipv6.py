import ipaddress

def ip_tipus_ellenorzes():
    ip = input("Adj meg egy IP-címet: ")
    try:
        ip_obj = ipaddress.ip_address(ip)
        
        if isinstance(ip_obj, ipaddress.IPv4Address):
            print(f"{ip} egy IPv4-cím.")
        elif isinstance(ip_obj, ipaddress.IPv6Address):
            print(f"{ip} egy IPv6-cím.")
    except ValueError:
        print(f"{ip} nem érvényes IP-cím.")

if __name__ == "__main__":
    ip_tipus_ellenorzes()
