from bottle import request
from models.user import UserModel, User

class UserService:
    def __init__(self):
        self.user_model = UserModel()


    def get_all(self):
        users = self.user_model.get_all()
        return users


    def cadastrar(self):
        nome = request.forms.get('nome')
        senha = request.forms.get('senha')

        user = User(nome=nome, senha=senha)
        self.user_model.add_user(user)


    def get_by_nome(self, user_nome):
        return self.user_model.get_by_nome(user_nome)


    def edit_senha(self, user):
        senha = request.forms.get('senha')

        user.senha = senha

        self.user_model.update_senha(user)


    def delete_user(self, user_id):
        self.user_model.delete_user(user_id)
