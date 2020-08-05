import ru, en

class Worker:
    service = 'WORKER'
    logger = ''
    controller = ''

    def __init__(self, logger, controller):
        self.logger = logger
        self.logger.service_init(self.service)
        self.controller = controller
    

    def set_local_ru(self, user_id):
        self.controller.set_language(user_id, 'ru')
        return ru.language_set


    def set_local_en(self, user_id):
        self.controller.set_language(user_id, 'en')
        return en.language_set


    global_command_list = {
        '🇷🇺 Русский': set_local_ru,
        '🇺🇸 English': set_local_en,
    }
    status_change_command_list = ''