from model.endpoints import EndPointsModel
from flask import Blueprint
from flask import request

epObj= EndPointsModel()
epController=Blueprint('epController', __name__)


@epController.route('/EP/allEndPoints')
def get_roles():
    return epObj.getAllEndPoints()


@epController.route('/EP/addEP',methods=['POST'])
def addEndPoints():
    return epObj.add_endPoints(request.form)
    

@epController.route('/EP/updateEP',methods=["PUT"])
def updateEP():
    return epObj.update_endpoints(request.form)


@epController.route('/EP/deleteEP/<id>',methods=["DELETE"])
def deleteEP(id):
    return epObj.delete_endpoints(id)

