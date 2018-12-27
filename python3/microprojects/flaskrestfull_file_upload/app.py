import os
import time

from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
PASSWORD = "<dummy_password>"

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "<dummy_scret_key>"

api = Api(app)

class Files(Resource):
    def get(self):
        return {'msg': 'Just POST man!'}
    
    def post(self):
        # password check
        if 'password' not in request.form or request.form['password'] != PASSWORD:
            return {
                "msg": "Password field missing or incorrect"
            }, 401

        # check if the post request has the file part
        print('request.files', request.files)
        if 'upload' not in request.files:
            return {"msg": 'No file part'}, 400
        file = request.files['upload']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return {"msg": 'No filename'}, 400
        if file:
            filename = secure_filename(file.filename)
            prefix = str(int(time.time())) + "_"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], prefix+filename))
            return {"msg": 'Received with success_tnx'}, 202

api.add_resource(Files, '/upload')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=False)
 