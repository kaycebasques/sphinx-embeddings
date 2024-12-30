from abc import ABC, abstractmethod
import hashlib
import json
import random

import google.generativeai as gemini
# import voyageai


class Model(ABC):

    @abstractmethod
    def configure(self, api_key):
        pass

    @abstractmethod
    def embed(self, text, model, task_type):
        pass


class Gemini(Model):

    def configure(self, api_key):
        self.api_key = api_key
        gemini.configure(api_key=api_key)

    def embed(self, text, model, task_type):
        try:
            response = gemini.embed_content(model=model, content=text, task_type=task_type)
            return response['embedding'] if 'embedding' in response else None
        except Exception as e:
            return None


class Voyage(Model):

    def configure(self, api_key):
        self.api_key = api_key
        # voyage = voyageai.Client(api_key=api_key)

    def embed(self, text, model, task_type):
        return [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]
        # try:
        #     embedding = voyage.embed([text], model='voyage-3', input_type='document').embeddings[0]
        #     return embedding
        # except Exception as e:
        #     return None
