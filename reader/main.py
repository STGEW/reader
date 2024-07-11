import time
import tika
from tika import parser
import yaml
from pathlib import Path
import logging


from translator import Translator, TranslationException


logger = logging.getLogger()

def get_config():
    conf_path = Path(__file__).resolve().parent.parent.joinpath(
        'config').joinpath('config.yml')
    with open(conf_path, 'r') as file:
        conf = yaml.safe_load(file)
        return conf


def main():
    tika.initVM()

    config = get_config()
    book_path = config['debug']['book_path']

    url = config['libretranslate']['url']
    port = config['libretranslate']['port']
    alternatives = config['libretranslate']['alternatives']
    orig_lang = config['libretranslate']['orig_lang']
    target_lang = config['libretranslate']['target_lang']
    
    with open(book_path, 'rb') as file_obj:
        response = parser.from_file(file_obj)
        content_orig = response['content']
    
    t = Translator(
        url, port, alternatives,
        orig_lang, target_lang)
    
    text = 'Hallo'
    try:
        res = t.translate(text)
    except TranslationException as e:
        logger.exception(e)
    logger.info(res)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()])
    main()
