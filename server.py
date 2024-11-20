import socket
import ipaddress

PAYLOAD = 2036
# default server response message

# user input for ip and port
while True:
    try:
        host = input("Input ip: ")
        ipaddress.ip_address(host)
        print(f"Ip address chosen: {host}")
        break
    except ValueError:
        print("Invalid IP address")

while True:
    try:
        port = int(input("Input port: "))
        if (port >= 0 and port <= 2**(16)):
            print(f"Port number chosen: {port}")
            break
        raise Exception("The input is not in the port range")
    except ValueError:
        print("Needs to be an int")
    except Exception as e:
        print(f"An error occurred: {e}")


# socket.SOCK_STREAM has the socket use datagram; TCP Connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    print(f"Server Host: {host}, Server Port: {port}")
    while True:
        print("\nWaiting for client message... ")
        data = conn.recv(PAYLOAD)
        print("Recieved Response from the Client")
        print(f"\nIP Client: {addr}, Data: {data.decode()}, Length Data: {len(data)}")
        if data:
            try:
                print(f"Sending data back to client {addr}")
                # gets response from client to end communication
                if data.decode() == 'end':
                    conn.sendall(b'Ended')
                    print("\nEnding server")
                    conn.close()
                    s.close()
                    break
                else:
                    conn.sendall(data.decode().upper().encode())
            except Exception as e:
                print(f"Error occurred {e}")
                s.close()
