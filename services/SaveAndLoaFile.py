import pickle

import pandas as pd


class SaveAndLoadFileService:
    @staticmethod
    def read_documents_from_one_file(filePath):
        df2 = pd.read_csv(filePath)
        documents2 = df2['title'].fillna('', inplace=False).tolist()
        document_names2 = df2['Unnamed: 0'].tolist()
        return documents2, document_names2

    @staticmethod
    def save_vectorizer(vectorizer, path):
        with open(path, "wb") as f:
            pickle.dump(vectorizer, f)

    @staticmethod
    def save_tfidf_matrix(tfidf_matrix, path):
        with open(path, "wb") as f:
            pickle.dump(tfidf_matrix, f)

    @staticmethod
    def save_document_names(document_names, path):
        with open(path, "wb") as f:
            pickle.dump(document_names, f)

    @staticmethod
    def load_vectorizer(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @staticmethod
    def load_tfidf_matrix(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    @staticmethod
    def load_document_names(path):
        with open(path, "rb") as f:
            return pickle.load(f)
