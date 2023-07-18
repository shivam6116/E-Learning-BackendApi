from flask import Blueprint

productController = Blueprint('productController', __name__)

@productController.route('/product')
def get_product():
    return 'List of product'
