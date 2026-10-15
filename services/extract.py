import os
import json
import requests
from datetime import datetime, timezone
import pandas as pd
import os
from pathlib import Path


parent = Path("..").resolve()

data = parent / 'raw_data'
print(type(data))


csv_files = sorted(data.glob("*.csv"))

df = []
for file in csv_files:
    df.append(pd.read_csv(file))

df_sales = df[0], df[4]
total_sales = pd.concat(df_sales)
print(total_sales)



#customer_master = csv_files[0]
#sales_orders = csv_files[4]

#print(customer_master, sales_orders)


#=========== Loading the key from the .env file =====


#df1 = pd.read_csv(data)



