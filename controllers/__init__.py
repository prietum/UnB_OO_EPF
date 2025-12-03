from bottle import Bottle
from controllers.login_controller import LoginController
from controllers.pet_controller import PetController

def init_controllers(app: Bottle):
    print("Registrando controllers...")

    # Controller de login
    LoginController(app)

    # Controller do tamagotchi
    PetController(app)