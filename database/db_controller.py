import psycopg2
from . import db_config as config

class Controller:
    service = 'DB'
    logger = ''

    def __init__(self, logger):
        super().__init__()
        self.logger = logger
        self.logger.service_init(self.service)
        self.logger.log(self.service, 'Creating connection')
        conn = psycopg2.connect(dbname=config.NAME, user=config.USER,
                                password=config.PASSWORD, host=config.HOST)
        self.logger.log(self.service, 'Connection created')

        self.logger.log(self.service, 'Creating cursor')
        cursor = conn.cursor
        self.logger.log(self.service, 'Cursor created')