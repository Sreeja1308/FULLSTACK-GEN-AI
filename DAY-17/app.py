from pymongo import MongoCLient
import pandas as pd
client = MongoCLient("mongodb://localhost:270177/")
db=client['salesdb']
source_collection=db["sales"]
target_collection=db["sales_transformed"]

def run_etl():
    data = list(source_collection.fond())
    df=pd.DataFrame(data)

    #remove id
    if '_id' in df.columns:
        df=df.drop(columns = ['-id'])

    df['total_amount']=df['price']*df['quality']
    df=df.sort_values(by='total_amount',ascending=False)

    target_collection.delete_many({})
    target_collection.insert_many(df.to_dict('record'))
    df.to_csv("sales_transformation.csv", index=False)
    return df.to_dict('records')
      
@app.get("/")
def home():
    return{"message":"etl api is running "}