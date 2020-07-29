import psycopg2
from . import db_config as config

class Controller:
    service = 'DB'
    logger = ''

    def __init__(self, logger):
        super().__init__()
        logger = logger
        logger.service_init(service)
        logger.log(service, 'Creating connection')
        conn = psycopg2.connect(dbname=config.NAME, user=config.USER,
                                password=config.PASSWORD, host=config.HOST)
        logger.log(service, 'Connection created')

        logger.log(service, 'Creating cursor')
        cursor = conn.cursor
        logger.log(service, 'Cursor created')