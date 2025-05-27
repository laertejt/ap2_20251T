from pathlib import Path
import pandas as pd
import random

BASE_DIR = Path(__file__).parent
df = pd.read_excel(BASE_DIR / 'alunos_estruturada.xlsx')
lista = df['Aluno'].values[:-1]
random.choice(lista)
