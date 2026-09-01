import glob
import pandas as pd

dataframes = []

for file in glob.glob("dados/*.csv"):
    dataframes.append(pd.read_csv(file))
vendas = pd.concat(dataframes, ignore_index=True)
print(f"Total de linhas consolidadas: {len(vendas)}")