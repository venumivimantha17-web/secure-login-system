import getpass

stored_username = "admin"
stored_password = "Cyber@123"

print("🔐 Welcome to Secure Login System")

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if username == stored_username and password == stored_password:
        print("✅ Login successful! Access granted.")
        break
    else:
        attempts -= 1
        print(f"❌ Wrong credentials. Attempts left: {attempts}")

if attempts == 0:
    print("🚫 Account locked!")