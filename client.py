'''
File: client.py
Description: The client where the user can query information about their IoT devices (2 Smart Fridge and a dishwasher)
'''

import socket
import ipaddress

PAYLOAD = 2036
# When the client sends a message but the server doesn't response. Client will wait this many seconds before a timeout.
TIMEOUT = 5

# Valid queries list
VALID_QUERIES = [
    "What is the average moisture inside my kitchen fridge in the past three hours?",
    "What is the average water consumption per cycle in my smart dishwasher?",
    "Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?"
]

def display_valid_queries():
    print("\nValid queries (enter number or full query):")
    for i, query in enumerate(VALID_QUERIES, 1):
        print(f"{i}. {query}")

def get_valid_query(message):
    if message.isdigit():
        index = int(message) - 1
        if 0 <= index < len(VALID_QUERIES):
            return VALID_QUERIES[index]
    return message if message in VALID_QUERIES else None

# user input for ip and port
'''
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
            print(f"port number chosen: {port}")
            break
        raise Exception("The input is not in the port range")
    except ValueError:
        print("Needs to be an int")
    except Exception as e:
        print(f"An error occurred: {e}")
'''
host = '192.168.56.1'
port = 1234
# socket.SOCK_STREAM has the socket use datagram; TCP  Connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.settimeout(TIMEOUT)
    while True:
        print("\nMessage to send to the server. Send message end to shutdown server. Ctrl^C to exit client: ")
        display_valid_queries()
        message = input("> ")

        # Check if message is valid
        if message.lower() == 'end':
            print(f'Message being sent: {message}')
            print(f"Client: Sending message '{message}' to Server host: {host}, with port: {port}")
            s.sendall(message.encode())
        else:
            query = get_valid_query(message)
            if query is None:
                print("Sorry, this query cannot be processed. Please try one of the valid queries listed above.")
                continue
            print(f'Message being sent: {query}')
            print(f"Client: Sending message '{query}' to Server host: {host}, with port: {port}")
            try:
                s.sendall(query.encode())
            except Exception as e:
                print(f"Error occurred: {e}")
            
        try:
            data = s.recv(PAYLOAD)
        # for both exceptions, continue. the code ahead that provide a summary requires a
        # success response from the server; these error indicate that a failed response.
        except socket.timeout:
            print(f"No response from server after {TIMEOUT} seconds")
            continue
        except ConnectionResetError as e:
            print(f"\nConnection Error occurred. Ensure the server is up before sending a message")
            continue 

        print("\nRecieved Response from Server:")
        print(f"IP SERVER: {host}, DATA: {data.decode()}, Length Data: {len(data)}")
        
        # gets the confirmation message from the server that it terminated
        if data.decode() == 'Ended':
            print("\nYou have ended the server")
