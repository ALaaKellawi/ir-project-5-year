from sklearn.metrics.pairwise import cosine_similarity

from services.SaveAndLoaFile import SaveAndLoadFileService


def query_matching(query: str, selectedDataset):
    print(query)
    print(selectedDataset)
    if selectedDataset == "qoura":
        loadQouraVictorizer = SaveAndLoadFileService.load_vectorizer(
            "C:\\Users\\Ghost\\Desktop\\pickleFiles\\vectorizer.pkl")
        loadQouratfidf_matrix = SaveAndLoadFileService.load_vectorizer(
            "C:\\Users\\Ghost\\Desktop\\pickleFiles\\tfidf_matrix.pkl")
        lodedQouraDocName = SaveAndLoadFileService.load_document_names(
            "C:\\Users\\Ghost\\Desktop\\pickleFiles\\document_names.pkl")
        query_tfidf = loadQouraVictorizer.transform([query])
        similarity = cosine_similarity(query_tfidf, loadQouratfidf_matrix).flatten()
        matching_results = []
        for i, doc_name in enumerate(lodedQouraDocName):
            if similarity[i] > 0:
                matching_results.append((doc_name, similarity[i]))
        sorted_results = sorted(matching_results, key=lambda x: x[1], reverse=True)
        print('**************************')
        print(query_tfidf)
        # print(loadQouratfidf_matrix)
        print(sorted_results)



    if selectedDataset == "lifestyle":
        loadLifeStyleVictorizer = SaveAndLoadFileService.load_vectorizer(
            "C:\\Users\\Ghost\\Desktop\\pickleFiles\\vectorizerDataset2New.pkl")
        loadLifeStyletfidf_matrix = SaveAndLoadFileService.load_vectorizer(
            "C:\\Users\\Ghost\\Desktop\\pickleFiles\\tfidf_matrixDataset2New.pkl")
        lodedLifeStyleDocName = SaveAndLoadFileService.load_document_names(
            "C:\\Users\\Ghost\\Desktop\\pickleFiles\\document_namesDataset2New.pkl")
        query_tfidf = loadLifeStyleVictorizer.transform([query])
        similarity = cosine_similarity(query_tfidf, loadLifeStyletfidf_matrix).flatten()
        matching_results = []
        for i, doc_name in enumerate(lodedLifeStyleDocName):
            if similarity[i] > 0:
                matching_results.append((doc_name, similarity[i]))
        sorted_results = sorted(matching_results, key=lambda x: x[1], reverse=True)
    return sorted_results[:20]
