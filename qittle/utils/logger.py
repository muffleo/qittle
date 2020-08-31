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
    format="<level><yellow>Qittle</yellow> | {message}</level> (<magenta>{time:HH:MM:ss}</magenta>)",
    filter=LoggerLevel("INFO"),
    level=0,
    enqueue=False,
)
logger.level("INFO", color="<white>")
logger.level("ERROR", color="<red>")
logger.level("SUCCESS", color="<green>")
