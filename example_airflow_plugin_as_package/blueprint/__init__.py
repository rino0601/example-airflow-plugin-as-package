"""
Package for airsflow flask blueprint

.. rubric:: SubModules

.. autosummary::
   :toctree: ../_autodoc

   api
   fab

"""
import random

from airflow.configuration import conf
from flask import Blueprint, jsonify

from example_airflow_plugin_as_package.blueprint.api import api_v0

_AIRFLOW__CORE__DAGS_FOLDER = conf.get('core', 'dags_folder')

bp_airs = Blueprint(
    "airs", __name__,
    url_prefix='/airs',
    template_folder='templates',  # registers airflow/plugins/templates as a Jinja template folder
)


@bp_airs.route("/api/action/checkout", methods=["GET"])
def api_checkout():
    condi = list(range(17))
    random.shuffle(condi)
    if condi[0] % 2:
        return jsonify(ok=True, condi=condi)
    return jsonify(ok=False, err_msg="blah blah blah"), 500


flask_blueprints = [bp_airs, api_v0]
