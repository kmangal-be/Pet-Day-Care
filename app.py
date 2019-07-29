from project import app
import os

if __name__ == '__main__':
    if os.environ['ENV'] == 'dev':
        app.run(host="localhost", port=3000, debug=True)
    elif os.environ['ENV'] == 'prod':
        app.run(host="pet-day-care.herokuapp.com/")
