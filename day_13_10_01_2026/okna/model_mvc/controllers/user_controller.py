class UserController:
    def __init__(self, model):
        self.model = model

    def create_user(self, name, email):
        if not name or email:
            raise ValueError("Brak Danych")
        self.model.add_user(name, email)

    def list_users(self):
        return self.model.get_users()
