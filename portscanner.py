import socket

ip = input("Ingrese la direccion IP a escanear: ")
#ip de pruebas en nmap = 45.33.32.156

for puerto in range (1, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result = sock.connect_ex((ip, puerto))

    if result == 0:
        print("\nPuerto Abierto: " + str(puerto) + "\n")
        sock.close()
    else:
        print("Puerto Cerrado: " + str(puerto))