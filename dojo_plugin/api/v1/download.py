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

@download_namespace.route("/<path:category>/<path:filename>")
class downloadBinary(Resource):
    def get(self, category, filename):
        tmp = category + "/" + filename + "/" + filename
        challenges_folder = os.path.join(current_app.root_path, "/var/challenges/" + tmp)
        return send_from_directory(directory=challenges_folder, filename=filename)

