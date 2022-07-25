"""
!! DO NOT use autodoc in this module.
"""
# http://airflow.apache.org/docs/apache-airflow/stable/plugins.html#interface
from airflow.plugins_manager import AirflowPlugin

from example_airflow_plugin_as_package.blueprint import flask_blueprints
from example_airflow_plugin_as_package.blueprint.fab import appbuilder_menu_items


class Plugin(AirflowPlugin):
    name = 'foo'
    flask_blueprints = flask_blueprints
    appbuilder_menu_items = appbuilder_menu_items
