from flask import url_for
from flask import send_from_directory, current_app
from flask_restx import Namespace, Resource
from CTFd.utils import get_app_config
# from ...utils import CHALLENGES_DIR
import pathlib
import os
from os import path


CHALLENGES_DIR = pathlib.Path("/var/challenges")


download_namespace = Namespace("download")

@download_namespace.route("/<path:filename>")
class downloadBinary(Resource):
    def get(self, filename):
        #tmp = "/" + category + "/" + filename + "/" + filename
        uploads = os.path.join(current_app.root_path, get_app_config('UPLOAD_FOLDER'))
        return send_from_directory(directory=uploads, filename=filename)
        return path.exists("logs.txt")

