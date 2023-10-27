import socket


def xor_encrypt(message, key):
    encrypted_message = bytearray()
    for i in range(len(message)):
        encrypted_message.append(message[i] ^ key[i % len(key)])
    return bytes(encrypted_message)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 12345)
server_socket.bind(server_address)


server_socket.listen(1)
print("Server is listening for incoming connections...")

client_socket, client_address = server_socket.accept()
print("Connection established with:", client_address)

message = "Hello, Client! This is a secret message."

xor_key = b'\x11\x22\x33\x44\x55'  # 5-byte XOR key
encrypted_message = xor_encrypt(message.encode(), xor_key)

client_socket.sendall(encrypted_message)
print("Encrypted message sent to the client.")

# Close the sockets
client_socket.close()
server_socket.close()
