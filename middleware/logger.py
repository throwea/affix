

import os
import sys
import traceback
from inspect import getframeinfo, stack

#TODO: log to db is not defined 
#TODO: logger should be initialized as an app dependency

from loguru import logger as loguru_logger

# modify loguru default log formatting
loguru_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | {message}"
loguru_logger.remove()
loguru_logger.add(sys.stderr, format=loguru_format)

# gets the filename, method, and line# of the context
def get_caller_info(stack_level=2):
    """
    Retrieves caller information from the stack.

    Args:
        stack_level: The stack level to inspect.

    Returns:
        Tuple containing filename, function name, and line number.
    """
    caller = getframeinfo(stack()[stack_level][0])
    return caller.filename, caller.function, caller.lineno


# annotates filename, method, and line# for log calls
def get_annotated_message(msg):
    """
    Annotates a message with the filename, method name, and line number of the caller.

    Args:
        msg: The original message.

    Returns:
        The annotated message.
    """
    name, func, line = get_caller_info(3)
    msg = f"{name}:{func}:{line} - {msg}"
    return msg

class Logger:
    """
    Logger class for piping logs to stdout and database.

    This class provides methods for various log levels and handles both printing
    logs to stdout and recording them in the database.
    """

    def __init__(self) -> None:
        pass

    def debug(self, msg: str):
        """
        Logs a debug message.

        Args:
            msg: The message to log.
            test_log: Flag to indicate if this is a test log.
        """
        annotated_msg = get_annotated_message(msg)
        loguru_logger.debug(annotated_msg)
        # log_to_db(annotated_msg, 'debug')

    def info(self, msg: str):
        """
        Logs an info message.

        Args:
            msg: The message to log.
        """
        annotated_msg = get_annotated_message(msg)
        loguru_logger.info(annotated_msg)
        log_to_db(annotated_msg, "info")

    def warn(self, msg: str):
        """
        Logs a warning message.

        Args:
            msg: The message to log.
        """
        annotated_msg = get_annotated_message(msg)
        loguru_logger.warning(annotated_msg)
        log_to_db(annotated_msg, "warn")

    def warning(self, msg: str):
        """
        Logs a warning message.

        Args:
            msg: The message to log.
        """
        self.warn(msg)

    def error(self, msg: str):
        """
        Logs an error message.

        Args:
            msg: The message to log.
        """
        annotated_msg = get_annotated_message(msg)
        loguru_logger.error(annotated_msg)
        log_to_db(annotated_msg, "error")

    def exception(self, msg: str):
        """
        Logs an exception message.

        Args:
            msg: The message to log.
        """
        annotated_msg = get_annotated_message(msg)
        loguru_logger.error(annotated_msg)
        traceback_str = traceback.format_exc()
        log_to_db(annotated_msg, "error", traceback_str)


logger = Logger()
