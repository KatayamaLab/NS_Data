import pandas as pd
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

df = pd.read_csv ('D:\\Documents\\Python Scripts\\NS make\\tsv_file\\LabView_10kHz.tsv', header = None,sep="\t")

freq = df[0][:1000]
amp = df[1][:1000]
spectrum = amp*20

df = pd.concat([freq, spectrum], axis=1)
print(df)
print(type(df))
New_csv_file = df.to_csv (f'D:\\Documents\\Python Scripts\\NS make\\csv_file/{date}.csv',  index = False)                    