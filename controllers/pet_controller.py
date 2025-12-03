from bottle import request, redirect, template, Bottle
from services.pet_service import PetService


class PetController:
    def __init__(self, app: Bottle):
        self.app = app
        self.service = PetService()
        self.register_routes()

    def register_routes(self):
        app = self.app

        # -----------------------------
        #   Criar Pet
        # -----------------------------
        @app.route('/pet/create', method=['GET', 'POST'])
        def create_pet():
            user_id = request.get_cookie("user_id")
            if not user_id:
             return redirect('/login')
            if request.method == 'POST':
                nome = request.forms.get('nome')

                if not nome:
                    return template('create_pet', error='Informe um nome')

                # cria e salva pet
                self.service.create_pet_for_user(int(user_id), nome)
                return redirect('/pet')

            return template('create_pet')

        # -----------------------------
        #   Exibir Pet
        # -----------------------------
        @app.route('/pet')
        def show_pet():
            user_id = request.get_cookie("user_id")
            if not user_id:
                return redirect('/login')

            pet = self.service.get_pet_by_user(int(user_id))

            if not pet:
                return redirect('/pet/create')

            return template('pet', pet=pet)

        # -----------------------------
        #   Ações
        # -----------------------------
        @app.route('/pet/comer')
        def pet_comer():
            user_id = request.get_cookie("user_id")
            self.service.comer(int(user_id))
            return redirect('/pet')

        @app.route('/pet/brincar')
        def pet_brincar():
            user_id = request.get_cookie("user_id")
            self.service.brincar(int(user_id))
            return redirect('/pet')

        @app.route('/pet/dormir')
        def pet_dormir():
            user_id = request.get_cookie("user_id")
            self.service.dormir(int(user_id))
            return redirect('/pet')
        
        @app.route('/pet/treinar')
        def pet_treinar():
            user_id = request.get_cookie("user_id")
            self.service.treinar(int(user_id))
            return redirect('/pet')
        
        @app.route('/pet/banhar')
        def pet_banhar():
            user_id = request.get_cookie("user_id")
            self.service.banhar(int(user_id))
            return redirect('/pet')
        
        @app.route('/pet/curar')
        def pet_curar():
            user_id = request.get_cookie("user_id")
            self.service.curar(int(user_id))
            return redirect('/pet')