import ssl
import socket

HOST = "0.0.0.0"
PORT = 8443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"[*] Server TLS in ascolto su {HOST}:{PORT}")

with context.wrap_socket(server_socket, server_side=True) as tls_server:
    conn, addr = tls_server.accept()
    print(f"[+] Connessione da {addr}")

    data = conn.recv(1024)
    print(f"[+] Ricevuto: {data.decode(errors='ignore')}")

    conn.sendall(b"Messaggio ricevuto in modo sicuro tramite TLS")
    conn.close()
