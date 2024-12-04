from PySide6.QtCore import QThread, Signal
import logging


logger = logging.getLogger()


class LLMWorker(QThread):
    result_ready = Signal(str)

    def __init__(self, text, llm_handler):
        """
        text (str) - text for processing
        llm_handler (llm_handler.LLMHandler) - a class to request a LLM to do something
        """
        super().__init__()
        self.llm_handler = llm_handler
        self.text = text
        logger.info(f"Create obj LLMWorker for text: {text}")

    def run(self):
        processed_text = self.process_text(self.text)
        self.result_ready.emit(processed_text)

    def process_text(self, text):
        logger.info(f"Process text: {text}")
        resp = self.llm_handler.ask(text)
        logger.info(f"Resp is: {resp}")
        return resp

