from flask import Blueprint
from model.userModel import userModel
from flask import request 
from datetime import datetime

obj=userModel()

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/users')
def user_signup_controller():
    return obj.user_signup_model()


@user_controller.route('/users/getall')
def get_all_users():
    return obj.getUsers()


@user_controller.route('/users/adduser',methods=["POST"])
def addUser():
    # "request form help us to get data from server sidre to us"
    return obj.add_user(request.form)

@user_controller.route('/users/updateuser',methods=["PUT"])
def updateUser():
    return obj.update_user(request.form)

@user_controller.route('/users/deleteuser/<id>',methods=["DELETE"])
def deleteUser(id):
    return obj.delete_user(id)


@user_controller.route('/users/patchuser/<id>',methods=["PATCH"])
def patchUser(id):
    return obj.patch_user(request.form , id)


@user_controller.route('/users/getall/limit/<limit>/page/<page>',methods=["GET"])
def userPagination(limit ,page):
    return obj.pagination_user(limit ,page)


@user_controller.route('/users/<uid>/upload/avatar',methods=["PUT"])
def uploadavtar(uid):
    '''
    In postman , under body section we get form data option in that we get option to upload file
     bydefault it is text
    ''' 
    file = request.files['avatar']
    # 
    uniqueName=str(datetime.now().timestamp()).replace(".","")
    filesplit= file.filename.split(".")
    extension=filesplit[len(filesplit)-1]

    file.save(f"uploads/{uniqueName}.{extension}")
    path=f"uploads/{uniqueName}.{extension}"
    return obj.addUserAvatar(uid,path)



@user_controller.route('/users/login',methods=["POST"])
def userLogIn():
    return obj.user_login(request.form)

