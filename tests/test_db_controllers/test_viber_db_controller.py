import pytest

from sqlalchemy.exc import OperationalError

from core.config_parser import parse_config
from core.db_controllers.viber_db_controller import ViberDatabaseController
from core.models.viber.chat import Chat
from core.models.viber.chat_relation import ChatRelation
from core.models.viber.contact import Contact
from core.models.viber.message import Message
from core.models.viber.event import Event


@pytest.fixture(scope='function', autouse=True)
def setup_dbc():
    _, viber_db_conf, _ = parse_config(path_to_config='../')

    viber_dbc = ViberDatabaseController(viber_db_conf)
    return viber_dbc


class TestViberDatabaseControllerSuite:
    def test_connection_string_cut_config(self):
        conf = {
            "drivername": "sqlite",
            "database": "db_name"
        }
        viber_dbc = ViberDatabaseController(conf)
        assert viber_dbc.url.__str__() == "sqlite:///db_name"

    def test_active_query(self, setup_dbc):
        viber_dbc = setup_dbc
        viber_dbc.connect()

        with pytest.raises(OperationalError):
            viber_dbc.drop_tables()
        with pytest.raises(OperationalError):
            viber_dbc.create_tables_with_check()

    def test_select_by_model_dict(self, setup_dbc):
        viber_dbc = setup_dbc
        assert list(viber_dbc.select_by_model.keys()) == \
               ['ChatInfo', 'Contact', 'ChatRelation', 'Events', 'Messages']

    def test_get_new_rows_query(self, setup_dbc):
        viber_dbc = setup_dbc
        viber_dbc.connect()

        res = viber_dbc.get_new_rows(Message, (0,))
        assert len(res) > 0
        res = viber_dbc.get_new_rows(Chat, (0,))
        assert len(res) > 0
        res = viber_dbc.get_new_rows(Contact, (0,))
        assert len(res) > 0
        res = viber_dbc.get_new_rows(ChatRelation, (0, 0))
        assert len(res) > 0
        res = viber_dbc.get_new_rows(Event, (0,))
        assert len(res) > 0

