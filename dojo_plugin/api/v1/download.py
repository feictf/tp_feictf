from flask import url_for
from flask import send_from_directory
from flask_restx import Namespace, Resource

download_namespace = Namespace("download")

@download_namespace.route("")
class downloadBinary(Resource):
    def get(self):
        return "<h1>PICE TAM</h1>"
    
