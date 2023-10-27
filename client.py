import socket


def xor_decrypt(encrypted_message, key):
    decrypted_message = [byte ^ key[i % len(key)] for i, byte in enumerate(encrypted_message)]
    return bytes(decrypted_message)



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 12345)
client_socket.connect(server_address)


encrypted_message = client_socket.recv(1024)

xor_key = b'\x11\x22\x33\x44\x55'  # 5-byte XOR key
decrypted_message = xor_decrypt(encrypted_message, xor_key)


print("Decrypted message from server:", decrypted_message.decode())


client_socket.close()
