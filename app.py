from project import app
from flask_sqlalchemy import SQLAlchemy
import os

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Pet
if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)
