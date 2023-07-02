import socket

def port_scan(target, start_port, end_port):
    print("{} için Port Tarama Sonuçları: \n".format(target))
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print("Port {}: Açık".format(port))
        else:
            print("Port {}: Kapalı".format(port))
        sock.close()

def main():
    target = input("Hedef IP adresini veya alan adını girin: ")
    start_port = int(input("Başlangıç port numarasını girin: "))
    end_port = int(input("Bitiş port numarasını girin: "))
    port_scan(target, start_port, end_port)

if __name__ == "__main__":
    main()
