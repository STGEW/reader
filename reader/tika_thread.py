import subprocess
import time
import logging

from pathlib import Path


logger = logging.getLogger()

exe_path = Path(__file__).resolve().parent.parent.joinpath(
    'bin', 'tika-server-standard-2.9.2.jar')
proc_args = ['java', '-jar', exe_path]


if __name__ == "__main__":
    logger.info("Starting the process")
    process = subprocess.Popen(proc_args)
    logger.info("The process is started")
    while True:
        if process.poll() is not None:
            logger.info("Process died, restarting...")
            process = subprocess.Popen(proc_args)
        time.sleep(1)

