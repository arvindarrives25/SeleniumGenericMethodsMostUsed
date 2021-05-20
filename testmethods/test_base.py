import inspect
import logging
import pytest


@pytest.mark.usefixtures("init_driver")
class TestBase:

    @staticmethod
    def get_logger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('Logs\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
