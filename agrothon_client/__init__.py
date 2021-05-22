import argparse
import logging
from logging.handlers import RotatingFileHandler
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("Agrothon.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

LOGGER = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
LOGGER.info("Parsing args")
parser.add_argument("-y", "--hostname", help="API Server host name")
parser.add_argument("-a", "--apikey", help="API Key of host")
parser.add_argument("-u", "--usb", help="USB Port of Arduino")

args = parser.parse_args()


USB_PORT = args.usb
SERVER_API_KEY = args.apikey
HOST = args.hostname

if USB_PORT is not None and SERVER_API_KEY is not None and HOST is not None:
    pass
else:
    LOGGER.info("Args Not Given, try Giving -h for more info")
    exit(1)


