"""
@File    :   __main__.py
@Path    :   agrothon_client/
@Time    :   2021/05/28
@Author  :   Chandra Kiran Viswanath Balusu
@Version :   1.0.8
@Contact :   ckvbalusu@gmail.com
@Desc    :   Main Module for Agrothon
"""
from .utils import serial_sensor_in, pump_status, motion_intruder_detect
import multiprocessing
import sys
import logging

LOGGER = logging.getLogger(__name__)

def main():
    try:
        pool = multiprocessing.Pool()
        sen_result = pool.apply_async(serial_sensor_in)
        pump_result = pool.apply_async(pump_status)
        multiprocessing.Process(motion_intruder_detect(), daemon=True).start()
        sen_result.wait()
        pump_result.wait()
    except KeyboardInterrupt:
        LOGGER.info("Keyboard interrupt given, exiting ...")
    finally:
        LOGGER.info("Exiting Program")
        sys.exit(0)

if __name__ == '__main__':
    main()