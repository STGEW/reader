import requests
import logging


logger = logging.getLogger()


class TranslationException(Exception):
    pass


class Translator:

    def __init__(
            self, url, port, alternatives,
            orig_lang, target_lang):
        self._url = url
        self._port = port
        self._alternatives = alternatives
        self._orig_lang = orig_lang
        self._target_lang = target_lang
    
    def translate(self, text):
        """
        raises exception TranslationException
        returns:
            {
                "alternatives":[list of strings],
                "translatedText":string
            }
        """
        resp = requests.request(
            method="post",
            url=f'http://{self._url}:{self._port}/translate',
            headers=None,
            json={
                'q': text,
                'source': self._orig_lang,
                'target': self._target_lang,
                'format': "text",
                'alternatives': self._alternatives
            })
        content = resp.content.decode()
        if resp.status_code != 200:
            err_msg = (
                "Error during text: '{text}' translation. "
                "Status code: '{resp.status_code}'."
                "Content: 'content'")
            logger.error(err_msg)
            raise TranslationException(err_msg)
        return content


def translate(text):
    resp = requests.request(
        method="post",
        url=f'http://{url}:{port}/translate',
        headers=None,
        json={
            'q': "Wie geht's?",
            'source': "de",
            'target': "ru",
            'format': "text",
            'alternatives': 3
        })