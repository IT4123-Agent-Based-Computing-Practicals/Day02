# Day 02: Socket Programming - Book Shop System 📚

## Overview 🎯

A simple client-server application using Python sockets to simulate an online bookshop where customers can view and purchase books.

## Files 📁

- `shopowner.py` - Server program (Shop Owner)
- `customer.py` - Client program (Customer)

## How It Works 🔄

### Server Side (`shopowner.py`) 🏪

- Creates a socket and binds to host and port 8080
- Maintains a book inventory with name, price, and stock quantity
- Listens for client connections
- Handles three types of requests:
  - **View Available Books**: Sends formatted list of all books
  - **Buy**: Processes purchase requests, checks stock, calculates total price
  - **Exit**: Closes connection gracefully

### Client Side (`customer.py`) 🛒

- Connects to the server using hostname and port
- Provides interactive menu:
  1. View Available Books
  2. Buy a Book (enter book name and quantity)
  3. Exit
- Sends requests to server and displays responses

## How to Run 🚀

**Terminal 1 - Start Server:**

```powershell
python shopowner.py
```

**Terminal 2 - Start Client:**

```powershell
python customer.py
```

Enter the hostname shown by the server (or use `localhost`)

## Key Concepts 💡

- **Socket Programming**: Network communication between client and server
- **TCP Connection**: Reliable connection-oriented protocol
- **Request-Response Pattern**: Client sends requests, server processes and responds
- **Encoding/Decoding**: Convert strings to bytes for network transmission

## Sample Books 📖

- Harry Potter 1 - $2000.00 (5 in stock)
- Harry Potter 2 - $4000.00 (10 in stock)
- Abc - $400.00 (2 in stock)

## Quick Code Reference 📝

### Server Template (4 Steps) 🏪

```python
# 1. Create & Bind
s = socket.socket()
s.bind((host, port))
s.listen(1)

# 2. Accept Connection
conn, addr = s.accept()

# 3. Receive & Send
msg = conn.recv(1024).decode()
conn.send(response.encode())

# 4. Close
conn.close()
```

### Client Template (3 Steps) 🛒

```python
# 1. Connect
s = socket.socket()
s.connect((host, port))

# 2. Send & Receive
s.send(message.encode())
response = s.recv(1024).decode()

# 3. Close
s.close()
```

### Remember 🧠

- **Server**: Create → Bind → Listen → Accept → Recv/Send
- **Client**: Create → Connect → Send/Recv
- Always **encode()** before sending, **decode()** after receiving

## Complete Code Snippets 💻

### Full Server Code (Minimal Version) 🏪

```python
import socket

# Setup
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)

# Accept connection
conn, addr = s.accept()
print(f"{addr} connected")

# Communication loop
while True:
    msg = conn.recv(1024).decode()

    if msg == "Exit":
        conn.send("Goodbye!".encode())
        break

    # Process and respond
    response = f"Received: {msg}"
    conn.send(response.encode())

conn.close()
```

### Full Client Code (Minimal Version) 🛒

```python
import socket

# Connect to server
s = socket.socket()
host = input("Enter server hostname: ")
port = 8080
s.connect((host, port))

# Communication loop
while True:
    msg = input("Enter message (or 'Exit'): ")
    s.send(msg.encode())

    response = s.recv(1024).decode()
    print("Server:", response)

    if msg == "Exit":
        break

s.close()
```

### Important Code Patterns 🔑

**Handling Multiple Messages:**

```python
# Server receives multiple inputs
msg1 = conn.recv(1024).decode()
msg2 = conn.recv(1024).decode()
msg3 = conn.recv(1024).decode()
```

**Working with Lists/Data:**

```python
# Send formatted data
for item in book_list:
    response += f"{item[0]} - ${item[1]}\n"
conn.send(response.encode())
```

**Error Handling:**

```python
try:
    s.connect((host, port))
except:
    print("Connection failed!")
```

### Common Functions 📚

```python
socket.socket()         # Create socket
s.bind((host, port))   # Bind to address (server only)
s.listen(1)            # Start listening (server only)
conn, addr = s.accept() # Accept connection (server only)
s.connect((host, port)) # Connect to server (client only)
s.send(data.encode())  # Send data (bytes)
s.recv(1024).decode()  # Receive data (convert to string)
s.close()              # Close connection
```

- **Client**: Create → Connect → Send/Recv
- Always **encode()** before sending, **decode()** after receiving
