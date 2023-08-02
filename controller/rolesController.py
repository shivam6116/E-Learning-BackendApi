from model.roles import RolesModel
from flask import Blueprint
from flask import request

rolesObj=RolesModel()

roleController=Blueprint('roleController', __name__)


@roleController.route('/roles/allroles')
def getRoles():
    return rolesObj.getAllRoles()


@roleController.route('/roles/addRole',methods=['POST'])
def addRoles():
    return rolesObj.add_roles(request.form)
    

@roleController.route('/roles/updatrole',methods=["PUT"])
def updateUser():
    return rolesObj.update_roles(request.form)



@roleController.route('/roles/deleteRole/<id>',methods=["DELETE"])
def deleteUser(id):
    return rolesObj.delete_roles(id)





