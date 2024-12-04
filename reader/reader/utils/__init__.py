import yaml
from pathlib import Path
import logging


from reader.utils.translator import Translator


logger = logging.getLogger()


def get_config():
    conf_path = Path(__file__).resolve().parent.parent.parent.parent.joinpath(
        'config').joinpath('config.yml')
    with open(conf_path, 'r') as file:
        conf = yaml.safe_load(file)
        return conf


def parse_config_for_translator():
    config = get_config()

    url = config['libretranslate']['url']
    port = config['libretranslate']['port']
    alternatives = config['libretranslate']['alternatives']
    orig_lang = config['libretranslate']['orig_lang']
    target_lang = config['libretranslate']['target_lang']

    return url, port, alternatives, orig_lang, target_lang


def parse_config_for_ui():
    config = get_config()
    ui_config = config['ui']
    return ui_config['font_size']


def get_translator():
    args = parse_config_for_translator()
    t = Translator(
        *args)
    return t


def get_book_path():
    config = get_config()
    book_path = config['debug']['book_path']
    return book_path


