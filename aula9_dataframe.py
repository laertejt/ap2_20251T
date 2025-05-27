import pandas as pd
file="C:\\Users\\21701079836\\Documents\\estruturada\\alunos.xlsx"
df = pd.read_excel(file)
df[0:5][["Matricula", "Aluno"]]
df["Endereco"] = ""