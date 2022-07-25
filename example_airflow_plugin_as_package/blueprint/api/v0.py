from airflow.www.app import csrf
from flask import Blueprint, abort

api = Blueprint('airs-api-v0', __name__, url_prefix='/airs/api/v0')
csrf.exempt(api)


@api.route("/namespace", strict_slashes=False, methods=["GET"])
def list_namespace():
    return "[]"


@api.route("/namespace", methods=["POST"])
def rsync_create_namespace():
    return "body", 201


@api.route("/namespace/<name>", methods=["GET"])
def get_namespace(name: str):
    abort(404)


@api.route("/namespace/<name>/checkout", methods=["PUT"])
def checkout_namespace(name: str):
    abort(404)


@api.route("/namespace/<name>/rsync", methods=["GET"])
def rsync_namespace_get(name: str):  # CLI request rsync command.
    abort(403)


@api.route("/namespace/<name>/rsync", methods=["PUT"])
def rsync_namespace_put(name: str):
    abort(404)
