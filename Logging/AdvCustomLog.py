import logging


class Log:
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A', level=logging.DEBUG, filename="AdvanceLogs.log", filemode="a")
    def write_info_to_log(self, msg):
        self.msg = msg
        loggerInfo = logging.getLogger()
        loggerInfo.info(self.msg)

    def write_error_to_log(self, msg):
        self.msg = msg
        loggerError = logging.getLogger()
        loggerError.error(self.msg)