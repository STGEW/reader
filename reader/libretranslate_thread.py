import subprocess
import time
import logging


logger = logging.getLogger()

proc_args = ['libretranslate', '--port', '3862']


if __name__ == "__main__":
    logger.info("Starting the process")
    process = subprocess.Popen(proc_args)
    logger.info("The process is started")
    while True:
        if process.poll() is not None:
            logger.info("Process died, restarting...")
            process = subprocess.Popen(proc_args)
        time.sleep(1)

