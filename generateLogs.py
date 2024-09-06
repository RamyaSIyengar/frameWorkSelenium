import logging

logging.basicConfig(filename=".\\logs\\log1.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

log = logging.getLogger()
log.setLevel('DEBUG')
log.info("first log")
log.debug("this is a new one")