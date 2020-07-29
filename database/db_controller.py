import psycopg2
import .db_config as config
from core import logger

class Controller:
    service = 'DB'

    def __init__(self):
        super().__init__()
        logger.service_init(service)
        logger.log(service, 'Creating connection')
        conn = psycopg2.connect(dbname=config.NAME, user=config.USER,
                                password=config.PASSWORD, host=config.HOST)
        logger.log(service, 'Connection created')

        logger.log(service, 'Creating cursor')
        cursor = conn.cursor
        logger.log(service, 'Cursor created')