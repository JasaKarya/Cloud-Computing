from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
import os

def create_app():
    app = Flask(__name__)
    api = Api(app)
    CORS(app)

    # Configure database before initializing db
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

    # Initialize db within the create_app function
    db = SQLAlchemy(app)

    # Create database model
    class ModelDatabase(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nama = db.Column(db.String(100))
        umur = db.Column(db.Integer)
        alamat = db.Column(db.TEXT)

        def save(self):
            try:
                db.session.add(self)
                db.session.commit()
                return True
            except:
                return False

    # Create database tables
    with app.app_context():
        db.create_all()

    identitas = {}

    #Class Get and Post Data
    class StartResource(Resource):
        def get(self):
            query = ModelDatabase.query.all()
            output = [
                {
                    "id": data.id,
                    "nama": data.nama,
                    "umur": data.umur,
                    "alamat": data.alamat
                } 
                for data in query
            ]

            response = {
                "msg": "Query data sukses",
                "code": 200,
                "data": output
            }

            return response, 200

        def post(self):
            dataNama = request.form["nama"]
            dataUmur = request.form["umur"]
            dataAlamat = request.form["alamat"]

            model = ModelDatabase(nama=dataNama, umur=dataUmur, alamat=dataAlamat)
            model.save()

            response = {
                "msg": "Data berhasil dimasukkan",
                "code": 200
            }

            return response, 200
    
        # delete all
        def delete(self):
            query = ModelDatabase.query.all()

            for data in query:
                db.session.delete(data)
                db.session.commit()

            response = {
                "msg":"Semua data berhasil dihapus",
                "code":200
            }

            return response, 200
    
    class UpdateResource(Resource):
        def put(self, id):
            # konsumsi id itu untuk query di model databasenya
            # pilih data yang ingin diedit berdasarkan id yang dimasukan
            query = ModelDatabase.query.get(id)

            # form untuk pegeditan data
            editNama = request.form["nama"]
            editUmur = request.form["umur"]
            editAlamat = request.form["alamat"]

            # mereplace nilai yang ada di setiap field/kolom
            query.nama = editNama
            query.umur = editUmur
            query.alamat = editAlamat
            db.session.commit()

            response = {
                "msg" : "Edit Data Berhasil",
                "code": 200
            }

            return response, 200

        # delete by id
        def delete(self, id):
            queryData = ModelDatabase.query.get(id)

            # panggil method untuk delete data by id
            db.session.delete(queryData)
            db.session.commit()

            response = {
                "msg" : "Delete Data Berhasil",
                "code" : 200
            }
            return response, 200


    api.add_resource(StartResource, "/api", methods=["GET", "POST", "DELETE"])
    api.add_resource(UpdateResource, "/api/<id>", methods=["PUT", "DELETE"])

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5005)
