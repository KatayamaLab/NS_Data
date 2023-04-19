import pandas as pd
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

df = pd.read_csv ('tsv_file/test_130.tsv', sep="\t", encoding="Shift-JIS", nrows=100000)
print(df.filter(items =[1]))
New_csv_file = df.to_csv (f'csv_file/{date}.csv', encoding="UTF-8", index = False)