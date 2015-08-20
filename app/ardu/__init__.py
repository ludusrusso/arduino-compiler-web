from flask import Blueprint
ardu = Blueprint('ardu', __name__) 

from . import views
