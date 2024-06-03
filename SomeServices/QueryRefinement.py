# import os
# from difflib import get_close_matches
#
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
#
# from loded_file import loded_file
#
# loaded_vectorizer = loded_file.load_vectorizer("C:\\Users\\LENOVO\\Desktop\\pickleFilesQuery\\1.pkl")
# loaded_tfidf_matrix = loded_file.load_tfidf_matrix("C:\\Users\\LENOVO\\Desktop\\pickleFilesQuery\\2.pkl")
# loaded_document_names = loded_file.load_document_names("C:\\Users\\LENOVO\\Desktop\\pickleFilesQuery\\3.pkl")
#
# doc = './query_IN_Files'
#
#
# def retrive_query(query: str, doc: str):
#     query = get_close_matches('futu', query.split())
#     print(query)
#     query_tfidf = loaded_vectorizer.transform([query])
#     query_vector = query_tfidf.toarray()[0]
#     similarity = cosine_similarity(query_vector.reshape(1, -1), loaded_tfidf_matrix).flatten()
#     sorted_indices = np.argsort(similarity)[::-1]  # عكس ترتيب المؤشرات للترتيب التنازلي
#     sorted_documents = [(loaded_document_names[i], similarity[i]) for i in sorted_indices if similarity[i] > 0]
#
#     retrieved_files = []
#     for document, _ in sorted_documents:
#         if document.endswith('.csv'):
#             file_path = os.path.join(doc, document)
#             with open(file_path, 'r') as file:
#                 content = file.read()
#                 document_name = os.path.splitext(document)[0]  # إزالة امتداد الملف
#                 retrieved_files.append((document_name, content))
#
#     return retrieved_files
#
#
# results = retrive_query('future', doc)
# for document, content in results:
#     print(f"Document: {document}")
#     print(f"Content: {content}\n")
import difflib
import os



def queryRefinement(query,file_path):
    suggestions_dict = {}  # قاموس لتخزين الاقتراحات وعدد مرات تكرارها
    list = []

    for filename in os.listdir(file_path):
        if filename.endswith('.csv'):
            input_file = os.path.join(file_path, filename)

            with open(input_file, 'r', encoding='utf-8') as infile:
                text = infile.read()
                query_capitalized = ' '.join(word.capitalize() for word in query.split())
                suggestions_phrase = difflib.get_close_matches(query_capitalized, [text])
                suggestions_words = difflib.get_close_matches(query_capitalized, text.split())

                if suggestions_phrase:
                    for suggestion in suggestions_phrase:
                        if suggestion in suggestions_dict:
                            suggestions_dict[suggestion].append(text)
                        else:
                            suggestions_dict[suggestion] = [text]

                if suggestions_words:
                        for suggestion in suggestions_words:
                            if suggestion in suggestions_dict:
                                suggestions_dict[suggestion].append(text)
                            else:
                                suggestions_dict[suggestion] = [text]
# def rrr(query):
#     suggestions_dict = {}  # Dictionary to store suggestions and their occurrences
#     list = []
#
#     with open(file_path, 'r', encoding='utf-8') as infile:
#         text = infile.read()
#         query_capitalized = ' '.join(word.capitalize() for word in query.split())
#         suggestions_phrase = difflib.get_close_matches(query_capitalized, [text])
#         suggestions_words = difflib.get_close_matches(query_capitalized, text.split())
#
#         if suggestions_phrase:
#             for suggestion in suggestions_phrase:
#                 if suggestion in suggestions_dict:
#                     suggestions_dict[suggestion].append(text)
#                 else:
#                     suggestions_dict[suggestion] = [text]
#
#         if suggestions_words:
#             for suggestion in suggestions_words:
#                 if suggestion in suggestions_dict:
#                     suggestions_dict[suggestion].append(text)
#                 else:
#                     suggestions_dict[suggestion] = [text]

    # رتب الاقتراحات حسب الأكثرية
    sorted_suggestions = sorted(suggestions_dict.items(), key=lambda x: len(x[1]), reverse=True)

    # قم بطباعة المحتوى للعناصر الأكثر تكرارًا في الوثائق
    count = 0
    for suggestion, texts in sorted_suggestions:
        if count >= 1:  # قف عند الخمسة الأكثر تكرارًا
            break
        print(f"Suggestion: {suggestion}")
        # print("Documents:")
        for text in texts:
            list.append(text)
            list.append('\n')
            # print(text)
        # for text in list:
        #     print(text)
        count += 1
        # print("------------")
    return list



# query = 'future'
# results = rrr('future','./query_IN_Files')
# for text in results:
#     print(f"Document: {text}")
