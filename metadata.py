'''
File: metadata.py
Description: Running this shows the DEVICE_METADATA format created in server.py. 
             client.py and server.py do not rely on this
'''

import dns
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from pprint import pprint
import re
import os

load_dotenv()

MONGO_URI = os.getenv('MONGODB_URI')

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client['IoT_Database']
collection = db['IoT_Table_metadata']
meta_collection = MongoClient(MONGO_URI)['IoT_Database']['IoT_Table_metadata']

doc = meta_collection.find_one()

DATA={}

for device in meta_collection.find():
    device = device['customAttributes']
    board = device['children'][0]['customAttributes']
    sensors = board['children']
    for sensor in sensors:
        sensor = sensor['customAttributes']
        if device['name'] not in DATA: DATA[device['name']] = {}
        sensor_type = re.search(r"(?<=_)(.*)(?=_)", sensor['name']).group()
        DATA[device['name']][sensor_type] = {
                "device_name": device["name"],
                "board_name": board["name"],
                "sensor_name": sensor["name"],
                "unit": sensor["unit"]
        }
        if sensor_type == 'water':
            DATA[device['name']][sensor_type]['conversation_factor'] = 0.264172
pprint(DATA)
