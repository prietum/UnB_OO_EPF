from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService

class Pet_Controller(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        # O usuário não pode acessar /pet, joga de volta pro /login
        self.app.route("/pet", method="GET", callback=self.volta_pro_login)

        # O usuário pode acessar /pet/nome_do_usuario depois de acertar o login
        self.app.route("/pet/<user_nome>", method="GET", callback=self.temporario)

    def volta_pro_login(self):
        self.redirect('/login')

    def temporario(self, user_nome):
        # O argumento 'user_nome' vem de 'self.app.route(/pet/<user_nome>, ...)'
        
        if request.method == "GET":
            return self.render("pet", user_nome=user_nome)

pet_routes = Bottle()
pet_controller = Pet_Controller(pet_routes)