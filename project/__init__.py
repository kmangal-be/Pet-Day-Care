from flask import Flask
import os

app = Flask(__name__)
from project.controller import *
