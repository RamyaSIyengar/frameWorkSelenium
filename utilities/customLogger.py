import logging
import os

print(os.curdir)

class LogGen:
    @staticmethod
    def loggen():
        log_file = os.path.abspath(os.curdir) + "//logs//Registration.log"
        print(f"Log file path: {log_file}")
        logging.basicConfig(filename=log_file,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

# Warn>Debug>info>error>fatal
