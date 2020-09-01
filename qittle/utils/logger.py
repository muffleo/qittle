import sys

from loguru import logger


class LoggerLevel:
    def __init__(self, level):
        self.level = level

    def __call__(self, record):
        level_no = logger.level(self.level).no
        return record["level"].no >= level_no


logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    format="<level><magenta>Qittle</magenta> | {message}</level> (<blue>{time:HH:MM:ss}</blue>)",
    filter=LoggerLevel("INFO"),
    level=0,
    enqueue=False,
)
logger.level("INFO", color="<white>")
logger.level("SUCCESS", color="<green>")
logger.level("WARNING", color="<yellow>")
logger.level("ERROR", color="<red>")


