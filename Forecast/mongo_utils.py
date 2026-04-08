from pymongo import MongoClient
from datetime import datetime
def convert_forecast_for_Mongo(forecast_list):
    return [
        {
            "ds":item["ds"].to_pydatetime() if hasatter(item["ds"],"to_pydatetime") else item["ds"],
            "yhat":float(item["yhat"]),
            "yhat_lower":float(item['yhat_lower']),
            "yhat_upper": float(item["yhat_upper"])
        }
        for item in forecast_list
    ]
def save_forecast(store_id,dept_id):
    Client=MongoClient("mongodb://localhost:27017/")
    db=Client["forecast_db"]
    collection=["sales_forecast"]
    doc={
        "store_id":int(store_id),
        "dept_id":int(dept_id),
     
        "Forecast":convert_forecast_for_Mongo(forecast_data),
        "timestamp":datetime.utcnow()

    }
    collection.insert_one(doc)

