'''
File: server.py
Description: The backend server that will handle the user query from client.py by calling the necesarry data from the MongoDB
             database. The queries are related to the IoT assignment of the sensors for 2 Smart Fridges and a dishwasher of 
             the user (virtually created in Dataniz).
'''

import socket
import ipaddress
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timedelta
import pytz
from dotenv import load_dotenv
import os
import re

load_dotenv()

PAYLOAD = 2036


MONGO_URI = os.getenv('MONGODB_URI')
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client['IoT_Database']                      
collection = db['IoT_Table_virtual']  

meta_collection = client['IoT_Database']['IoT_Table_metadata']
DEVICE_METADATA = {}

# create DEVICE_METADATA to be used
# format for DEVICE_METADATA shown in readme or by running metadata.py
for device in meta_collection.find():
    device = device['customAttributes']
    board = device['children'][0]['customAttributes']
    sensors = board['children']
    for sensor in sensors:
        sensor = sensor['customAttributes']
        if device['name'] not in DEVICE_METADATA: DEVICE_METADATA[device['name']] = {}
        # the type/role of the sensor is not an attribute in the payload
        # but it is mentioned in the sensor name. (ex fridge1_moist_{name of actual sensor})
        # extracts the sensor's type/role by relying on the name
        # note: logic relys on the name; should add try-catch/check in case invalid name
        sensor_type = re.search(r"(?<=_)(.*)(?=_)", sensor['name']).group()
        DEVICE_METADATA[device['name']][sensor_type] = {
                "device_name": device["name"],
                "board_name": board["name"],
                "sensor_name": sensor["name"],
                "unit": sensor["unit"]
        }

        if sensor_type == 'water':
            DEVICE_METADATA[device['name']][sensor_type]['conversion_factor'] = 0.264172

def get_moisture_readings(start_time=None, end_time=None):
    """Get moisture readings from the virtual collection"""
    query = {
        "payload.board_name": DEVICE_METADATA["SmartFridge1"]["moist"]["board_name"],
        "payload.fridge1_moist_AM2320": {"$exists": True}
    }
    
    if start_time and end_time:
        query["time"] = {"$gte": start_time, "$lte": end_time}
    
    return collection.find(query)

def get_water_consumption():
    """Get water consumption data for dishwasher"""
    query = {
        "payload.board_name": DEVICE_METADATA["dishwasher"]['water']["board_name"],
        "payload.dish_water_YF-S201": {"$exists": True}
    }
    return collection.find(query)

def get_electricity_consumption():
    """Get electricity consumption for all devices"""
    devices = list(map(lambda device: device['current'], DEVICE_METADATA.values())) 
    result = {}
    
    for device in devices:
        query = {
            "payload.board_name": device['board_name'],
            f"payload.{device['sensor_name']}": {"$exists": True}  
        }
        latest_reading = collection.find(query)
        if latest_reading:
            try:
                elec_sum = sum(list(map(lambda doc: float(doc["payload"][device['sensor_name']]), latest_reading)))
                conversion_factor = 1
                result[device['device_name']] = elec_sum * conversion_factor
            except (KeyError, ValueError) as e:
                result[device['device_name']] = 0
    return result

def get_pst_time():
    """Get current time in PST"""
    pst = pytz.timezone('America/Los_Angeles')
    return datetime.now(pst)

def process_query(query):
    """Process incoming queries and return appropriate response"""
    if query == "What is the average moisture inside my kitchen fridge in the past three hours?":
        try:
            end_time = get_pst_time()
            start_time = end_time - timedelta(hours=3)
            
            readings = get_moisture_readings(start_time, end_time)
            moisture_values = []
            
            for doc in readings:
                try:
                    moisture = float(doc["payload"]["fridge1_moist_AM2320"])
                    moisture_values.append(moisture)
                except (KeyError, ValueError, TypeError):
                    continue
            
            if not moisture_values:
                return "No moisture data available for the past three hours"
            
            avg_moisture = sum(moisture_values) / len(moisture_values)
            metadata_info = f"Device: {DEVICE_METADATA['SmartFridge1']['moist']['board_name']}, Unit: {DEVICE_METADATA['SmartFridge1']['moist']['unit']}"
            
            return f"Average moisture: {avg_moisture:.2f}% RH\nMetadata: {metadata_info}"
        except Exception as e:
            return f"Error processing moisture query: {str(e)}"

    elif query == "What is the average water consumption per cycle in my smart dishwasher?":
        try:
            readings = get_water_consumption()
            consumption_values = []
            
            for doc in readings:
                try:
                    raw_consumption = float(doc["payload"]["dish_water_YF-S201"])
                    gallons = raw_consumption * DEVICE_METADATA["dishwasher"]['water']["conversion_factor"]
                    consumption_values.append(gallons)
                except (KeyError, ValueError, TypeError) as e:
                    print(e)
                    continue
            
            if not consumption_values:
                return "No water consumption data available"
            
            avg_consumption = sum(consumption_values) / len(consumption_values)
            return f"Average water consumption: {avg_consumption:.2f} gallons"
        except Exception as e:
            return f"Error processing water consumption query: {str(e)}"

    elif query == "Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?":
        try:
            consumption_data = get_electricity_consumption()
            print('working')
            
            if not consumption_data:
                return "No electricity consumption data available"
            
            max_consumer = max(consumption_data.items(), key=lambda x: x[1])
            consumptions = "\n".join([f"{device}: {value:.2f} kWh" 
                                    for device, value in consumption_data.items()])
            
            return f"Device Electricity Consumption:\n{consumptions}\n\nHighest consumer: {max_consumer[0]} with {max_consumer[1]:.2f} kWh"
        except Exception as e:
            return f"Error processing electricity consumption query: {str(e)}"

    return "Invalid query"

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
            print(f"Port number chosen: {port}")
            break
        raise Exception("The input is not in the port range")
    except ValueError:
        print("Needs to be an int")
    except Exception as e:
        print(f"An error occurred: {e}")
'''
host = '0.0.0.0'
port = 1234
# socket.SOCK_STREAM has the socket use datagram; TCP Connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    print(f"Server Host: {host}, Server Port: {port}")
    while True:
        print("\nWaiting for client message... ")
        data = conn.recv(PAYLOAD)
        print("Received Response from the Client")
        print(f"\nIP Client: {addr}, Data: {data.decode()}, Length Data: {len(data)}")
        if data:
            try:
                print(f"Processing query from client {addr}")
                query = data.decode()
                if query == 'end':
                    conn.sendall(b'Ended')
                    print("\nEnding server")
                    conn.close()
                    s.close()
                    break
                
                response = process_query(query)
                conn.sendall(response.encode())
                
            except Exception as e:
                print(f"Error occurred {e}")
                error_msg = f"Error processing query: {str(e)}"
                conn.sendall(error_msg.encode())
