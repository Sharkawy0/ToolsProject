# from Orders import OrderManager
#
#
# class UserManager:
#     def __init__(self, db):
#         self.collection = db.get_collection("users")
#
#     # def create_user(self, user):
#         self.collection.insert_one(user.to_dict())
#
#     def get_user_by_id(self, user_id):
#         return self.collection.find_one({"user_id": user_id})
#
#     def get_user_orders(self, user_id):
#         order_manager = OrderManager(self.collection.database)  # Pass the same database
#         return order_manager.get_user_orders(user_id)