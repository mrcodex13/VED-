# from src.logger import logging 

# logging.info("Starting the demo.py script as info...")
# logging.debug("Starting the demo.py script as debug...")
# logging.warning("Starting the demo.py script as warning...")
# logging.error("Starting the demo.py script as error...")
# logging.critical("Starting the demo.py script as critical...")
# logging.info("Demo.py script completed successfully.")



from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1 + 10
    logging.debug(a)

except Exception as e:
    logging.debug(e)
    raise MyException(e, sys) from e