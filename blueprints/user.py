from flask import Blueprint
import models.model_user
app = Blueprint("user",__name__)


@app.route('/user')
def main():
    return "This is User Page "