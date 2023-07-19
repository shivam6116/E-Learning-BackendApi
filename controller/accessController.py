from model.access import AccessModel
from flask import Blueprint
from flask import request

accObj= AccessModel()
accController=Blueprint('accController', __name__)


@accController.route('/Access/allAccess')
def get_Access():
    return accObj.getAllaccess()

@accController.route('/Access/addAccess',methods=['POST'])
def addAccess():
    return accObj.add_Access(request.form)
    


@accController.route('/Access/updateAccess',methods=["PUT"])
def updateAccess():
    return accObj.update_Access(request.form)


@accController.route('/Access/deleteAccess/<id>',methods=["DELETE"])
def deleteEP(id):
    return accObj.delete_Access(id)

