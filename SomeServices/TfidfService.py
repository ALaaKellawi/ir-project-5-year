from sklearn.feature_extraction.text import TfidfVectorizer

from SomeServices import SaveAndLoaFileService


class TfidfService:
    def create_tfidf(self, filePath, vectorPath, tfidfPath, saveDocName):
        documents2, document_names2 = SaveAndLoaFileService.read_documents_from_one_file(filePath)
        vectorizer = TfidfVectorizer()
        print("Vectoriser Created.")
        tfidf_matrix = vectorizer.fit_transform(documents2)
        print("TF-IDF Created.")
        feature_names = vectorizer.get_feature_names_out()
        SaveAndLoaFileService.save_vectorizer(vectorizer, vectorPath)
        SaveAndLoaFileService.save_tfidf_matrix(tfidf_matrix, tfidfPath)
        SaveAndLoaFileService.save_document_names(document_names2, saveDocName)
