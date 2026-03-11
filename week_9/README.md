# WhatABook Python Console Application

## Overview

The **WhatABook application** is a Python console program that connects to a **MongoDB Atlas database**. The application allows users to browse available books, filter books by genre, and manage a customer wishlist.

This program demonstrates the following concepts:

- Connecting a Python application to **MongoDB Atlas**
- **Modular configuration** — cluster address and database name are entered at runtime (nothing hardcoded)
- Querying **MongoDB collections**
- Using **aggregation with `$lookup`**
- Menu-driven console applications
- Basic input validation

The database contains three collections:

- `books`
- `customers`
- `wishlistitems`

---

## Requirements

Before running the application, ensure the following software is installed:

- **Python 3**
- **MongoDB Atlas account**
- **mongosh (MongoDB shell)**
- **pymongo Python package**

---

## Project Structure

```
week_9/
│
├── Group3-WhatABook-installation.js
├── whatABook_app.py
├── README.md
└── venv/
```

---

## Step 1: Create the Database

Open a terminal and start **mongosh** connected to your MongoDB Atlas cluster.

```
mongosh "your-mongodb-connection-string"
```

Once connected, navigate to the project folder and run the installation script:

```
load("Group3-WhatABook-installation.js")
```

The installation script will:

- Create the database named **`whatabook`**
- Create the required collections
- Insert sample data

Collections created:

- `books`
- `customers`
- `wishlistitems`

---

## Step 2: Install Python Dependencies

Navigate to the project directory:

```
cd ~/Documents/buwebdev/web-335/week_9
```

Create a Python virtual environment:

```
python3 -m venv venv
```

Activate the virtual environment:

```
source venv/bin/activate
```

Install the MongoDB driver:

```
pip install pymongo
```

---

## Step 3: Run the Application

While in the project directory and with the virtual environment activated, run the program:

```
python whatABook_app.py
```

or

```
python3 whatABook_app.py
```

---

## Step 4: Connection and Login

When the program starts, it prompts for connection details and MongoDB Atlas credentials. Nothing is hardcoded — you supply cluster, database, and credentials each run.

```
Enter cluster address (e.g. yourcluster.xxxxx.mongodb.net): cluster0.xxxxx.mongodb.net
Enter database name: whatABookDB
Enter MongoDB username: web335_user
Enter MongoDB password: s3cret
```

After a successful connection, the application displays database statistics and the main menu.

---

## Application Menu

The menu provides the following options:

| Option | Function |
|------|------|
| **1** | View all books |
| **2** | View books by genre |
| **3** | View customer wishlist |
| **4** | Add book to wishlist |
| **5** | Remove book from wishlist |
| **6** | Exit application |

---

## Example Program Flow

Start the application:

```
python whatABook_app.py
```

Login using your MongoDB Atlas credentials.

Select an option from the menu.

Example:

```
Select option: 1
```

The application will display the list of books stored in the database.

---

## Notes

- The application is **fully modular**: cluster address and database name are entered at runtime with your username and password. No connection details are hardcoded in the source.
- The program requires an **active internet connection** to connect to MongoDB Atlas.
- Collection names are **case-sensitive**.
- Ensure the **installation script has been executed before running the application** (and use the same database name when prompted).