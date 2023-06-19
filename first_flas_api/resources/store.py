import uuid
from flask import request
from flask.views import MethodView
from flask_florest import Blueprint, abort
from db import stores
