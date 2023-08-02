from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from controller.userController import user_controller
from controller.productController import productController
from controller.rolesController import roleController
from controller.endpointsController import epController
from controller.accessController import accController


app = Flask(__name__)


app.register_blueprint(user_controller)
app.register_blueprint(productController)
app.register_blueprint(roleController)
app.register_blueprint(epController)
app.register_blueprint(accController)


@app.route("/")
def home():
    return "Welcome To Flask RestFul APIs"


if __name__ == '__main__':
    app.run(debug=True)
