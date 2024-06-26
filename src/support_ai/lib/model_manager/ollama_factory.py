from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from ..const import CONFIG_MODEL
from .model_factory import ModelFactory


class OllamaFactory(ModelFactory):
    def __init__(self, config):
        self.model = config[CONFIG_MODEL]
        if not self.model:
            raise ValueError(f'Missing {CONFIG_MODEL} in llm config')

    def create_llm(self):
        return ChatOllama(model=self.model)

    def create_embeddings(self):
        return OllamaEmbeddings(model=self.model)
