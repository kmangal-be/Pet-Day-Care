import os, glob
from flask import Blueprint

bp = Blueprint('api', __name__)
from project.controller import hello, employee
