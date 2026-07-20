import socket
import datetime


def getTarget():
    ip = input("Enter the target IP: ")
    try:
        socket.inet_aton(ip)
    except socket.error:
        print("Invalid IP")
        exit()
    return ip

def grabBanner(ip):
    common_Ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389, 3306, 8080]

    print("\n" + "=" * 50)
    print(f"Target   : {ip}")
    print(f"Started  : {datetime.datetime.now()}")
    print("=" * 50 + "\n")

    for port in common_Ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((ip, port))                        # closed ports throw here

            if port in [80, 8080, 443]:                  # HTTP won't respond without a request
                s.send(b"HEAD / HTTP/1.0\r\n\r\n")

            try:
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f"  [+] Port {port:5} -> {banner}")
                else:
                    print(f"  [~] Port {port:5} -> Open, no banner")
            except:
                print(f"  [~] Port {port:5} -> Open, no banner")

            s.close()

        except:
            print(f"  [-] Port {port:5} -> Closed")

def main():
    target = getTarget()
    grabBanner(target)

main()