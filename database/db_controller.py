import psycopg2
import time
from . import db_config as config

class Controller:
    service = 'DB'
    logger = ''
    conn = ''

    def __init__(self, logger):
        super().__init__()
        self.logger = logger
        self.logger.service_init(self.service)
        self.logger.log(self.service, 'Creating connection')
        self.conn = psycopg2.connect(dbname=config.NAME, user=config.USER,
                                password=config.PASSWORD, host=config.HOST)
        self.logger.log(self.service, 'Connection created')

        self.logger.log(self.service, 'Searching for tables...')
        start_time = time.time()
        users_table = True
        users_result = 'found'
        guilds_table = True
        guilds_result = 'found'
        cursor = self.conn.cursor()
        try:
            cursor.execute('SELECT * FROM information_schema.tables WHERE table_name=\'%s\''%('users'))
            if cursor.fetchone() is None:
                users_table = False
                users_result = 'not found'
        except psycopg2.Error as e:
            users_table = False
            users_result = 'not found'
            cursor.execute('ROLLBACK')
        try:
            cursor.execute('SELECT * FROM information_schema.tables WHERE table_name=\'%s\''%('guilds'))
            if cursor.fetchone() is None:
                guilds_table = False
                guilds_result = 'not found'
        except psycopg2.Error as e:
            guilds_table = False
            guilds_result = 'not found'
            cursor.execute('ROLLBACK')
        cursor.close()
        self.conn.commit()
        self.logger.log(self.service, 'Table users %s, table guilds %s. Time of completion: %sms'%(users_result,
                                                                                                 guilds_result,
                                                                                                 str(int((time.time() - start_time) * 1000))))
        if not users_table or not guilds_table:
            self.logger.log(self.service, 'Creating not existing tables...')
            start_time = time.time()
            if not users_table:
                cursor = self.conn.cursor()
                cursor.execute('''CREATE TABLE users(
                                            id serial PRIMARY KEY,
                                            user_id integer NOT NULL,
                                            language text,
                                            battle_status text,
                                            bot_status text,
                                            role text,
                                            guild_in_id integer
                                        );''')
                cursor.close()
                self.conn.commit()
            if not guilds_table:
                cursor = self.conn.cursor()
                cursor.execute('''CREATE TABLE guilds(
                                            id serial PRIMARY KEY,
                                            chat_id integer,
                                            guild_name text,
                                            guild_admin integer,
                                            ping_time text
                                        );''')
                cursor.close()
                self.conn.commit()
            result = ''
            if not users_table and guilds_table:
                result = 'users, guilds'
            elif not users_table:
                result = 'users'
            else:
                result = 'guilds'
            self.logger.log(self.service, 
                            'Tables {%s} created in %sms'%(
                                result,
                                str(int((time.time() - start_time) * 1000))
                            ))
    

    def create_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
        data = cursor.fetchone()
        if data is None:
            cursor.execute('INSERT INTO users(user_id) VALUES(%s)', (user_id,))
            self.logger.log(self.service, 'User with id {%s} successfully created'%(user_id))
        else:
            self.logger.log(self.service, 'User with id {%s} already exists, nothing happend'%(user_id))
        cursor.close()
        self.conn.commit()
    

    def set_language(self, user_id, language):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE users SET language=\'%s\' WHERE user_id=%s'%(language, user_id,))
        self.logger.log(self.service, 'Language updated in db for user %s to %s language'%(user_id, language))
        cursor.close()
        self.conn.commit()