import ru, en

class Worker:
    service = 'Worker'
    logger = ''
    controller = ''

    def __init__(self, logger, controller):
        self.logger = logger
        self.logger.service_init(service)
        self.controller = controller
    

    def set_local_ru(self, user_id):
        self.controller.set_language(user_id, 'ru')
        return ru.language_set


    def set_local_en(self, user_id):
        self.controller.set_language(user_id, 'en')
        return en.language_set