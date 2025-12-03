from bottle import Bottle, request, response
from .base_controller import BaseController
from services.user_service import UserService

class LoginController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/login", method=["GET","POST"], callback=self.prompt_login)
        self.app.route("/login/register", method=["GET","POST"], callback=self.prompt_register)

    def prompt_login(self):
        if request.method == "GET":
            status = request.query.get('status', 0)
            return self.render("login_login", status=status)

        else:
            # POST
            user_nome = request.POST.nome
            user_senha = request.POST.senha

            user = self.user_service.get_by_nome(user_nome)

            if user is not None and user.senha == user_senha:

                # SALVA COOKIE AQUI
                response.set_cookie("user_id", str(user.id), path="/")

                return self.redirect('/pet')

            elif user is None:
                print(user)
                return self.redirect('/login?status=1')  # usuário não existe
            else:
                return self.redirect('/login?status=2')  # senha errada
            
    def prompt_register(self):
        if request.method == "GET":
            status = request.query.get('status', 0)
            return self.render("login_cadastro", status=status)

        else:
            # POST
            user_nome = request.POST.nome
            user_senha = request.POST.senha

            # verifica se já existe
            user_existente = self.user_service.get_by_nome(user_nome)
            if user_existente:
                return self.redirect("/login/register?status=1")

            # cria novo usuário
            novo_user = self.user_service.create_user(user_nome, user_senha)

            # salva cookie
            response.set_cookie("user_id", str(novo_user.id), path="/")

            return self.redirect("/pet/create")
