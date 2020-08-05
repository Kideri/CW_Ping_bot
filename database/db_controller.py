import psycopg2
import time
from . import db_config as config

class Controller:
    service = 'DB'
    logger = ''
    cursor = ''

    def __init__(self, logger):
        super().__init__()
        self.logger = logger
        self.logger.service_init(self.service)
        self.logger.log(self.service, 'Creating connection')
        conn = psycopg2.connect(dbname=config.NAME, user=config.USER,
                                password=config.PASSWORD, host=config.HOST)
        self.logger.log(self.service, 'Connection created')

        self.logger.log(self.service, 'Creating cursor')
        self.cursor = conn.cursor()
        self.logger.log(self.service, 'Cursor created')

        self.logger.log(self.service, 'Searching for tables...')
        start_time = time.time()
        users_table = True
        guilds_table = True
        result = self.cursor.execute('SELECT name FROM information_schema.tables WHERE table_name=%s'%('users'))
        if result.getCount() == 0:
            users_table = False
        result = self.cursor.execute('SELECT name FROM information_schema.tables WHERE table_name=%s'%('guilds'))
        if result.getCount() == 0:
            guilds_table = False
        self.logger.log(self.service, 'Table users %s, table guilds %s. Time of completion: %s'%((users_table if 'found' else 'not found'),
                                                                                                 (guilds_table if 'found' else 'not found'),
                                                                                                 str(int((time.time() - start_time) * 1000))))
        if not users_table or not guilds_table:
            self.logger.log(self.service, 'Creating not existing tables...')
            start_time = time.time()
            if not users_table:
                self.cursor.execute('''CREATE TABLE users(
                                            id integer PRIMARY KEY,
                                            user_id integer NOT NULL,
                                            language text,
                                            battle_status text,
                                            bot_status text,
                                            role text,
                                            guild_in_id integer
                                        );''')
            if not guilds_table:
                self.cursor.execute('''CREATE TABLE guilds(
                                            id integer PRIMARY KEY,
                                            chat_id integer,
                                            guild_name text,
                                            guild_admin integer,
                                            ping_time text
                                        );''')
            self.logger.log(self.service, 
                            'Tables {%s} created in %s'%(
                                not users_table and not guilds_table if 'users, guilds'
                                else not users_table if 'users'
                                else 'guilds',
                                str(int((time.time() - start_time) * 1000))
                            ))
    

    def create_user(self, user_id):
        self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        data = self.cursor.fetchone()
        if data is None:
            cursor.execute('ISERT INTO users VALUES(?)', (user_id,))
            self.logger(self.service, 'User with id {%s} successfully created'%(user_id))
        else:
            self.logger(self.service, 'User with id {%s} already exists, nothing happend'%(user_id))
    

    def set_language(self, user_id, language):
        cursor.execute('UPDATE users SET language=\'%s\' WHERE user_id=%s'%(language, user_id,))
        self.logger.log(self.service, 'Language updated in db for user %s to %s language'%(user_id, language))