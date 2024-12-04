import sys
import logging
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QScrollArea, QTextEdit, QVBoxLayout,
    QPushButton, QHBoxLayout)
from PySide6.QtGui import QFont


from reader.utils import (
    get_book_path, get_translator, parse_config_for_ui)
from reader.workers.translation_worker import TranslationWorker
from reader.workers.llm_worker import LLMWorker
from reader.utils.llm_handler import LLMHandler
from reader.utils.epub_reader import read_epub


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('/tmp/book_reader.log')])

logger = logging.getLogger()


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.label = QLabel("Processed text will appear here")
        self.layout.addWidget(self.label)

    def set_text(self, text):
        self.label.setText(text)


class MainWindow(QMainWindow):
    def __init__(self, content, translator, llm_handler, font):
        """
        content (string) - content of the book
        translator (translator.Translator) - a class used for translating
        llm_handler (llm_handler. LLMHandler) - a class to communicate with llm
        font (QtGui.QFont)
        """
        super().__init__()
        self.content = content
        self.translator = translator
        self.llm_handler = llm_handler
        self.llm_worker = None

        # Set up the main widget and layout
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        # left half of the window
        left_layout = QVBoxLayout()
        left_bottom_layout = QHBoxLayout()
        main_scroll_area = QScrollArea()
        self.main_text_edit = QTextEdit()
        self.main_text_edit.setText(self.content)
        self.main_text_edit.setFont(font)
        main_scroll_area.setProperty("selectByMouse", True)
        main_scroll_area.setWidget(self.main_text_edit)
        main_scroll_area.setWidgetResizable(True)

        # right half of the window
        right_layout = QVBoxLayout()
        r_top_scroll_area = QScrollArea()
        self.r_top_text_edit = QTextEdit()
        self.r_top_text_edit.setFont(font)
        # r_top_scroll_area.setProperty("selectByMouse", False)
        r_top_scroll_area.setWidget(self.r_top_text_edit)
        r_top_scroll_area.setWidgetResizable(True)

        r_bottom_scroll_area = QScrollArea()
        self.r_bottom_text_edit = QTextEdit()
        self.r_bottom_text_edit.setFont(font)
        # l_top_scroll_area.setProperty("selectByMouse", False)
        r_bottom_scroll_area.setWidget(self.r_bottom_text_edit)
        r_bottom_scroll_area.setWidgetResizable(True)

        # Create a button
        self.btn_translate = QPushButton("Translate")
        self.btn_translate.clicked.connect(self.on_btn_translate_clicked)

        self.btn_ai = QPushButton("Ask AI")
        self.btn_ai.clicked.connect(self.on_btn_llm_clicked)

        # Add widgets to the layout
        right_layout.addWidget(r_top_scroll_area)
        right_layout.addWidget(r_bottom_scroll_area)
       
        left_layout.addWidget(main_scroll_area, 1)
        left_bottom_layout.addWidget(
            self.btn_translate)
        left_bottom_layout.addWidget(
            self.btn_ai)
        left_layout.addLayout(left_bottom_layout)
        # , alignment=Qt.AlignBottom
        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(right_layout, 1)

        # Set the main widget as the central widget of the QMainWindow
        self.setCentralWidget(main_widget)
        self.resize(1200, 800)  # Width: 1200 pixels, Height: 800 pixels

    def on_btn_translate_clicked(self):
        logger.info("Btn translate clicked")
        selected_text = self.main_text_edit.textCursor().selectedText()
        logger.info(f"Selected text: {selected_text}")
        if selected_text:
            self.translation_worker = TranslationWorker(
                selected_text, self.translator)
            self.translation_worker.result_ready.connect(
                self.handle_translation_result)
            logger.info(f"Start translation worker")
            self.translation_worker.start()

    def handle_translation_result(self, result):
        logger.info(f"Handle translation result: {result}")
        self.r_top_text_edit.setText(result)

    def on_btn_llm_clicked(self):
        logger.info("Btn llm clicked")
        selected_text = self.main_text_edit.textCursor().selectedText()
        logger.info(f"Selected text: {selected_text}")
        if selected_text:
            # if self.llm_worker and self.llm_worker.isRunning():
            if self.llm_worker:
                logger.info("LLM Worker exists")
                logger.info("LLM Worker quit")
                self.llm_worker.quit()
                logger.info("LLM Worker will wait")
                # self.llm_worker.wait()
                # logger.info("LLM Worker wait done")
            self.llm_worker = LLMWorker(
                selected_text, self.llm_handler)
            self.llm_worker.result_ready.connect(
                self.handle_llm_result)
            logger.info(f"Start llm worker")
            self.llm_worker.start()

    def handle_llm_result(self, result):
        logger.info(f"Handle llm result: {result}")
        self.r_bottom_text_edit.setText(result)


def main():
    translator = get_translator()
    book_path = get_book_path()
    content = read_epub(book_path)
    font_size = parse_config_for_ui()

    font = QFont()
    font.setPointSize(font_size)

    llm_handler = LLMHandler()

    app = QApplication([])
    window = MainWindow(content, translator, llm_handler, font)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
