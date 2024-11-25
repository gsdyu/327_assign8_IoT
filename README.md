# IoT System - Assignment 8 [Group 30] Justin Chong, Nam Ton

## System Requirements
- Python 3.x
- MongoDB
- Required Python packages: pymongo python-dotenv pytz (For the env file)

## Setup Instructions

1. Clone the repository

2. Create .env file in project root with your MongoDB URI: (also add a git ignore with a .env just in case cause you don't want to share it to the public)
   MONGODB_URI=mongodb+srv://username:<password>@cluster0.xxxx.mongodb.net/?retryWrites=true&w=majority

3. Configure Database:
- Database name: 'test' (This is example this is where you would put your database name)
- Collection: 'Stuff_virtual' (This is example this is where you would put your collection name)
- Ensure your IoT devices are sending data to the correct collection

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
{
  "_id": { "$oid": "67441679d50fad3a8935b40e" },
  "cmd": "publish",
  "retain": false,
  "qos": { "$numberInt": "0" },
  "dup": false,
  "length": { "$numberInt": "286" },
  "payload": {
    "timestamp": "1732515449",
    "topic": "dishwasher/data/sub",
    "parent_asset_uid": "dishwasher_id",
    "asset_uid": "bvw-611-q14-g94",
    "board_name": "Sipeed MAIX Bit - dishwasher_board",
    "dish_current_Ta12-100": "1.4927",
    "dish_water_YF-S201": "20.1028"
  },
  "topic": "dishwasher/data/sub",
  "time": {
    "$date": { "$numberLong": "1732515449000" }
  },
  "__v": { "$numberInt": "0" }
}

### SmartFridge1 Payload
{
  "_id": { "$oid": "67441689d50fad3a8935b4b4" },
  "cmd": "publish",
  "retain": false,
  "qos": { "$numberInt": "0" },
  "dup": false,
  "length": { "$numberInt": "319" },
  "payload": {
    "timestamp": "1732515465",
    "topic": "fridge1/data/sub",
    "parent_asset_uid": "fridge-1_id",
    "asset_uid": "689-7px-4e3-ads",
    "board_name": "Arduino Due - bob",
    "fridge1_moist_AM2320": "47.6483",
    "fridge1_temp-resis_10K3A1-SERIES-1": "176580.8155",
    "fridge1_current_Ta12-100": "2.2211"
  },
  "topic": "fridge1/data/sub",
  "time": {
    "$date": { "$numberLong": "1732515465000" }
  },
  "__v": { "$numberInt": "0" }
}

### SmartFridge2 Payload
{
  "_id": { "$oid": "67441695d50fad3a8935b51c" },
  "cmd": "publish",
  "retain": false,
  "qos": { "$numberInt": "0" },
  "dup": false,
  "length": { "$numberInt": "366" },
  "payload": {
    "timestamp": "1732515476",
    "topic": "fridge2/data/sub",
    "parent_asset_uid": "fridge-2_id",
    "asset_uid": "f80e23bb-66af-43b1-a6e9-7b4af3580568",
    "board_name": "board 1 e9605a66-012d-440f-bab0-884dcc419453",
    "fridge2_moist_AM2320": "0.0007",
    "fridge2_current_Ta12-100": "2.5980",
    "fridge2_temp-resis_10K3A1-SERIES-1": "183793.1150"
  },
  "topic": "fridge2/data/sub",
  "time": {
    "$date": { "$numberLong": "1732515476000" }
  },
  "__v": { "$numberInt": "0" }
}

## Metadata

### Dishwasher Metadata
{
  "_id": { "$oid": "67441186def8b71c8fb5f7a3" },
  "assetUid": "dishwasher_id",
  "parentAssetUid": null,
  "eventTypes": [],
  "latitude": { "$numberInt": "1" },
  "longitude": { "$numberInt": "1" },
  "customAttributes": {
    "generationDate": "2024-11-25T05:55:59.183832Z",
    "type": "DEVICE",
    "name": "dishwasher",
    "children": [
      {
        "assetUid": "bvw-611-q14-g94",
        "parentAssetUid": "dishwasher_id",
        "customAttributes": {
          "type": "BOARD",
          "name": "Sipeed MAIX Bit - dishwasher_board",
          "children": [
            {
              "assetUid": "383-jm3-22b-4cz",
              "parentAssetUid": "bvw-611-q14-g94",
              "customAttributes": {
                "type": "SENSOR",
                "name": "dish_current_Ta12-100",
                "unit": "mA",
                "minValue": { "$numberInt": "0" },
                "maxValue": { "$numberInt": "5" },
                "desiredMinValue": { "$numberDouble": "0.1" },
                "desiredMaxValue": { "$numberDouble": "4.99" }
              }
            },
            {
              "assetUid": "u19-top-1o9-1jq",
              "parentAssetUid": "bvw-611-q14-g94",
              "customAttributes": {
                "type": "SENSOR",
                "name": "dish_water_YF-S201",
                "unit": "Liters Per Minute",
                "minValue": { "$numberInt": "1" },
                "maxValue": { "$numberInt": "30" },
                "desiredMinValue": { "$numberDouble": "1.01" },
                "desiredMaxValue": { "$numberDouble": "29.99" }
              }
            }
          ]
        }
      }
    ]
  },
  "__v": { "$numberInt": "0" }
}

### SmartFridge1 Metadata
{
  "_id": { "$oid": "674411b0def8b71c8fb5f7a7" },
  "assetUid": "fridge-1_id",
  "parentAssetUid": null,
  "eventTypes": [],
  "latitude": { "$numberInt": "2" },
  "longitude": { "$numberInt": "2" },
  "customAttributes": {
    "generationDate": "2024-11-25T05:56:47.486974Z",
    "type": "DEVICE",
    "name": "SmartFridge1",
    "children": [
      {
        "assetUid": "689-7px-4e3-ads",
        "parentAssetUid": "fridge-1_id",
        "customAttributes": {
          "type": "BOARD",
          "name": "Arduino Due - bob",
          "children": [
            {
              "assetUid": "890-6o0-p8u-pbq",
              "parentAssetUid": "689-7px-4e3-ads",
              "customAttributes": {
                "type": "SENSOR",
                "name": "fridge1_moist_AM2320",
                "unit": "%",
                "minValue": { "$numberInt": "0" },
                "maxValue": { "$numberInt": "100" },
                "desiredMinValue": { "$numberDouble": "0.01" },
                "desiredMaxValue": { "$numberDouble": "99.99" }
              }
            },
            {
              "assetUid": "yof-32c-igw-lkd",
              "parentAssetUid": "689-7px-4e3-ads",
              "customAttributes": {
                "type": "SENSOR",
                "name": "fridge1_temp-resis_10K3A1-SERIES-1",
                "unit": "ohm",
                "minValue": { "$numberInt": "341" },
                "maxValue": { "$numberInt": "336098" },
                "desiredMinValue": { "$numberDouble": "341.01" },
                "desiredMaxValue": { "$numberDouble": "336097.99" }
              }
            },
            {
              "assetUid": "aas-25c-3l0-252",
              "parentAssetUid": "689-7px-4e3-ads",
              "customAttributes": {
                "type": "SENSOR",
                "name": "fridge1_current_Ta12-100",
                "unit": "mA",
                "minValue": { "$numberInt": "0" },
                "maxValue": { "$numberInt": "5" },
                "desiredMinValue": { "$numberDouble": "0.1" },
                "desiredMaxValue": { "$numberDouble": "4.99" }
              }
            }
          ]
        }
      }
    ]
  },
  "__v": { "$numberInt": "0" }
}

### SmartFridge2 Metadata
{
  "_id": { "$oid": "674411c1def8b71c8fb5f7aa" },
  "assetUid": "fridge-2_id",
  "parentAssetUid": null,
  "eventTypes": [],
  "latitude": { "$numberInt": "3" },
  "longitude": { "$numberInt": "3" },
  "customAttributes": {
    "generationDate": "2024-11-25T05:57:09.291782Z",
    "type": "DEVICE",
    "name": "SmartFridge2",
    "children": [
      {
        "assetUid": "f80e23bb-66af-43b1-a6e9-7b4af3580568",
        "parentAssetUid": "fridge-2_id",
        "customAttributes": {
          "type": "BOARD",
          "name": "board 1 e9605a66-012d-440f-bab0-884dcc419453",
          "children": [
            {
              "assetUid": "97d5f063-a88d-42ca-82ea-6baa6001f446",
              "parentAssetUid": "f80e23bb-66af-43b1-a6e9-7b4af3580568",
              "customAttributes": {
                "type": "SENSOR",
                "name": "fridge2_moist_AM2320",
                "unit": "%",
                "minValue": { "$numberInt": "0" },
                "maxValue": { "$numberInt": "100" },
                "desiredMinValue": { "$numberDouble": "0.01" },
                "desiredMaxValue": { "$numberDouble": "99.99" }
              }
            },
            {
              "assetUid": "7236c9c3-fc72-4668-86c6-5414e01cab7a",
              "parentAssetUid": "f80e23bb-66af-43b1-a6e9-7b4af3580568",
              "customAttributes": {
                "type": "SENSOR",
                "name": "fridge2_current_Ta12-100",
                "unit": "mA",
                "minValue": { "$numberInt": "0" },
                "maxValue": { "$numberInt": "5" },
                "desiredMinValue": { "$numberDouble": "0.1" },
                "desiredMaxValue": { "$numberDouble": "4.99" }
              }
            },
            {
              "assetUid": "d6742234-f21f-4a2a-b036-18907e06fa8a",
              "parentAssetUid": "f80e23bb-66af-43b1-a6e9-7b4af3580568",
              "customAttributes": {
                "type": "SENSOR",
                "name": "fridge2_temp-resis_10K3A1-SERIES-1",
                "unit": "ohm",
                "minValue": { "$numberInt": "341" },
                "maxValue": { "$numberInt": "336098" },
                "desiredMinValue": { "$numberDouble": "341.01" },
                "desiredMaxValue": { "$numberDouble": "336097.99" }
              }
            }
          ]
        }
      }
    ]
  },
  "__v": { "$numberInt": "0" }
}

### DEVICE_METADATA (Modified metadata):

  {'SmartFridge1': {'current': {'board_name': 'Arduino Due - bob',
                                'device_name': 'SmartFridge1',
                                'sensor_name': 'fridge1_current_Ta12-100',
                                'unit': 'mA'},
                    'moist': {'board_name': 'Arduino Due - bob',
                              'device_name': 'SmartFridge1',
                              'sensor_name': 'fridge1_moist_AM2320',
                              'unit': '%'},
                    'temp-resis': {'board_name': 'Arduino Due - bob',
                                   'device_name': 'SmartFridge1',
                                   'sensor_name': 'fridge1_temp-resis_10K3A1-SERIES-1',
                                   'unit': 'ohm'}},
   'SmartFridge2': {'current': {'board_name': 'board 1 '
                                              'e9605a66-012d-440f-bab0-884dcc419453',
                                'device_name': 'SmartFridge2',
                                'sensor_name': 'fridge2_current_Ta12-100',
                                'unit': 'mA'},
                    'moist': {'board_name': 'board 1 '
                                            'e9605a66-012d-440f-bab0-884dcc419453',
                              'device_name': 'SmartFridge2',
                              'sensor_name': 'fridge2_moist_AM2320',
                              'unit': '%'},
                    'temp-resis': {'board_name': 'board 1 '
                                                 'e9605a66-012d-440f-bab0-884dcc419453',
                                   'device_name': 'SmartFridge2',
                                   'sensor_name': 'fridge2_temp-resis_10K3A1-SERIES-1',
                                   'unit': 'ohm'}},
   'dishwasher': {'current': {'board_name': 'Sipeed MAIX Bit - dishwasher_board',
                              'device_name': 'dishwasher',
                              'sensor_name': 'dish_current_Ta12-100',
                              'unit': 'mA'},
                  'water': {'board_name': 'Sipeed MAIX Bit - dishwasher_board',
                            'conversation_factor': 0.264172,
                            'device_name': 'dishwasher',
                            'sensor_name': 'dish_water_YF-S201',
                          'unit': 'Liters Per Minute'}}}
