from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService

class Login_Controller(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/login", method=["GET","POST"], callback=self.prompt_login)
        self.app.route("/login/register", method=["GET","POST"], callback=self.prompt_register)

    def prompt_login(self):
        if request.method == "GET":
            # status -> 0 é neutro, 1 significa que o login deu errado, 2 signica que o cadastro deu certo
            status = request.query.get('status', 0)

            # A depender de status, o 'login_login.tpl' mostra avisos diferentes
            return self.render("login_login", status=status)
        else:
                #POST
            # Imprime os dados colocados no formulário 'view/login_login'
            user_nome = request.POST.nome
            user_senha = request.POST.senha
            print(user_nome)
            print(user_senha)

            # Se os dados forem válidos, redireciona para /pet/user_nome
            # Senão, manda fazer o login de novo redirecionando para /login com mensagem de erro
            user = self.user_service.get_by_nome(user_nome)

            if user != None:
                if user.senha == user_senha:
                    # Redireciona para /pet/nome_do_usuário, e daí passa a ser controlado pelo pet_controller.py
                    self.redirect(f'/pet/{user_nome}')
                else:
                    # Redireciona para login com status 3 (login deu errado, senha inválida)
                    self.redirect(f'/login?status=2')
            else:
                # Redireciona para login com status 1 (login deu errado, nome inválido)
                self.redirect('/login?status=1')
        
    def prompt_register(self):
        if request.method == "GET":
            # status -> 0 é neutro, 1 significa que o cadastro deu errado
            status = request.query.get('status', 0)

            return self.render("login_cadastro", status=status)
        else:
                #POST
            # Imprime os dados colocados no formulário 'view/login_cadastro'
            user_nome = request.POST.nome
            user_senha = request.POST.senha
            print(request.POST.nome)
            print(request.POST.senha)

            # Se os dados forem válidos, redireciona para /login com uma mensagem de sucesso de cadastro
            # Senão, manda fazer o cadastro de novo redirecionando para /login/cadastro com mensagem de erro
            user = self.user_service.get_by_nome(user_nome)

            if user == None:
                self.user_service.cadastrar()
                # Redireciona para /login com status 2 (cadastro deu certo)
                self.redirect('/login?status=2')
            else:
                # Redireciona para /login/cadastro com status 1 (cadastro deu errado)
                self.redirect('/login/register?status=1')

login_routes = Bottle()
login_controller = Login_Controller(login_routes)