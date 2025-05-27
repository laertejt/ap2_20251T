turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}

lista_notas = []
for chave, valor in turma.items():
    media = sum(valor["notas"]) / len(valor["notas"])
    print(f"{chave}: a media é {media}")
    lista_notas.append(media)
max(lista_notas)


dic_funcionario = {}

dic_funcionario["Nome"] = "la"

lista = ["maria"]
lista_mai=[]
for i in lista:
    lista_mai.append(i.upper())