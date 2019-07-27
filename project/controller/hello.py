from project import app
from flask import render_template


@app.route('/ping', methods=['GET'])
def index():
    return 'pong';
