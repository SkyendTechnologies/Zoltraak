import logging
import sys
import builtins
from datetime import datetime

class CustomFormatter(logging.Formatter):
    def format(self, record):
        line_number = record.lineno if record.lineno else "NA"
        file_name = record.pathname.split('/')[-1] if record.pathname else "Undefined"

        log_message = (
            f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]} "
            f"{record.levelname[0]} {file_name}:{line_number} {record.getMessage()}"
        )
        return log_message

def init_logger(log_level=logging.INFO):
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(CustomFormatter())

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(handler)

    # Redirect print to logging
    def print_to_log(*args, sep=" ", end="\n", file=None, flush=False):
        message = sep.join(map(str, args)) + end
        if file is None or file == sys.stdout:
            logging.info(message.strip())  # Логируем сообщение
        else:
            original_print(*args, sep=sep, end=end, file=file, flush=flush)  # Если file задан, вызываем оригинальный print

    original_print = builtins.print  # Сохраняем оригинальную функцию print
    builtins.print = print_to_log  # Переназначаем print

# # Example usage
# if __name__ == "__main__":
#     init_logger(logging.DEBUG)
#
#     print("This is a test message.")
#     logging.debug("Debugging information.")
#     logging.warning("This is a warning.")
#     print("Message with", "multiple arguments", sep=", ", end="!", flush=True)
