# orders/models.py

class UserManager:
    def __init__(self, mongo_db):
        self.collection = mongo_db.get_collection('users')

    def create_user(self, user_data):
        result = self.collection.insert_one(user_data)
        return str(result.inserted_id)

    def get_user(self, user_id):
        return self.collection.find_one({"_id": user_id})

class OrderManager:
    def __init__(self, mongo_db):
        self.collection = mongo_db.get_collection('orders')

    def create_order(self, user_id, pickup_location, dropoff_location, package_details, delivery_time):
        order_data = {
            "user_id": user_id,
            "pickup_location": pickup_location,
            "dropoff_location": dropoff_location,
            "package_details": package_details,
            "delivery_time": delivery_time,
            "status": "Pending"
        }
        result = self.collection.insert_one(order_data)
        return {"order_id": str(result.inserted_id), "status": "Order created"}

    def get_user_orders(self, user_id):
        return list(self.collection.find({"user_id": user_id}))

    def get_order_details(self, order_id):
        return self.collection.find_one({"_id": order_id})

    def update_order_status(self, order_id, new_status):
        result = self.collection.update_one({"_id": order_id}, {"$set": {"status": new_status}})
        if result.modified_count > 0:
            return {"status": "Order status updated"}
        return None

    def get_assigned_orders_to_courier(self, courier_id):
        return list(self.collection.find({"courier_id": courier_id}))