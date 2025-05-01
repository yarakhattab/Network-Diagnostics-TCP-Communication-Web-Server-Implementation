from socket import *
import threading
import datetime
port = 5051
server_ip = '192.168.1.107'#ip ot the server laptop
messages = {}
#receiving function 
def receive_messages(socket1):
    while True:
        try:
            data, _ = socket1.recvfrom(2048)
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = data.decode('utf-8')
            line_number = len(messages) + 1
            messages[line_number] = (message, timestamp)
        except Exception as e:
            print(f"An error occurred: {e}")
#thread
def main():
    peer_socket = socket(AF_INET, SOCK_DGRAM)
    peer_socket.bind(('', port))  
    # threading for receiving message function
    recv_thread = threading.Thread(target=receive_messages, args=(peer_socket,))
    recv_thread.daemon = True  # the thread will automatically exit when the main program exits even if it is still running
    recv_thread.start() # start the thread

    first_name = input("First name: ")
    last_name = input("Last name: ")

    try:
        while True:
            choice = input("Enter '1' to send a message, '2' to display a message: ")
            #send a message by peer
            if choice == '1':
                mesg = input("Enter your message: ")
                full_mesge = f"{first_name} {last_name}: {mesg}"
                peer_socket.sendto(full_mesge.encode('utf-8'), (server_ip, port))
                print("Your message was sent.")
                print("__")
            #disblay a message that received to the peer by enter the line number +D
            elif choice == '2':
                line = input("Enter the line number and 'D' to display the message (e.g., '2D'): ")
                if line.endswith('D'):
                    line_number = int(line[:1])
                    if line_number in messages:
                        print(f"Message from line {line_number}: {messages[line_number][0]}")
                        print("__")
                    else:
                        print("No message found of this line number !!!!")
    finally:
        peer_socket.close()
if __name__ == "__main__":
    main()