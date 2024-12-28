from abc import ABC, abstractmethod
import hashlib
import json
import random

# import google.generativeai as gemini
# import voyageai

def write(out_dir, doc_name, text, embedding):
    md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
    data = {
        'doc_name': doc_name,
        'text': text,
        'md5': md5,
        'embedding': embedding
    }
    path = f'{out_dir}/{md5}.json'
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


class Model(ABC):

    @abstractmethod
    def configure(self, out_dir, api_key):
        pass

    @abstractmethod
    def embed(self, text):
        pass


class Gemini(Model):

    def configure(self, out_dir, api_key):
        self.out_dir = out_dir
        self.api_key = api_key
        # gemini.configure(api_key=api_key)

    def embed(self, text, doc_name):
        embedding = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]
        write(self.out_dir, doc_name, text, embedding)
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

    def configure(self, out_dir, api_key):
        self.out_dir = out_dir
        self.api_key = api_key
        # voyage = voyageai.Client(api_key=api_key)

    def embed(self, text, doc_name):
        embedding = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]
        write(self.out_dir, doc_name, text, embedding)
        # try:
        #     embedding = voyage.embed([text], model='voyage-3', input_type='document').embeddings[0]
        #     return embedding
        # except Exception as e:
        #     return None
