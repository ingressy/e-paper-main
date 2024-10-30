from passlib.hash import pbkdf2_sha256

# Funktion zum Erstellen eines Eintrags für die Passwortdatei
def create_password_entry(username, password):
    hashed_password = pbkdf2_sha256.hash(password)
    return f"{username}:{hashed_password}"

# Erstelle eine Passwortdatei
with open("password_file.txt", "w") as f:
    f.write(create_password_entry("user1", "password123") + "\n")
    f.write(create_password_entry("user2", "mypassword") + "\n")

print("Passwortdatei erstellt.")
