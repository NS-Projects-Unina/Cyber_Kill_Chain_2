import ssl
import socket

HOST = "127.0.0.1"
PORT = 8443

context = ssl._create_unverified_context()

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname="localhost") as tls_client:
        print("[*] Connessione TLS stabilita")
        tls_client.sendall(b"Ciao server, questo messaggio e cifrato")
        response = tls_client.recv(1024)
        print("[+] Risposta dal server:", response.decode(errors="ignore"))
