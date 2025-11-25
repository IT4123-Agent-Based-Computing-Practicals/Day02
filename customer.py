import socket
import sys
import time

s = socket.socket()
host = input(str("Please enter host name of the Server: "))
port = 8080
s.connect((host,port))
print("Connected to the Book Shop Server")
while 1:
    print("Book Shop Menu:")
    print("1. View Available Books")
    print("2. Buy a Book")
    print("3. Exit")
    option = input(str("Enter Your Option: "))

    if option == "1":
        option1_msg = "View Available Books".encode()
        s.send(option1_msg)
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print("Shop Owner: ",incoming_message)
        print("")
    elif option == "2":
        buy_msg = "Buy"
        buy_msg = buy_msg.encode()
        s.send(buy_msg)

        book_name = input(str("Enter the name of the book: "))
        book_name = book_name.encode()
        s.send(book_name)

        book_count = input(str("Enter the quantity needed: "))
        book_count = book_count.encode()
        s.send(book_count)

        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print("Shop Owner: ",incoming_message)
        print("")
    elif option == "3":
        exit_msg = "Exit".encode()
        s.send(exit_msg)
        print("Exiting...")
        break