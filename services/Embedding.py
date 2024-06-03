import pandas as pd
import torch
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import semantic_search
tqdm.pandas()



# model = SentenceTransformer('BAAI/bge-small-en-v1.5')

def embeedingWithSentenceTransFormer(query,dataset):
    model = SentenceTransformer('BAAI/bge-small-en-v1.5')
    print('1111111111111')
    filePath=""
    docIdColumn=""
    dataSetPath=""
    if dataset == 'qoura':
       filePath="../embedding.pqt"
       docIdColumn="Unnamed: 0"
       dataSetPath="../FirstData/test.csv"
    else:
       filePath="../embedding_second2.pqt"
       docIdColumn = "id"
       dataSetPath = "../SecondData/second_data2.csv"


    df = pd.read_parquet(filePath)
    df = df.fillna('')

    id_to_index = dict(enumerate(df[docIdColumn].tolist()))

    df["embedding_list"] = df["embedding"].progress_apply(lambda x: torch.FloatTensor(x))
    print(df)
    output = model.encode(query)

    query_embeddings = torch.FloatTensor(output)

    hits = semantic_search(query_embeddings, df["embedding_list"].to_list(), top_k=10)
    df2 = pd.read_csv(dataSetPath)

    # document_row = df[df['doc_id'] == int(document_id)]

    results = []
    for hit in hits[0]:
        corpus_id = hit["corpus_id"]
        result = {
            "id": id_to_index[corpus_id],
            "score": hit["score"]
        }
        document_row = df2[df2['doc_id'] == int(id_to_index[corpus_id])]
        document_text = document_row['title'].values[0]
        results.append(document_text)

    for result in results:
        print(result)

    return results


# embeedingWithSentenceTransFormer('how much should i feed my 1 year old english mastiff?')





