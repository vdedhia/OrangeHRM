import logging


class Logger(object):

    def __init__(self):
        self.FORMAT = '%(asctime)s - %(levelname)s: %(message)s'
        self.format = logging.basicConfig(filename=None, level=logging.INFO, format=self.FORMAT)

    @staticmethod
    def logger(level, *msg) -> object:
        """
        :param level: logs level - string - can be: 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'
        :param msg: your logs
        """
        level = level.upper()
        if level == 'INFO':
            logging.info(msg)
        elif level == 'DEBUG':
            logging.debug(msg)
        elif level == 'WARNING':
            logging.warning(msg)
        elif level == 'ERROR':
            logging.error(msg)
        elif level == 'CRITICAL':
            logging.critical(msg)
        else:
            raise ValueError('Unknown log level %s, available: INFO, WARNING, DEBUG, ERROR, CRITICAL' % msg)

    def log_request(self, method, url, data=None, headers=None, json=None, params=None, cert=None):
        self.logger('INFO', 'Sending {} request to {}'.format(method, url))
        if data:
            self.logger('INFO', '{} request with data {}'.format(method, data))
        if headers:
            self.logger('INFO', '{} request with headers {}'.format(method, headers))
        if json:
            self.logger('INFO', '{} request with json {}'.format(method, json))
        if params:
            self.logger('INFO', '{} request with params {}'.format(method, params))
        if cert:
            self.logger('INFO', '{} request with cert {}'.format(method, cert))

    def log_response(self, response):
        self.logger('INFO', 'Received response: {} \nwith code {}'.format(response.text, response.status_code))
