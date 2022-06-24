# Nur Khafidah | 19090075 | 6C
# Helina Putri | 19090133 | 6D

from ast import Import
from application import app
from flask import request, jsonify, make_response
from werkzeug.utils import secure_filename
from .modeldb import *
import datetime, random, string, os
import tensorflow as tf


# Create User
# http://127.0.0.1:5000/api/v1/users/signup
@app.route("/api/v1/users/signup", methods=["POST"])
def signup():
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    created_at = datetime.datetime.utcnow()
    user = Users(fullname=fullname, username=username, email=email, password=password, token='', face='', created_at=created_at)
    db.session.add(user)
    db.session.commit()
    return make_response(jsonify({"msg": "registrasi sukses", "username":username, "password":password}))


# Login User
# http://127.0.0.1:5000/api/v1/users/signin
@app.route("/api/v1/users/signin", methods=["POST"])
def signin():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        user = Users.query.filter(username == username and password == password).first()
        if user:
            token = ''.join(random.choices(string.ascii_lowercase + string.digits, k=25))
            Users.query.filter_by(username=username).update({'token': token})
            db.session.commit()
            return make_response(jsonify({"msg": "Login sukses", "token":token}))
        return make_response(jsonify({"msg": "username atau password salah"}))
    return make_response(jsonify({"msg": "Username atau password tidak boleh kosong"}))


# Face lock
# http://127.0.0.1:5000/api/v1/users/signin/faces
@app.route("/api/v1/users/signin/faces/<string:token>", methods=["POST"])
def faces(token):
    image = request.files['image']
    user = Users.query.filter_by(token == token).first()

    if user and image:
        model = '.\model\model-mobilenetV2.h5'
        finalimg = tf.keras.applications.mobilenet_v2.preprocess_input(image)
        pred =  model.predict(finalimg)
        results = imagenet_utils.decode_predictions(pred)
        return make_response(jsonify({"msg": "Login Successfull!", "result": results}))
    return make_response(jsonify({"msg": "Login Failed!", "result": results}))


# Upload File
def validate_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['UPLOAD_EXTENSIONS']

# http://127.0.0.1:5000/api/v1/files/upload
@app.route('/api/v1/files/upload/<string:token>', methods=["POST", "GET"])
def upFile(token):
    user = Users.query.filter_by(token=token).first()
    if user:
        upfile = request.files['file']
        time = datetime.datetime.now()
        if upfile and validate_file(upfile.filename):
            filename = secure_filename(upfile.filename)
            upfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            f1 = Files(filename=upfile.filename, type_file='', size_file='', owner_file=user.username, uploaded_at=time)
            db.session.add(f1)
            db.session.commit()
            return jsonify({"msg": "Upload File Successful !", "name":filename, "time":time})
        return jsonify({"msg": "Upload File Failed !"})


# Show File
# http://127.0.0.1:5000/api/v1/files/show
@app.route("/api/v1/files/show/<string:token>", methods=["GET"])
def showListFiles(token):
    user = Users.query.filter_by(token=token).first()

    if user:
        array_files =[]
        files = Files.query.all()
        for file in files:
            dict_logs = {}
            dict_logs.update({"filename": file.filename, "type_file": file.type_file, "size_file": file.size_file, "owner_file":file.owner_file, "uploaded_at": file.uploaded_at})
            array_files.append(dict_logs)
        return make_response(jsonify(array_files), 200, {'content-type':'application/json'})
    return make_response(jsonify({"msg": "Failed!"}))


# Delete file
# http://127.0.0.1:5000/api/v1/files/delete
@app.route("/api/v1/files/delete/<string:token>", methods=["POST"])
def deleteFiles(token):
    user = Users.query.filter_by(token=token).first()
    file = request.form.get('file')

    if user:
        file = Files.query.filter_by(filename = file).first() 
        db.session.delete(file)
        db.session.commit()

        return make_response(jsonify({"msg": "Delete was Successfull!"}))
    return make_response(jsonify({"msg": "Delete was Failed!"}))