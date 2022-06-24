# Nur Khafidah | 19090075 | 6C
# Helina Putri | 19090133 | 6D

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/db_odrive'
app.config['UPLOAD_FOLDER'] = 'dump'
app.config['UPLOAD_EXTENSIONS'] = ['zip','pdf','doc','docx','xls','xlsx','ppt','pptx','mp4','mkv','mp3','wav','jpg', 'jpeg', 'png', 'gif']
db = SQLAlchemy(app)

from application.backend import routes