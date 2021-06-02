from SQLAlchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
sqlalchemy = SQLAlchemy(host='sql-container', port=3306)

