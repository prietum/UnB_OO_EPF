from models.user import UserModel, User

class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def get_all(self):
        return self.user_model.get_all()

    def create_user(self, nome, senha):
        # cria objeto User
        user = User(nome=nome, senha=senha)

        # salva no model
        self.user_model.add_user(user)

        # retorna para o controller poder pegar o id
        return user

    def get_by_nome(self, nome):
        return self.user_model.get_by_nome(nome)

    def edit_senha(self, user, nova_senha):
        user.senha = nova_senha
        self.user_model.update_senha(user)
        return user

    def delete_user(self, user_id):
        self.user_model.delete_user(user_id)
