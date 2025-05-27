# Exercício 4: Conversão de Mês para Número
# Escreva um programa que peça ao usuário para digitar o nome de um mês e retorne seu número correspondente.
# Exemplo:
# - Entrada: 'Março' → Saída: '03'
# - Entrada: 'Dezembro' → Saída: '12'

# Exemplo de entrada:
# ['Janeiro', 'Maio', 'Setembro', 'Novembro']
lista_mes = ['Janeiro', 'Maio', 'Setembro', 'Novembro']

for mes in lista_mes:
    if mes == 'Janeiro':
        print("mes é 1")
    elif mes == 'Fevereiro':
        print("mes é 2")
    elif mes == 'Marco':
        print("mes é 3")
    elif mes == 'Abril':
        print("mes é 4")

dic_mes = {
    "Janeiro": {"julia": 1, "ana": 10},
    "Fevereiro": 2,
    "Marco": 3,
    "Abril": 4,
    "Maio": 5,
    "Junho": 6,
    "Julho": 7,
    "Agosto": 8,
    "Setembro": 9,
    "Outubro": 10,
    "Novembro": 11,
    "Dezembro": 12,
}

dic = {
    "calebe": {"media": 10},
    "jose":  {"media": 8},
    "joao":  {"media": 9},
}

for chave, valor in dic.items():
    valor



dic_mes["Janeiro"]["ana"]


for mes in lista_mes:
    print(dic_mes[mes])
dic_mes.items()

mes = input("Digite o mes:")
print(dic_mes[mes])

dic_mes["janeiro"]= 0