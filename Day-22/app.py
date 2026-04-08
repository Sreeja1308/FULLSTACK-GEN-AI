import pandas as pd
from pymongo import MongoClient

df=pd.read_csv("fake_job_postings.csv")

df.dropna(subset=['title','description','fraudulent'])
Client=MongoClient("mongodb://localhost:27017/")
db=Client['job_data']
collections=db["job_posting"]

data_dict=df.to_dict(orient='records')
collections.insert_many(data_dict)
print("The data was inserted")
