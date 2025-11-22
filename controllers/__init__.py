from bottle import Bottle
from controllers.login_controller import login_routes
from controllers.pet_controller import pet_routes

def init_controllers(app: Bottle):
    app.merge(login_routes)
    app.merge(pet_routes)
