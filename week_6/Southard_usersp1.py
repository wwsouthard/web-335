"""
Author: Will Southard
File Name: Southard_usersp1.py
Description: Connects to MongoDB Atlas (web335DB) and displays user documents
per Hands-On 4.2: Python with MongoDB, Part I.
"""

from pymongo import MongoClient

# Build a connection string to connect to MongoDB Atlas.
# IMPORTANT: Replace the connection string below with YOUR Atlas connection string.
# Tip: In Atlas, click Connect > Drivers (Python) to copy the correct URI.
client = MongoClient(
    "mongodb+srv://<username>:<password>@<cluster-host>/web335DB?retryWrites=true&w=majority"
)

# Configure a variable to access the web335DB database
db = client["web335DB"]

print("\n--- Displaying ALL documents in the users collection ---")
# 4. Display all documents in the user’s collection. :contentReference[oaicite:2]{index=2}
for user in db.users.find({}):
    print(user)

print("\n--- Displaying user where employeeId is 1011 ---")
# 5. Display a document where the employeeId is 1011. :contentReference[oaicite:3]{index=3}
print(db.users.find_one({"employeeId": "1011"}))

print("\n--- Displaying user where lastName is Mozart ---")
# 6. Display a document where the lastName is Mozart. :contentReference[oaicite:4]{index=4}
print(db.users.find_one({"lastName": "Mozart"}))

# Close the client connection
client.close()