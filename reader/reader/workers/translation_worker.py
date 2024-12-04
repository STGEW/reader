from PySide6.QtCore import QThread, Signal
import logging


from reader.utils.translator import TranslationException


logger = logging.getLogger()


class TranslationWorker(QThread):
    result_ready = Signal(str)

    def __init__(self, text, translator):
        """
        text (str) - text for processing
        translator (translator.Translator) - a class to translate everything
        """
        super().__init__()
        self.translator = translator
        self.text = text
        logger.info(f"Create obj TranslationWorker for text: {text}")

    def run(self):
        processed_text = self.process_text(self.text)
        self.result_ready.emit(processed_text)

    def process_text(self, text):
        logger.info(f"Process text: {text}")
        try:
            resp = self.translator.translate(text)
            logger.info(f"Responce from translator: {resp}")
            translated_text = resp["translatedText"]
            alternatives = resp["alternatives"]
            alternatives = [f"'{i}'" for i in alternatives]
            alternatives = ", ".join(alternatives)
            res_msg = (
                f"Requested a translation for original text: '{text}'. "
                f"Translation is: '{translated_text}'. "
                f"Alternatives are: {alternatives}."
                )
            logger.info(f"resp message: {res_msg}")
            return res_msg
        except TranslationException as e:
            logger.exception(e)
            return e

