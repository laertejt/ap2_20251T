#1.	Crie uma lista frutas contendo as seguintes frutas: "maçã", "banana", "laranja", "uva".
lista_frutas = ["maçã", "banana", "laranja", "uva"]
#2.	Imprima o primeiro e o último elemento da lista.
print(lista_frutas[0])
print(lista_frutas[-1])
#3.	Adicione a fruta "manga" ao final da lista.
lista_frutas = lista_frutas + ['manga']
#4.	Remova a fruta "banana" da lista.
lista_frutas.remove('banana')
lista_frutas.pop(0)
#5.	Substitua "laranja" por "abacaxi".
lista_frutas[2] = "abacaxi"
#6.	Crie uma lista numeros contendo os números de 1 a 10.
lista_range = list(range(1, 11))
#7.	Calcule e imprima a soma de todos os números da lista.
total = 0
for i in lista_range:
    total += i
    print(i)
print(total)
#8.	Encontre e imprima o maior e o menor número da lista.
max(lista_range)
min(lista_range)
# 9.	Inverta a ordem dos elementos na lista e imprima a lista invertida.
lista_range.reverse()
#10.	Crie uma lista cidades contendo as seguintes cidades: 
# #"São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba".
lista_cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
lista_cidades.index("São Paulo")
lista_cidades.remove("Rio de Janeiro")

nova_lista = []
for i in lista_cidades:
    nova_lista = nova_lista + [i]



