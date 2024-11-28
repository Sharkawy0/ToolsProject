from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
print("Connected to MongoDB!")

db = client['my_database']
collection = db['orders']
print("Database and collection created or accessed.")

# Step 3: Insert Data
order = {
    "order_id": 1,
    "status": "Pending",
    "pickup_location": "Location A",
    "delivery_location": "Location B"
}
collection.insert_one(order)
print("Inserted one order.")

