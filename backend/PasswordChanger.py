import Credentials
from SQL import create_connection, execute_query
import bcrypt
# pip install bcrypt

# HOW TO USE:
# Step 1: put a new password into the new_password string
# Step 2: run the file
# (This is assuming Credentials.py and SQL.py are in the same folder, and bcrypt is installed)

# Put a new password HERE
new_password = "testing"

creds = Credentials.Creds()
conn = create_connection(creds.address, creds.username, creds.password, creds.db)

password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
print("Generated Password Hash:", password_hash)

def change_password(email, password_hash):
    query = "UPDATE OwnerLogin SET PasswordHash = %s WHERE Email = %s"
    try:
        execute_query(conn, query, (password_hash, email))
        print(f"Password successfully updated for {email}")
    except Exception as e:
        print(f"Error updating password: {e}")

# The "Email" is currently just "admin"
change_password("admin", password_hash)

conn.close()