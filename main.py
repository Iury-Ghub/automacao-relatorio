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

vendas["data"] = pd.to_datetime(vendas["data"])
vendas["mes"] = vendas["data"].dt.to_period("M")
faturamento_mensal = vendas.groupby("mes")["receita"].sum()

crescimento_mensal = (faturamento_mensal.pct_change()* 100).round(2)

print("Crecimento mensal (%:")
print(crescimento_mensal)
