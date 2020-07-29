class Logger:

    def __init__(self):
        super().__init__()
        print ('[LOGGER] {LOGGER} started')

    def log(self, service, message):
        print('[' + service + '] ' + message)


    def service_init(self, service):
        print('[LOGGER] Service {' + service + '} initialized')