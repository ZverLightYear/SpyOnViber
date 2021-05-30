import pytest

from core.config_parser import parse_config
from core.db_controllers.app_db_controller import ApplicationDatabaseController
from core.models.app.chat import Chat
from core.models.app.chat_relation import ChatRelation
from core.models.app.contact import Contact
from core.models.app.message import Message


@pytest.fixture(scope='function', autouse=True)
def setup_dbc():
    app_db_conf, _, _ = parse_config(path_to_config='../')

    app_dbc = ApplicationDatabaseController(app_db_conf)
    return app_dbc


class TestApplicationDatabaseControllerSuite:
    def test_connection_string_with_full_config(self):
        conf = {
            "drivername": "sqlite",
            "username": "user",
            "password": "password",
            "host": "localhost",
            "port": "9876",
            "database": "db_name"
        }
        app_dbc = ApplicationDatabaseController(conf)
        assert app_dbc.url.__str__() == "sqlite://user:password@localhost:9876/db_name"

    def test_get_last_model_id_query(self, setup_dbc):
        app_dbc = setup_dbc
        app_dbc.connect()

        res = app_dbc.get_last_model_id(Message)
        assert res[0] is not None
        res = app_dbc.get_last_model_id(Chat)
        assert res[0] is not None
        res = app_dbc.get_last_model_id(Contact)
        assert res[0] is not None
        res = app_dbc.get_last_model_id(ChatRelation)
        assert res[0] is not None and res[1] is not None

