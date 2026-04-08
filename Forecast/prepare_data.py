import pandas as pd
def load_and_merge_data():
    sales_df=pd.read_csv("train.csv",parse_dates=["Dates"])
    features_df=pd.read_csv("features.csv",parse_dates=["Dates"])
    stores_df=pd.read_csv("stores.csv",parse_dates=["Dates"])
    merged=pd.merge(sales_df,features_df,on=["Store","Dates"], how="left")
    merged=pd.merge(merged, stores_df,on="Store",how="left")
    for i in range(1,6):
        merged[f"MarkDown{i}"]=merged[f"MarkDown{i}"].fillna(0)
    return merged