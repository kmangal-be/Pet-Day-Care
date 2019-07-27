echo "setting up virtual environment"
python3 -m venv venv

# activate virtual environment
echo "activating virtual environment"
. venv/bin/activate

echo "virtual environment created successfully"

# install Flask
echo "install flask"
pip install Flask

pip install flask_sqlalchemy
pip install SQLAlchemy
pip install flask_script
pip install flask_migrate
pip install psycopg2-binary
echo "--- Flask Installed Successfully ---"

# Setting up environment variables
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost:5432/pet_day_care"
export ENV=dev

python manager.py db init
python manager.py db migrate
python manager.py db upgrade
python app.py