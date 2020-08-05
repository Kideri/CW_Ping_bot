from .worker import Worker

class Parser:
    service = 'Parser'
    logger = ''
    worker = ''


    def __init__(self, logger, worker):
        self.logger = logger
        self.logger.service_init(self.service)
        self.worker = worker
        self.logger.log(self.service, 'Command list initialized: ' + 
                                      len(self.worker.global_command_list) + ' global commands, ' + 
                                      len(self.worker.status_change_command_list) + ' status change commands')
        self.worker = worker
    

    def parse(self, user_id, text):
        if text in self.worker.global_comand_list:
            self.logger.log(self.service, 'User %s called global command: {%s}'%(user_id, text))
            return self.worker.global_command_list[text]()
        if text in self.worker.status_change_command_list:
            self.logger.log(self.service, 'User %s called status change command: {%s}'%(user_id, text))
            return self.worker.status_change_comand_list[text]()
        self.logger.log(self.service, 'User %s called unknown command: {%s}'%(user_id, text))
        return 'failed'