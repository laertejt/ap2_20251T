# Entrada
# num1 = int(input("Digite o numero inteiro:"))
# num2 = int(input("Digite o numero inteiro:"))


def somar(num1, num2):
    resposta = num1 + num2
    return resposta

num1 = 5
num2 = 6
s1 = somar(num1, num2)
print(s1)


# Exercicio 2
# num_par_impar = 6
# resto = num_par_impar % 2
# if resto == 0:
#     print("Numero é Par")
# else:
#     print("Numero é Impar")




def eh_par(x):
    resto = x % 2
    if resto == 0:
        return True
    else:
        return False

if eh_par(4):
    print('é par')
else:
    print('é impar')





#Exercicio 3
num1 = 5
num2 = 3
num3 = 10
resposta = (num1+num2+num3)/3
print(resposta)

def calcular_media(num1, num2, num3):
    resposta = (num1+num2+num3)/3
    return resposta 

resposta = calcular_media(num1, num2, num3)


# Exercicio 4
num1 = 10
num2 = 15
num3 = 20



def maior(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            print(num1)
            return num1
    else:
        if num2 >= num3:
            print(num2)
            return num2
        else:
            if num3 >= num1:
                print(num3)
                return num3

x = 10
y = 15
z = 20      
maior(x, y, z)



# Exercicio 5
num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
sinal = input("Digite a Operação:")

if sinal=='+':
    print(num1 + num2)
elif sinal=='-':
    print(num1 - num2)
elif sinal=='*':
    print(num1 * num2)
elif sinal=='/':
    print(num1 / num2)
else:
    print('Operacao nao existe')


def calculadora(y, z, sinal):
    if sinal=='+':
        print(num1 + num2)
    elif sinal=='-':
        print(num1 - num2)
    elif sinal=='*':
        print(num1 * num2)
    elif sinal=='/':
        print(num1 / num2)
    else:
        print('Operacao nao existe')

calculadora(sinal="+", z=1, y=3)

# Exercicio 6
# 6.	Ler uma sequência de números inteiros e contar quantos são positivos, negativos e zeros.
# Entrada: Uma lista de números inteiros (o usuário decide quantos números serão inseridos).
# Saída: A contagem de números positivos, negativos e zeros.
# Exemplo:
# Entrada: [3, -1, 0, 7, -5]
# Saída: 2 positivos, 2 negativos, 1 zero

lista = [3, -1, 0, 7, -5]
lista_positivo = []
lista_negativo = []
lista_zero = []
contador_positivo = 0
contador_negativo = 0
contador_zero = 0
for n in lista:
    if n > 0:
        lista_positivo.append(n)
        contador_positivo +=1
    elif n == 0:
        lista_zero.append(n)
        contador_zero +=1
    else:
        lista_negativo.append(n)
        contador_negativo +=1
len(lista_negativo)
len(lista_positivo)


def definir_positico(lista):
    lista_positivo = []
    lista_negativo = []
    lista_zero = []
    contador_positivo = 0
    contador_negativo = 0
    contador_zero = 0
    for n in lista:
        if n > 0:
            lista_positivo.append(n)
            contador_positivo +=1
        elif n == 0:
            lista_zero.append(n)
            contador_zero +=1
        else:
            lista_negativo.append(n)
            contador_negativo +=1
            len(lista_negativo)
            len(lista_positivo)

# 7.	Escrever um programa que receba as 3 notas das avaliações dos alunos e determine a média final através da ponderação padrão do Ibmec.
# Entrada: Três números.
# Saída: Nota Final.
# Exemplo:
# Entrada: 5, 6.5, 10
# Saída: 6

    




         

    


