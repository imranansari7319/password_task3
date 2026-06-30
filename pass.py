# Simple Password Generator

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    index = (i * 7 + length * 3) % len(characters)
    password += characters[index]

print("Generated Password:", password)