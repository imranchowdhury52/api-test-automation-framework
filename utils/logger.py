import logging

LOG_NAME = "api"


def get_logger():
    return logging.getLogger(LOG_NAME)
