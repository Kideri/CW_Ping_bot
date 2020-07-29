import psycopg2
from . import db_config as config

class Controller:
    service = 'DB'
    logger = ''

    def __init__(self, logger):
        super().__init__()
        Controller.logger = logger
        Controller.logger.service_init(Controller.service)
        Controller.logger.log(service, 'Creating connection')
        conn = psycopg2.connect(dbname=config.NAME, user=config.USER,
                                password=config.PASSWORD, host=config.HOST)
        Controller.logger.log(service, 'Connection created')

        Controller.logger.log(service, 'Creating cursor')
        cursor = conn.cursor
        Controller.logger.log(service, 'Cursor created')