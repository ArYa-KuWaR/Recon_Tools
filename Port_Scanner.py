import socket
import datetime

def get_Target():
    ip = input("Enter the IP Adress of Target: ")
    try:
        socket.inet_aton(ip)  # checks whether input matches IP format, if not it will throw an exception
    except socket.error:
        print("Invalid IP address")
        exit()
    return ip

def scan_ports(ip):
    
    print("\n" + "-" * 50)
    print(f"Target: {ip}")
    print(f"Started scannin at: {datetime.datetime.now()}")
    print("-" * 50 + "\n")


    # result = s.connect_ex(("127.0.0.1", 80))       This code snippet was created to test for local 
    # print(result)                   if result = 0, then the port is open; if anything else, then the port is closed    
    # s.close()                       we used coonect_ex instead of connect because connect_ex returns an error code instead of raising an exception if the connection fails. 

    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 1. CREATE              this is a socket object; it will be used to connect to the target host and port
        s.settimeout(0.5)                                       # 2. CONFIGURE           if we didnt add this the scanning of 65000 ports would take hours, this timers sits on a port for 0.5 seconds and then moves on to next port.
        result = s.connect_ex((ip, port))                       # 3. CONNECT
        if result == 0:
            print(f"[+] Port {port:5} -> open.")
        s.close()                                               # 4. CLOSE
    
    print("Scanning completed.")

def main():
    target = get_Target()
    scan_ports(target)

main()