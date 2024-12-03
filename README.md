# IoT System - Assignment 8 

## Group 30 - Authors
- **Justin Chong** 
- **Nam Ton**

## System Requirements
- Python 3.x
- MongoDB
- Required Python packages: pymongo python-dotenv pytz (For the env file)

## Setup Instructions

1. Clone the repository

2. Create .env file in project root with your MongoDB URI: (also add a git ignore with a .env just in case cause you don't want to share it to the public)

   MONGODB_URI=mongodb+srv://username:<password>@cluster0.xxxx.mongodb.net/?retryWrites=true&w=majority

- for privacy reasons, the MONGODB_URI we used is only provided in the report submitted 

3. Configure Database:
- Database name: 'test' (This is example this is where you would put your database name)
- Collection: 'Stuff_virtual' (This is example this is where you would put your collection name)
- Ensure your IoT devices are sending data to the correct collection
    - We used Dataniz (dataniz.com) to generate the virtual sensors and send the data to our database
    - The sensor name should be in the format [device-name]_[sensor-function]_[actual-sensor-name]
      - The server parses the sensor function from the sensor name with regex

## Running the System

1. Start the Server:
- Run python3 server.py
- Enter IP (e.g., 127.0.0.1 for local testing)
- Enter Port (e.g., 12345) (or any port)

2. In a new terminal, start the Client:
- Run python3 client.py
- Enter same IP and Port as server

3. Available Queries:
- What is the average moisture inside my kitchen fridge in the past three hours?
- What is the average water consumption per cycle in my smart dishwasher?
- Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?
- Also gives option to select the query (1,2,3) or input the queries above yourself (Will not take any other options)

4. To exit:
- Type 'Ctrl c' in client


## Example Payload Documents from Database

### Dishwasher Payload
{"_id":{"$oid":"67447a4fd50fad3a8939eb6e"},"cmd":"publish","retain":false,"qos":{"$numberInt":"0"},"dup":false,"length":{"$numberInt":"317"},"payload":{"timestamp":"1732541007","topic":"dishwasher/data/sub","parent_asset_uid":"dishwasher_id","asset_uid":"bvw-611-q14-g94","board_name":"Sipeed MAIX Bit - dishwasher_board","dish_water_YF-S201":"12.3781","dish_current_ACS712":"1.0696","dish_voltage_ina219":"5.6645"},"topic":"dishwasher/data/sub","time":{"$date":{"$numberLong":"1732541007000"}},"__v":{"$numberInt":"0"}}
### SmartFridge1 Payload
{"_id":{"$oid":"67447a5fd50fad3a8939ec1c"},"cmd":"publish","retain":false,"qos":{"$numberInt":"0"},"dup":false,"length":{"$numberInt":"312"},"payload":{"timestamp":"1732541023","topic":"fridge1/data/sub","parent_asset_uid":"fridge-1_id","asset_uid":"689-7px-4e3-ads","board_name":"Arduino Due - bob","fridge1_moist_AM2320":"30.7791","fridge1_current_ACS712ELCTR-20A-T":"2.6614","fridge1_voltage_ina219":"-1.3314"},"topic":"fridge1/data/sub","time":{"$date":{"$numberLong":"1732541023000"}},"__v":{"$numberInt":"0"}}
### SmartFridge2 Payload
{"_id":{"$oid":"67447a69d50fad3a8939ec7a"},"cmd":"publish","retain":false,"qos":{"$numberInt":"0"},"dup":false,"length":{"$numberInt":"359"},"payload":{"timestamp":"1732541033","topic":"fridge2/data/sub","parent_asset_uid":"fridge-2_id","asset_uid":"f80e23bb-66af-43b1-a6e9-7b4af3580568","board_name":"board 1 e9605a66-012d-440f-bab0-884dcc419453","fridge2_moist_AM2320":"99.9920","fridge2_current_ACS712ELCTR-20A-T":"3.6084","fridge2_voltage_ina219":"0.3933"},"topic":"fridge2/data/sub","time":{"$date":{"$numberLong":"1732541033000"}},"__v":{"$numberInt":"0"}}
## Metadata

### Dishwasher Metadata
{"_id":{"$oid":"674479e3def8b71c8fb5f828"},"assetUid":"dishwasher_id","parentAssetUid":null,"eventTypes":[],"latitude":{"$numberInt":"1"},"longitude":{"$numberInt":"-1"},"customAttributes":{"generationDate":"2024-11-25T13:21:31.333154Z","type":"DEVICE","name":"dishwasher","children":[{"assetUid":"bvw-611-q14-g94","parentAssetUid":"dishwasher_id","customAttributes":{"type":"BOARD","name":"Sipeed MAIX Bit - dishwasher_board","children":[{"assetUid":"u19-top-1o9-1jq","parentAssetUid":"bvw-611-q14-g94","customAttributes":{"type":"SENSOR","name":"dish_water_YF-S201","unit":"Liters Per Minute","minValue":{"$numberInt":"1"},"maxValue":{"$numberInt":"30"},"desiredMinValue":{"$numberDouble":"1.01"},"desiredMaxValue":{"$numberDouble":"29.99"}}},{"assetUid":"1y2-u21-7n7-31y","parentAssetUid":"bvw-611-q14-g94","customAttributes":{"type":"SENSOR","name":"dish_current_ACS712","unit":"V","minValue":{"$numberDouble":"-0.1"},"maxValue":{"$numberInt":"8"},"desiredMinValue":{"$numberDouble":"-0.09"},"desiredMaxValue":{"$numberDouble":"7.99"}}},{"assetUid":"o0p-p5o-p70-6c2","parentAssetUid":"bvw-611-q14-g94","customAttributes":{"type":"SENSOR","name":"dish_voltage_ina219","unit":"V","minValue":{"$numberInt":"-26"},"maxValue":{"$numberInt":"26"},"desiredMinValue":{"$numberDouble":"-25.99"},"desiredMaxValue":{"$numberDouble":"25.99"}}}]}}]},"__v":{"$numberInt":"0"}}
### SmartFridge1 Metadata
{"_id":{"$oid":"674479f0def8b71c8fb5f82b"},"assetUid":"fridge-1_id","parentAssetUid":null,"eventTypes":[],"latitude":{"$numberInt":"2"},"longitude":{"$numberInt":"2"},"customAttributes":{"generationDate":"2024-11-25T13:21:44.481196Z","type":"DEVICE","name":"SmartFridge1","children":[{"assetUid":"689-7px-4e3-ads","parentAssetUid":"fridge-1_id","customAttributes":{"type":"BOARD","name":"Arduino Due - bob","children":[{"assetUid":"890-6o0-p8u-pbq","parentAssetUid":"689-7px-4e3-ads","customAttributes":{"type":"SENSOR","name":"fridge1_moist_AM2320","unit":"%","minValue":{"$numberInt":"0"},"maxValue":{"$numberInt":"100"},"desiredMinValue":{"$numberDouble":"0.01"},"desiredMaxValue":{"$numberDouble":"99.99"}}},{"assetUid":"178-8j9-954-1hq","parentAssetUid":"689-7px-4e3-ads","customAttributes":{"type":"SENSOR","name":"fridge1_current_ACS712ELCTR-20A-T","unit":"V","minValue":{"$numberDouble":"-0.1"},"maxValue":{"$numberInt":"8"},"desiredMinValue":{"$numberDouble":"-0.09"},"desiredMaxValue":{"$numberDouble":"7.99"}}},{"assetUid":"54t-xge-xlw-v09","parentAssetUid":"689-7px-4e3-ads","customAttributes":{"type":"SENSOR","name":"fridge1_voltage_ina219","unit":"V","minValue":{"$numberInt":"-26"},"maxValue":{"$numberInt":"26"},"desiredMinValue":{"$numberDouble":"-25.99"},"desiredMaxValue":{"$numberDouble":"25.99"}}}]}}]},"__v":{"$numberInt":"0"}}
### SmartFridge2 Metadata
{"_id":{"$oid":"674479fcdef8b71c8fb5f82e"},"assetUid":"fridge-2_id","parentAssetUid":null,"eventTypes":[],"latitude":{"$numberInt":"3"},"longitude":{"$numberInt":"3"},"customAttributes":{"generationDate":"2024-11-25T13:21:57.162844Z","type":"DEVICE","name":"SmartFridge2","children":[{"assetUid":"f80e23bb-66af-43b1-a6e9-7b4af3580568","parentAssetUid":"fridge-2_id","customAttributes":{"type":"BOARD","name":"board 1 e9605a66-012d-440f-bab0-884dcc419453","children":[{"assetUid":"97d5f063-a88d-42ca-82ea-6baa6001f446","parentAssetUid":"f80e23bb-66af-43b1-a6e9-7b4af3580568","customAttributes":{"type":"SENSOR","name":"fridge2_moist_AM2320","unit":"%","minValue":{"$numberInt":"0"},"maxValue":{"$numberInt":"100"},"desiredMinValue":{"$numberDouble":"0.01"},"desiredMaxValue":{"$numberDouble":"99.99"}}},{"assetUid":"58p-6qp-1t1-3u8","parentAssetUid":"f80e23bb-66af-43b1-a6e9-7b4af3580568","customAttributes":{"type":"SENSOR","name":"fridge2_current_ACS712ELCTR-20A-T","unit":"V","minValue":{"$numberDouble":"-0.1"},"maxValue":{"$numberInt":"8"},"desiredMinValue":{"$numberDouble":"-0.09"},"desiredMaxValue":{"$numberDouble":"7.99"}}},{"assetUid":"7a6-od6-0f7-pdk","parentAssetUid":"f80e23bb-66af-43b1-a6e9-7b4af3580568","customAttributes":{"type":"SENSOR","name":"fridge2_voltage_ina219","unit":"V","minValue":{"$numberInt":"-26"},"maxValue":{"$numberInt":"26"},"desiredMinValue":{"$numberDouble":"-25.99"},"desiredMaxValue":{"$numberDouble":"25.99"}}}]}}]},"__v":{"$numberInt":"0"}}
### DEVICE_METADATA (Modified metadata):
{'SmartFridge1': {'current': {'board_name': 'Arduino Due - bob',
                              'device_name': 'SmartFridge1',
                              'sensor_name': 'fridge1_current_ACS712ELCTR-20A-T',
                              'unit': 'V'},
                  'moist': {'board_name': 'Arduino Due - bob',
                            'device_name': 'SmartFridge1',
                            'sensor_name': 'fridge1_moist_AM2320',
                            'unit': '%'},
                  'voltage': {'board_name': 'Arduino Due - bob',
                              'device_name': 'SmartFridge1',
                              'sensor_name': 'fridge1_voltage_ina219',
                              'unit': 'V'}},
 'SmartFridge2': {'current': {'board_name': 'board 1 '
                                            'e9605a66-012d-440f-bab0-884dcc419453',
                              'device_name': 'SmartFridge2',
                              'sensor_name': 'fridge2_current_ACS712ELCTR-20A-T',
                              'unit': 'V'},
                  'moist': {'board_name': 'board 1 '
                                          'e9605a66-012d-440f-bab0-884dcc419453',
                            'device_name': 'SmartFridge2',
                            'sensor_name': 'fridge2_moist_AM2320',
                            'unit': '%'},
                  'voltage': {'board_name': 'board 1 '
                                            'e9605a66-012d-440f-bab0-884dcc419453',
                              'device_name': 'SmartFridge2',
                              'sensor_name': 'fridge2_voltage_ina219',
                              'unit': 'V'}},
 'dishwasher': {'current': {'board_name': 'Sipeed MAIX Bit - dishwasher_board',
                            'device_name': 'dishwasher',
                            'sensor_name': 'dish_current_ACS712',
                            'unit': 'V'},
                'voltage': {'board_name': 'Sipeed MAIX Bit - dishwasher_board',
                            'device_name': 'dishwasher',
                            'sensor_name': 'dish_voltage_ina219',
                            'unit': 'V'},
                'water': {'board_name': 'Sipeed MAIX Bit - dishwasher_board',
                          'conversation_factor': 0.264172,
                          'device_name': 'dishwasher',
                          'sensor_name': 'dish_water_YF-S201',
                          'unit': 'Liters Per Minute'}}}
