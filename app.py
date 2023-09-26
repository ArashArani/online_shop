from flask import Flask , Blueprint
from blueprints.general import app as general
from blueprints.user import app as user
from blueprints.admin import app as admin
import config
import extentions
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from models.model_users import User


app = Flask(__name__)

app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)


app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = config.SECRET_KEY

extentions.db.init_app(app)

csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()





with app.app_context():
    extentions.db.create_all()

app.run(debug=True)