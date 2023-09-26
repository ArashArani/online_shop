from flask import Blueprint , render_template , request , redirect , session
from flask_login import login_user
from models.model_users import User
from passlib.hash import sha256_crypt
from extentions import db


app = Blueprint('user',__name__)

@app.route('/user/login' , methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')
    else:
        register = request.form.get('register', None)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        phone = request.form.get('phone', None)
        address = request.form.get('address', None)

        if register != None :
            user = User(username = username , password = sha256_crypt.encrypt(password),phone=phone,address=address)

            db.session.add(user)
            db.session.commit()
            login_user(user)

            return redirect('/user/dashboard')