import ir_datasets
import pandas as pd


class DataPresentation:
    # def __init__(self):

    def load_Data(self, datasetUrl, destinationFile):
        dataset = ir_datasets.load(datasetUrl)
        data = {'id': [], 'title': []}
        for doc in dataset.docs_iter():
            print(doc)
            id = doc.doc_id
            text = doc.text
            data['id'].append(id)
            data['title'].append(text)
        df = pd.DataFrame(data['title'], columns=['title'], index=data['id'])
        df.to_csv(destinationFile)

    def load_Query(self, queryUrl, destinationFile):
        dataset = ir_datasets.load(queryUrl)
        data = {'id': [], 'title': []}
        for doc in dataset.queries_iter():
            print(doc)
            id = doc.query_id
            text = doc.text
            data['id'].append(id)
            data['title'].append(text)
        df = pd.DataFrame(data, columns=['id', 'title'])
        df.to_csv(destinationFile)

    def load_Qrels(self, qrelsUrl, destinationFile):
        dataset = ir_datasets.load(qrelsUrl)
        data = {'query_id': [], 'doc_id': [], 'relevance': [], 'iteration': []}
        for qrel in dataset.qrels_iter():
            data['query_id'].append(qrel.query_id)
            data['doc_id'].append(qrel.doc_id)
            data['relevance'].append(qrel.relevance)
            data['iteration'].append(qrel.iteration)

        df = pd.DataFrame(data)
        df.to_csv(destinationFile)
