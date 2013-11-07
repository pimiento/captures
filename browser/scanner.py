import time
import logging
from imagescanner import ImageScanner, settings
from imagescanner.utils.logger import config_logger
settings.LOGGING_LEVEL = logging.DEBUG
config_logger()

def take_scan():
    # waiting for initialize scannig for good
    time.sleep(3)
    iscanner = ImageScanner()
    scanners = iscanner.list_scanners()
    scanner = scanners[0]
    return scanner.scan().read()
