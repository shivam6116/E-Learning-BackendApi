
from flask import Flask
from controller.userController import user_controller
from controller.productController import productController



app = Flask(__name__)


app.register_blueprint(user_controller)
app.register_blueprint(productController)


@app.route("/home")
def home():
    return "this is home page"


if __name__ == '__main__':
    app.run(debug=True)
