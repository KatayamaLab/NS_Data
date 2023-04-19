import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csv_file/2023-03-03 18-05-46.csv", header= None)
print(df[1] [50])
x = df[1]*100/(df[1][50])
print(x[50])

def plot_LabVIEW(t, x, fq, F_abs_amp, output_FN,IDN, final_graph, y_label, y_unit, result_dir):
    fig = plt.figure(figsize = (16,9))
    title = "freq_LabView_FFT"
    plt.plot(t,x)
    plt.xlabel("freqency(Hz)")