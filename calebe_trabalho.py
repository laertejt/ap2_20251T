import pandas as pd
import matplotlib.pyplot as plt
file = "C:\\Users\\21701079836\\Documents\\estruturada\\multbrindes_classes.xlsx"
df = pd.read_excel(file)
df.columns
contagem = df["Código Geral"].value_counts()
contagem.plot.bar()

contagem_lucro = df.groupby(["Código Geral"])["Lucro"].sum()
contagem_lucro.plot.bar()
contagem_lucro.plot.pie()