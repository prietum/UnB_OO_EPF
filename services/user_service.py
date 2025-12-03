from models.user import UserModel, User

class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def get_all(self):
        return self.user_model.get_all()

    def create_user(self, nome, senha):
        # delega a criação ao model
        return self.user_model.create_user(nome, senha)

    def get_by_nome(self, nome):
        return self.user_model.get_by_nome(nome)

    def edit_senha(self, user, nova_senha):
        user.senha = nova_senha
        self.user_model.update_senha(user.id, nova_senha)
        return user

    def delete_user(self, user_id):
        self.user_model.delete_user(user_id)
