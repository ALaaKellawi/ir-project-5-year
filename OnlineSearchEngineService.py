import pandas as pd
from autocorrect import Speller
from flask import Flask, render_template, request
import requests

# from Four_match_method_with_10 import query_matching_top_10
# from loded_file import loded_file
# from match_Method import retrieve_files
from services.QueryRefinement import queryRefinement

# from textProccessing import TextProcessor

app = Flask(__name__)


# @app.route('/')
# def hello():
#     return 'Hello, World!'


@app.route('/')
def home():
    return render_template('/uiCore.html')

    # return jsonify({'processed_text': ' '.join(text_processing_service)})


@app.route('/process', methods=['POST'])
def process():
    query = request.form['input_data']
    value = request.form['value']
    print(f"data: {query}")
    print(f"Value: {value}")
    spell = Speller(lang='en')
    # query = spell(query)
    print(query)
    response = requests.post('http://localhost:8011/TextProcess', json={'text': query})
    processed_text = ''

    if response.status_code == 200:
        print('//////////////////////')
        processed_text = ' '.join(response.json()['TextProcess'])

    # response2 = requests.post('http://localhost:8002/vectorizer', json={'text': processed_text})
    # query_tfidf = ''
    #
    # if response2.status_code == 200:
    #     query_tfidf = response2.json()['vectorizer']
    #     print(query_tfidf)

    response3 = requests.post('http://localhost:8015/queryMatch', json={'text': processed_text, 'dataset': value})
    query_match = ''
    if value == 'qoura':
        csv_file_path = 'FirstData/test.csv'
    else:
        csv_file_path = 'SecondData/second_data2.csv'
    df = pd.read_csv(csv_file_path)
    if response3.status_code == 200:

        sorted_documents = response3.json()
        document_textList = []
        for document_id, similarity in sorted_documents:
            # Find the row in the DataFrame that matches the document ID
            document_row = df[df['doc_id'] == int(document_id)]

            # Get the document text
            document_text = document_row['title'].values[0]
            document_textList.append(document_text)

            # Print the document ID, document text, and similarity score
            # print(f"Document: {document_id}, Similarity: {similarity}")
            # print(f"Document Text: {document_text}")
            # print()
        # print(document_text)

    return render_template('uiCore.html', data=document_textList)


@app.route('/suggest', methods=['POST'])
def suggest():
    print("ttttttttttttttttttttttttt")
    query = request.form['input_data']
    print(query)
    value = request.form['search_type']
    print(value)
    if value == 'qoura':
        my_list = queryRefinement(query, 'query_IN_Files')
    else:
        my_list = queryRefinement(query, 'second_query2')

    print(my_list)
    # print(jsonify(my_list))
    return my_list


if __name__ == '__main__':
    app.run()

# return jsonify('Hello, World!')
