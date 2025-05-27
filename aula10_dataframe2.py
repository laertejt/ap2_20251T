import pandas as pd
import matplotlib.pyplot as plt
file = "C:\\Users\\21701079836\\Documents\\estruturada\\Dados_de_Pacientes.csv"
df = pd.read_csv(file)
df.columns
df["Idade"].describe()
df["faixa_idade"] = pd.cut(df["Idade"], bins=[0,12,18,50,100],
       labels=["crianças", "adolescentes", "adultos", "idosos"])
contagem = df["faixa_idade"].value_counts()
# Melhoria do gráfico de pizza
plt.figure(figsize=(8, 8))
ax = contagem.plot.pie(
    autopct='%1.0f%%',       # Porcentagens com uma casa decimal
    startangle=120,           # Inicia o gráfico de pizza a partir de 90°
    colors=['#483D8B', '#99ff99', '#ffcc99', '#ff6666'],  # Cores customizadas
    explode=[0.1, 0, 0, 0],  # Explodir a fatia "crianças" para destaque
    wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'linestyle': 'solid'},  # Bordas das fatias
    textprops={'fontsize': 12, 'color': 'black'}  # Ajusta o estilo do texto
)

# Título e outras customizações
plt.title("Distribuição por Faixa Etária", fontsize=14)
plt.ylabel("")  # Remove a label "faixa_idade"
plt.show()






# exercicio 1
df.head(5)
df.tail(5)
df.sample(5)
# ex 2
df.shape
# ex 3
df.columns
# ex 4
df.dtypes
# ex 5
df.describe()
# ex 6
df.info()
# ex 7
df["Procedimento"].unique()
# ex 8
filtro = df["Procedimento"]=="Implante Dentário"
df_implante = df[ filtro ]
df_implante["Idade"].mean()

df.groupby(["Procedimento"])["Idade"].mean()


# ex 9
cols = ['Cidade', 'Bairro', 'Valor_Imovel']
df2 = df[cols]
# ex 10
filtro = df["Cidade"]=="Curitiba"
df_cwd = df2[filtro]
# ex 11
df.isnull().sum()
# ex 12
df2 = df2.sort_values(["Valor_Imovel"], ascending=True)
#ex 13
valor_media = df2["Valor_Imovel"].mean()
#ex 14
df2["Valor_Imovel"].median()
#ex 15
df2["Valor_Imovel"].std()
#ex 16
df2["Valor_Imovel"].min()
df2["Valor_Imovel"].max()
# ex 17
filtro = df["Valor_Imovel"]>=valor_media
df2[ filtro ]
# ex 18
df["valor_m2"] = df["Valor_Imovel"] / df["Area_m2"]
# ex 19
dic = [{"Cidade":"Teste", "Valor_Imovel":99999, "Area_m2":100}]
df3 = pd.DataFrame(dic)
df = pd.concat([df, df3], axis=0)
# 
df[df["ID_Imovel"].isnull()]

df.to_excel("C:\\Users\\21701079836\\Documents\\estruturada\\junta.xlsx")

