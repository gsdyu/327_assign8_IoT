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





