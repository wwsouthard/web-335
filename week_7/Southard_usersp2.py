"""
Title: Southard_usersp2.py
Author: Will Southard
Date: 28 February 2025
Description: Hands-On 5.2 - Python with MongoDB, Part II.
             Connects to web335DB and performs CRUD operations on the users collection.
"""

# Import the MongoClient
from pymongo import MongoClient
import datetime

# Build a connection string to connect to MongoDB Atlas (web335DB)
# Replace <password> with your actual database user password.
client = MongoClient(
    "mongodb+srv://web335_user:<password>@bellevueuniversity.agiceyx.mongodb.net/web335DB?retryWrites=true&w=majority"
)

# Configure a variable to access the web335DB database
db = client["web335DB"]

# ---------------------------------------------------------------------------
# Verify connection and database (confirms you're connected to the right DB)
# ---------------------------------------------------------------------------
print("\n--- Connection verification ---")
client.admin.command("ping")  # Raises if connection fails
print(f"Connected to database: {db.name}")
print(f"Collections in {db.name}: {list(db.list_collection_names())}")

# ---------------------------------------------------------------------------
# Step 3: Create a new user document and add it to the users collection
# ---------------------------------------------------------------------------
new_user = {
    "firstName": "Will",
    "lastName": "Southard",
    "employeeId": "1014",
    "email": "wsouthard@me.com",
    "dateCreated": datetime.datetime.utcnow(),
}

# Insert the document into the users collection
new_user_id = db.users.insert_one(new_user).inserted_id
print("\n--- Step 3: Document created ---")
print(f"Inserted document ID: {new_user_id}")

# ---------------------------------------------------------------------------
# Step 4: Prove the document was created
# ---------------------------------------------------------------------------
print("\n--- Step 4: Prove the document was created ---")
print(db.users.find_one({"employeeId": "1014"}))

# ---------------------------------------------------------------------------
# Step 5: Update the email address of the document created in step 3
# ---------------------------------------------------------------------------
db.users.update_one(
    {"employeeId": "1014"},
    {"$set": {"email": "will.southard@me.com"}},
)
print("\n--- Step 5: Email address updated ---")

# ---------------------------------------------------------------------------
# Step 6: Prove the document was updated
# ---------------------------------------------------------------------------
print("\n--- Step 6: Prove the document was updated ---")
print(db.users.find_one({"employeeId": "1014"}))

# ---------------------------------------------------------------------------
# Step 7: Delete the document that was created in step 3
# ---------------------------------------------------------------------------
result = db.users.delete_one({"employeeId": "1014"})
print("\n--- Step 7: Document deleted ---")
print(result)

# ---------------------------------------------------------------------------
# Step 8: Prove the document was deleted
# ---------------------------------------------------------------------------
print("\n--- Step 8: Prove the document was deleted ---")
print(db.users.find_one({"employeeId": "1014"}))

# Close the client connection
client.close()
