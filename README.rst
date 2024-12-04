About libretranslate:
https://github.com/LibreTranslate/LibreTranslate


About Ollama LLM
curl -fsSL https://ollama.com/install.sh | sh

To start ollama (8B parameters):
ollama pull llama2
ollama run llama2


Possible future task: database with verbs, nouns, etc
https://www.openthesaurus.de/about/download
sudo apt-get install mysql-server
sudo apt-get install libmysqlclient-dev
https://pypi.org/project/py-openthesaurus/ - all steps should be executed


TBD:
- Add progress for the book
- Exceptions, improve stability
- add information about two packages - 'translate server' and 'reader'


Exception example:
(venv_reader) afomin@afomin-unit:~/projects/mj/foreign_book_reader/reader$ reader
/home/afomin/projects/mj/venv_reader/lib/python3.10/site-packages/EbookLib-0.18-py3.10.egg/ebooklib/epub.py:1395: UserWarning: In the future version we will turn default option ignore_ncx to True.
/home/afomin/projects/mj/venv_reader/lib/python3.10/site-packages/EbookLib-0.18-py3.10.egg/ebooklib/epub.py:1423: FutureWarning: This search incorrectly ignores the root element, and will be fixed in a future version.  If you rely on the current behaviour, change it to './/xmlns:rootfile[@media-type]'
2024-07-10 10:28:02,520 - root - INFO - Btn llm clicked
2024-07-10 10:28:02,521 - root - INFO - Selected text: Mädchen
2024-07-10 10:28:02,521 - root - INFO - Create obj LLMWorker for text: Mädchen
2024-07-10 10:28:02,521 - root - INFO - Start llm worker
2024-07-10 10:28:02,522 - root - INFO - Process text: Mädchen
2024-07-10 10:28:04,607 - root - INFO - Btn llm clicked
2024-07-10 10:28:04,607 - root - INFO - Selected text: Offizierspuffs
2024-07-10 10:28:04,607 - root - INFO - Create obj LLMWorker for text: Offizierspuffs
2024-07-10 10:28:04,608 - root - INFO - Start llm worker
2024-07-10 10:28:04,608 - root - INFO - Process text: Offizierspuffs
2024-07-10 10:29:20,086 - root - INFO - Resp is: Sure, I'd be happy to help! "Mädchen" is the German word for "girl." In Russian, the equivalent word is "девушка" (devingushka).

Here are some possible translations of "Mädchen" in different contexts:

* "Mädchen" can be translated as "девушка" (devingushka) in a general sense. For example, "Sie ist eine schöne Mädchen" can be translated as "Она – прекрасная девушка." (Ona - prekrasnaya devushka.)
* In a more romantic or flirtatious context, "Mädchen" can be translated as "моя любовь" (moya lyubov). For example, "Er ist so schön und wie ein Mädchen" can be translated as "Он так прекрасен и похож на мою любовь." (On tak prekrasen i poshcheg k moej lyubvi.)
* In a more playful or teasing context, "Mädchen" can be translated as "моя кошка" (moya koshka). For example, "Sie ist so niedlich wie ein Mädchen" can be translated as "Она так привлекательна и похожа на мою кошку." (On tak priyvlekalnaya i poshcheg k moej koshke.)

I hope this helps! Let me know if you have any other questions.
QThread: Destroyed while thread is still running
Aborted (core dumped)

QThread: Destroyed while thread is still running
Aborted (core dumped)
