class User:
    def __init__(self, user_id, name, email, phone, password, user_type='user'):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.user_type = user_type  # 'user' or 'admin'

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "password": self.password,
            "user_type": self.user_type
        }