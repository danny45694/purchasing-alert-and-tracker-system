import os
import json
import requests
from datetime import datetime, timezone
import pandas as pd
import os
from pathlib import Path

parent = Path("..").resolve()

data = parent / 'raw_data'

list = []
for file in data.iterdir():
    df = pd.read_csv(file)
    list.append(df)

print(list)

#=========== Loading the key from the .env file =====

