#
# class OrderManager:
#     def __init__(self, db):
#         self.collection = db.get_collection("orders")
#
#     def create_order(self, order):
#         # self.collection.insert_one(order.to_dict())
#
#     def get_user_orders(self, user_id):
#         return list(self.collection.find({"user_id": user_id}))
#
#     def get_order_details(self, order_id):
#         return self.collection.find_one({"order_id": order_id})
#
#     def update_order_status(self, order_id, new_status):
#         self.collection.update_one({"order_id": order_id}, {"$set": {"status": new_status}})
#
#     def assign_courier(self, order_id, courier_id):
#         self.collection.update_one({"order_id": order_id}, {"$set": {"courier_id": courier_id}})
#
#     def get_assigned_orders_to_courier(self, courier_id):
#         return list(self.collection.find({"courier_id": courier_id}))