import pandas as pd
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
tqdm.pandas()

model = SentenceTransformer('BAAI/bge-small-en-v1.5')

df = pd.read_csv("SecondData/second_data2.csv")
df = df.fillna('')
print(df)

df["embedding"] = df.title.progress_apply(lambda x: model.encode(x))
df.to_parquet('./embedding_second2.pqt', index=False)