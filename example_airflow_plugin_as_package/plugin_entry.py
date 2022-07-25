"""
!! DO NOT use autodoc in this module.
"""
# http://airflow.apache.org/docs/apache-airflow/stable/plugins.html#interface
from airflow.plugins_manager import AirflowPlugin


class Plugin(AirflowPlugin):
    name = 'foo'
    appbuilder_menu_items = [{
        "name": "google",
        "category": "FOO!!",
        "category_icon": "fa-th",
        "href": "https://google.com"
    }, {
        "name": "reddit",
        "category": "FOO!!",
        "category_icon": "fa-th",
        "href": "https://www.reddit.com"
    }, ]
