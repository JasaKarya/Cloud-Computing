import os

# Get the base directory of the current file
basedir = os.path.abspath(os.path.dirname(__file__))

# Define the SQLite database URI
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite")