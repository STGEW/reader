import subprocess
import time
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('/tmp/translate_thread.log')])


logger = logging.getLogger()

proc_args = ['libretranslate', '--port', '3862']


def main():
    logger.info("Starting the process")
    process = subprocess.Popen(proc_args)
    logger.info("The process is started")
    while True:
        if process.poll() is not None:
            logger.info("Process died, restarting...")
            process = subprocess.Popen(proc_args)
        time.sleep(1)

if __name__ == "__main__":
    main()
