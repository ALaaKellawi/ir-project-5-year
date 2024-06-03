
import difflib
import os



def tqueryRefinement(query,file_path):
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
