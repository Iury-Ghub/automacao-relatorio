import glob
import pandas as pd

dataframes = []

for file in glob.glob("dados/*.csv"):
    dataframes.append(pd.read_csv(file))
vendas = pd.concat(dataframes, ignore_index=True)
print(f"Total de linhas consolidadas: {len(vendas)}")

vendas["receita"] = vendas["quantidade"] * vendas["preco_unitario"]

top_produtos = (
    vendas
    .groupby("produto")
    ["receita"].sum().sort_values(ascending=False).head(5)
)

print("Top 5 produtos por faturamento:")
print(top_produtos)