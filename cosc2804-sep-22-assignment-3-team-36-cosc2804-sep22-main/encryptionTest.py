from cryptography.fernet import Fernet

message = "hello i am secret message!"

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("original message: ", message)
print("encoded message: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted message: ", decMessage)
