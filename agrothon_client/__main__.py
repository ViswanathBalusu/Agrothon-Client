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
import os
import logging

LOGGER = logging.getLogger(__name__)

def main():
    try:
        pool = multiprocessing.Pool()
        sen_result = pool.apply_async(serial_sensor_in)
        pump_result = pool.apply_async(pump_status)
        intruder_checker = multiprocessing.Process(motion_intruder_detect(), daemon=True)
        intruder_checker.start()
        sen_result.wait()
        pump_result.wait()
    except (KeyboardInterrupt,  SystemExit):
        LOGGER.info("Keyboard interrupt given, exiting ...")
        pool.terminate()
        # pool.join()
        intruder_checker.join()
    # finally:
    #     LOGGER.info("Exiting Program")
    #     os._exit(0)

if __name__ == '__main__':
    main()