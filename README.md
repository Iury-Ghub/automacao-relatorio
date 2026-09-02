# Automação de Relatório de Vendas

Script em Python que automatiza a geração de um relatório gerencial a partir de
vários arquivos de vendas. Ele lê todos os CSVs de uma pasta, consolida tudo em
uma base única e calcula indicadores de negócio, salvando o resultado em um
relatório de texto.

## Funcionalidades
- Consolida automaticamente todos os CSVs da pasta `dados/` em uma base única
- Calcula o ranking dos 5 produtos que mais faturaram
- Calcula o crescimento percentual do faturamento mês a mês
- Gera um relatório consolidado em `saida/relatorio.txt`
- Trata a entrada de forma dinâmica: basta adicionar mais CSVs em `dados/`

## Tecnologias
- Python 3.11+
- pandas

## Estrutura do projeto
````
projeto2-automacao-relatorio/
├── dados/                    # CSVs de entrada (um por mês)
│   ├── vendas_2025_01.csv
│   ├── vendas_2025_02.csv
│   └── vendas_2025_03.csv
├── saida/                    # relatório gerado (ignorado pelo Git)
│   └── relatorio.txt
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
````

## Como instalar
````bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
````

## Como rodar
````bash
python main.py
````
O relatório é gerado em `saida/relatorio.txt`.

## Exemplo de saída
````
=== RELATÓRIO DE VENDAS ===

Crescimento mensal (%):
mes
2025-01      NaN
2025-02    75.72
2025-03    35.21

=== TOP PRODUTOS ===

produto
Notebook Dell       17500.0
Monitor 27          13500.0
Cadeira gamer        4800.0
SSD 1TB              4500.0
Teclado mecanico     2800.0
````
````
````

Dois pontos pra você conferir/ajustar (documentação boa é documentação **verdadeira**):

1. **O `requirements.txt`.** Lá no setup eu te mandei instalar o `matplotlib` junto, então ele provavelmente está listado no teu `requirements.txt` — mas o código do Projeto 2 ainda **não usa** gráfico. Duas opções honestas: ou você adiciona o gráfico depois (é o item que falta pro "nível robusto") e aí o matplotlib se justifica, ou, se quiser deixar enxuto agora, dá pra gerar um requirements só com o que é usado. Por ora, deixa como está — só fica ciente dessa pontinha.

2. **Confere se a saída de exemplo bate** com o teu `relatorio.txt` real (abre o arquivo e compara). Se você mexeu em algum título, atualiza aqui.

Quando o arquivo estiver pronto, commita:
````powershell
git add README.md
git commit -m "docs: adiciona README do projeto 2"
git push
````

Detalhe de fluxo: como é uma mudança pequena de documentação, commitar direto na `master` está de bom tamanho — não precisa abrir PR pra tudo. No trabalho real, a régua costuma ser: mudança de código → branch + PR; ajuste rápido de doc → direto. Mas se quiser treinar o fluxo de PR de novo pra fixar, também é válido criar uma branch `docs/readme` — tua escolha.

Sobe o README e me diz como ficou na página do GitHub (o ideal é ele renderizar bonito, com a estrutura de pastas e o exemplo em caixinhas de código). Aí o **Projeto 2 fecha oficialmente** e a gente escolhe o próximo passo. 📸