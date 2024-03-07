import datetime
import os
from typing import List


class Logger:
    file_name = f"logs/log_" + \
        str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def _write_log_to_file(cls, data: str):
        if not os.path.exists("logs"):
            os.makedirs("logs")
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)


    @classmethod
    def add_sql_result(cls, result: List[tuple]):
        data_to_add = f"\n-----\n"
        data_to_add += f"SQL result: {result}\n"
        data_to_add += "\n-----\n"
        cls._write_log_to_file(data_to_add)
