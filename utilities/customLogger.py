import logging
import os

print(os.curdir)


class LogGen:

    @staticmethod
    def loggen():
        log_file = "./logs/Registration.log"
        print(log_file)
        print(f"Log file path: {log_file}")
        logging.basicConfig(filename=log_file,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logging.info("from customLogger")
        return logger

# Warn>Debug>info>error>fatal
