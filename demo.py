from visa.logger import logging
from visa.exception import USVisaException
import sys
try:
    a = 1/0
except Exception as e:
    logging.info("An error occurred")
    raise USVisaException(e, sys)