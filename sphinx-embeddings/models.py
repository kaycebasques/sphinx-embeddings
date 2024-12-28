from abc import ABC, abstractmethod

# import google.generativeai as gemini
# import voyageai


class Model(ABC):

    @abstractmethod
    def configure(self, api_key):
        pass

    @abstractmethod
    def embed(self, text):
        pass


class Gemini(Model):

    def configure(self, api_key=None):
        self.api_key = api_key
        # gemini.configure(api_key=api_key)

    def embed(self, text):
        return text[::-1]
        # try:
        #     response = gemini.embed_content(
        #         model='models/text-embedding-004',
        #         content=text,
        #         task_type='SEMANTIC_SIMILARITY'
        #     )
        #     return response['embedding'] if 'embedding' in response else None
        # except Exception as e:
        #     return None


class Voyage(Model):

    def configure(self, api_key=None):
        self.api_key = api_key
        # voyage = voyageai.Client(api_key=api_key)

    def embed(self, text):
        return text[::-1]
        # try:
        #     embedding = voyage.embed([text], model='voyage-3', input_type='document').embeddings[0]
        #     return embedding
        # except Exception as e:
        #     return None
