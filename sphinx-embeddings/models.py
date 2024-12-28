from abc import ABC, abstractmethod
import hashlib
import json
import random

import google.generativeai as gemini
# import voyageai

def write(out_dir, doc_name, text, embedding):
    md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
    # TODO: Save task type and model name
    data = {
        'doc_name': doc_name,
        'text': text,
        'md5': md5,
        # TODO: Use model name as key (so that you can store outputs from many models)
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
        gemini.configure(api_key=api_key)

    def embed(self, text, doc_name):
        try:
            response = gemini.embed_content(
                # TODO: Accept the user-provided model name
                model='models/text-embedding-004',
                content=text,
                # TODO: Make this configurable
                task_type='SEMANTIC_SIMILARITY'
            )
            embedding = response['embedding'] if 'embedding' in response else None
        except Exception as e:
            embedding = None
        write(self.out_dir, doc_name, text, embedding)


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
