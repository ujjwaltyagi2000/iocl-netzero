# testing code to fetch data from data.gov.in
import pandas as pd
import requests

df=pd.read_csv("https://api.data.gov.in/resource/8d3b6596-b09e-4077-aebf-425193185a5b?api-key=579b464db66ec23bdd0000014d331dc47176456852b5edabe3c24089&format=csv&offset=1500&limit=999")
df.to_csv('no_data.csv')