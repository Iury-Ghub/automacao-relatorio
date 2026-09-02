import glob
import pandas as pd

dataframes = []

#cria lista
for file in glob.glob("dados/*.csv"):
    dataframes.append(pd.read_csv(file))
vendas = pd.concat(dataframes, ignore_index=True)

#cria receita
print(f"Total de linhas consolidadas: {len(vendas)}")

vendas["receita"] = vendas["quantidade"] * vendas["preco_unitario"]

#cria top produtos
top_produtos = (
    vendas
    .groupby("produto")
    ["receita"].sum().sort_values(ascending=False).head(5)
)

vendas["data"] = pd.to_datetime(vendas["data"])
vendas["mes"] = vendas["data"].dt.to_period("M")
faturamento_mensal = vendas.groupby("mes")["receita"].sum()

crescimento_mensal = (faturamento_mensal.pct_change()* 100).round(2)

with open("saida/relatorio.txt", "w", encoding="utf-8") as f:
    f.write("=== RELATÓRIO DE VENDAS ===\n\n")

    f.write("Crescimento mensal (%):\n")
    f.write(crescimento_mensal.to_string())
    f.write("\n\n")

    f.write("=== TOP PRODUTOS ===\n\n")
    f.write(top_produtos.to_string())
    f.write("\n\n")


