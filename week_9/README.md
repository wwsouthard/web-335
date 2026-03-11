# WhatABook Python Console Application

## Overview

The **WhatABook application** is a Python console program that connects to a **MongoDB Atlas database**. The application allows users to browse available books, filter books by genre, and manage a customer wishlist.

This program demonstrates the following concepts:

- Connecting a Python application to **MongoDB Atlas**
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

## Step 3: Configure the Application

Open the file **`whatABook_app.py`**.

Locate the cluster configuration section and update the cluster address if necessary.

Example:

```
CLUSTER_ADDRESS = "cluster0.xxxxx.mongodb.net"
```

---

## Step 4: Run the Application

While in the project directory and with the virtual environment activated, run the program:

```
python whatABook_app.py
```

or

```
python3 whatABook_app.py
```

---

## Step 5: Login to MongoDB

When the program starts, it will prompt for your MongoDB Atlas credentials.

```
Enter MongoDB username: web335_user
Enter MongoDB password: s3cret
```

After successful login, the application will display database statistics and the main menu.

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

- The program requires an **active internet connection** to connect to MongoDB Atlas.
- Collection names are **case-sensitive**.
- Ensure the **installation script has been executed before running the application**.