from flask import Blueprint , render_template , request , session , redirect , abort
import config
app = Blueprint("admin",__name__)


@app.route('/admin/login' , methods = ["POST","GET"])
def main():
    if request.method == "POST":
        username= request.form.get('username',None)
        password= request.form.get('password',None)

        if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD :
            session ['Admin_Login'] = username
            return redirect('/admin/dashboard')
        else:
            return redirect('/admin/login')
    else :
        return render_template ("/admin/login.html")


@app.route('/admin/dashboard' , methods = ["GET"])
def dashboard():
    if session.get('Admin_Login', None) == None:
        abort(403)
    return "dashboard"