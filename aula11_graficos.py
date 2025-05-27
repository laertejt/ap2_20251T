import matplotlib.pyplot as plt
import pandas as pd

file = "C:\\Users\\21701079836\\Documents\\estruturada\\multbrindes.xlsx"
file2 = "C:\\Users\\21701079836\\Documents\\estruturada\\multbrindes2.xlsx"
file3 = "C:\\Users\\21701079836\\Documents\\estruturada\\multbrindes3.xlsx"
file4 = "C:\\Users\\21701079836\\Documents\\estruturada\\multbrindes4.xlsx"
file5 = "C:\\Users\\21701079836\\Documents\\estruturada\\multbrindes5.xlsx"
df = pd.read_excel(file)
df2 = pd.read_excel(file2)
df3 = pd.read_excel(file3)
df4 = pd.read_excel(file4)
cols = df.columns
df4.columns = cols
df_final = pd.concat([df,df2,df3,df4], axis=0, ignore_index=True)
df_final.to_excel(file5)

df.columns
df.head()
categoria = df["CARGOS"].unique()
grafico = df.groupby(["CARGOS"])["VALOR FINAL"].sum()
plt.bar(categoria, grafico)



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do arquivo
file = "C:\\Users\\21701079836\\Documents\\estruturada\\dna_escola_despesas.xlsx"
df = pd.read_excel(file)
# Agrupamento por cargos
grafico = df.groupby("CARGOS")["VALOR FINAL"].sum().sort_values(ascending=False)
# Tamanho da figura
plt.figure(figsize=(12, 6))
# Paleta de cores do Seaborn
cores = sns.color_palette("viridis", len(grafico))
# Criação do gráfico
bars = plt.bar(grafico.index, grafico.values, color=cores)
# Adiciona os valores sobre as barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height, f'R${height:,.2f}', ha='center', va='bottom', fontsize=9)
# Títulos e rótulos
plt.title("Total de Despesas por Cargo", fontsize=16)
plt.xlabel("Cargos", fontsize=12)
plt.ylabel("Valor Final (R$)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)



# Linha
x = pd.date_range(start="2025-05-01", periods=5, freq="D")
y = [2,4,6,8,10]
plt.plot(x, y, marker="x")
plt.title("Grafico de Linha")
plt.xlabel("Datas")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)

# Barra
categoria = ["Maca", "Banana", "Cereja", "Uva"]
valores = [23,17,35,29]
plt.bar(categoria, valores) 

# Horizontal
plt.barh(categoria, valores)

# Pizza
categoria = ["Maca", "Banana", "Cereja", "Uva"]
valores = [10,50,30,10]
plt.pie(valores, labels=categoria)
