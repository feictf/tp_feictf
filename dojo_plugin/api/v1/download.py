from flask import url_for
from flask import send_from_directory
from flask_restx import Namespace

download_namespace = Namespace("download")

@download_namespace.route("/")
def download():
    # uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    # send_from_directory(directory="/", filename="docker.py")
    return "<h1>PICE TAM</h1>"