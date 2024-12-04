from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser


class LLMHandler:
    def __init__(self):
        llm = Ollama(model="llama2")
        output_parser = StrOutputParser()
        prompt = ChatPromptTemplate.from_messages([
            ("system",  'Translate my input from German to Russian. '
                'And explain the meaning of words in Russian.'),
                ("user", "{input}")])
        self._chain = prompt | llm | output_parser

    def ask(self, text):
        resp = self._chain.invoke({"input": text})
        return resp

