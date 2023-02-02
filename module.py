import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

country_index = pd.read_csv("country_index.csv")
province_index =pd.read_csv("province_index.csv")
region_1_index = pd.read_csv("region_1_index.csv")
variety_index = pd.read_csv("variety_index.csv")
winery_index = pd.read_csv("winery_index.csv")


# df = pd.read_csv("preprocess.csv")
# perfectwines = df[df["points"]==95].sort_values("price")

df_pinot = pd.read_csv("df_pinot.csv")
perfectpinot = df_pinot[df_pinot["points"]>=95].sort_values("price")
pinot_sellers = df_pinot[df_pinot["winery"].isin(df_pinot.value_counts("winery")[df_pinot.value_counts("winery") >= 20].index)].groupby("winery").agg(
    {"title":"count",
     "price":['min', 'median',"mean",'max'],
     "points":['min', 'median',"mean",'max'],
     
     })

df_bourgogne = pd.read_csv("df_bourgogne.csv")
perfectbourgogne = df_bourgogne[df_bourgogne["points"]>=95].sort_values("price")
bourgogne_sellers = df_bourgogne[df_bourgogne["winery"].isin(df_bourgogne.value_counts("winery")[df_bourgogne.value_counts("winery") >= 20].index)].groupby("winery").agg(
    {"title":"count",
     "price":['min', 'median',"mean",'max'],
     "points":['min', 'median',"mean",'max'],
     
     })

df_beaune = pd.read_csv("df_beaune.csv")
perfectbeaune = df_beaune[df_beaune["points"]>=95].sort_values("price")
beaune_sellers= df_beaune[df_beaune["winery"].isin(df_beaune.value_counts("winery")[df_beaune.value_counts("winery") >= 10].index)].groupby("winery").agg(
    {"title":"count",
     "price":['min', 'median',"mean",'max'],
     "points":['min', 'median',"mean",'max'],
     
     })

df_croix_predicted = pd.read_csv("df_croix_predicted.csv")

