import socket

target = input("Enter target IP or website: ")

# Common ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443]

print(f"\nScanning target: {target}\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    
    s.close()

print("\nScanning Completed!")