from flask import url_for
from flask import send_from_directory
from flask_restx import Namespace, Resource
from ...utils import CHALLENGES_DIR
from os import path

download_namespace = Namespace("download")


@download_namespace.route("/<path:category>/<path:filename>")
class downloadBinary(Resource):
    def get(self, category, filename):
        tmp = category + "/" + filename + "/" + filename
        # return send_from_directory("opt/dojo/data/challenges/" + tmp, filename)
        return path.exists("logs.txt")
    
