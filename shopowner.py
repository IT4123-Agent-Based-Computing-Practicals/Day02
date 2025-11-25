import socket       #PROVIDE ACCESS TO NETWORK
import sys
import time

book_list = list([
    ["Harry Potter 1",2000.00,5],
    ["Harry Potter 2",4000.00,10],
    ["Abc",400.00,2],
])

s = socket.socket()
host = socket.gethostname()
print("Server will start on Host!",host)
port = 8080        #ENDPOINT COMMUNICATION
s.bind((host,port))   #Binds the socket s to the host and port so it can listen for incoming connections on this address.
print("")
print("Server done binding to host and port successfully")
print("")
s.listen(1)   #Start listening for incoming connections
print("Server is waiting for incoming connection")
print("")

conn,addr = s.accept()
print(addr," has connected to the server and is now online.....")
print("")

while 1:
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()

    if incoming_message == "View Available Books":
        response = "Available books:\n"
        for i, book in enumerate(book_list):
            response += f"{i+1}. {book[0]} - ${book[1]} ({book[2]} in stock)\n" # 1. Harry Potter 1 - $2000.0 (5 in stock)
        conn.send(response.encode())

    elif incoming_message == "Buy":
        incoming_book_name = conn.recv(1024)
        incoming_book_name = incoming_book_name.decode()

        incoming_qty = conn.recv(1024)
        incoming_qty = incoming_qty.decode()
        incoming_qty = int(incoming_qty)

        for book in book_list:
            if book[0] == incoming_book_name:
                if book[2] >= incoming_qty:
                    total_price = incoming_qty * book[1]
                    response = f"Success!! Total price is: {total_price}"
                    book[2] = book[2] - incoming_qty
                    conn.send(response.encode())
                    break
                else:
                    conn.send("Not enough books in the stock!".encode())
                    break
        else:
            conn.send("Book not found!".encode())

    elif incoming_message == "Exit":
        print("Client requested exit.")
        conn.send("Goodbye!".encode())
        break