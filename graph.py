import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("D:\Documents\LabView_data\LabView_2MHz.tsv",header=None, sep="\t")
# print(df)
freq = df[0][:1000]
spectrum = df[1][:1000]
amp = spectrum[50]
spectrum *= 20

plt.figure(figsize=(16,9))
plt.bar(freq, spectrum, width=3.0)
plt.yscale("log")
plt.grid()
plt.xlim(0,500)
plt.ylim(10**(-4), 10**2)
plt.show()