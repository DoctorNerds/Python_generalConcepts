"""
@author: Fábio Mori
"""

#Escola Matriz - Class 12: Python Introduction

#1. Prompt user for name and age and show on screen
nome=input("Qual é o seu nome? ")
idade=input("Quantos anos você tem? ")
print('\nOlá,', nome, 'é um prazer ter você como aluno da Escola Matriz')

#2. Get a value from the user and store it in a predefined variable (int and string)
x=int(input('Digite um número: '))
y=str(input('Digite uma palavra: '))    

#3.1 Create a string and select the piece that will be shown on the screen by slicing technique
palavra='programador'
print(palavra[0:5])
print(palavra[4])

#3.2 Create a list and select the piece that will be shown on the screen by slicing technique
#and change specific elements
filmes=["Matrix","Senhor dos Anéis", "Harry Potter"]
print(filmes[1])
print(filmes[2])
filmes[2]="Maze Runner"
print(filmes[2])
filmes.append("Jogos Vorazes")

#3.3 Create a list whith string and integer type values
aleatorio=["Pipoca", 111, "panela", 1.0]

#3.4 Create a tuple and select the piece that will be shown on screen by slicing technique
#and change specific elements
comidas=('miojo', 1.8, "macarrão")
print(comidas[1])
comidas[1]="feijoada"

#4.1 Transform a list into dictionary using the query resource to a specific element inside it
itens=[('Computador',4000),('HD externo',350.99),('Fone Gamer',1500.99)]
lista_itens=dict(itens)
print(lista_itens.keys())
print(lista_itens.values())
print(lista_itens['Computador'])

#4.2 Create a dictionary and using the query resource to a specific element inside it
itens={'Computador':4000, 'HD externo':350.99, 'Fone Gamer':1500.99}
item=input("Qual item da lista você deseja comprar? ")
valor=itens[item]
print('O valor do ', item, 'é de ', valor)

#5. Create a matrix through lists
A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(A[1][2])
print(A[2][0])

#6. Make operations between scalars numbers 
x=3
y=4
w1=x+y
w2=y-x
z=12
w3=z/y
w4=x*y
w5=y/x
w6=y//x
w7=y%x
w8=x**2

#7. Compare scalars values and shown the result on screen
a=7
b=7
c=4
d=9
print(a==b)
print(a==c)
print(a>d)
print(b!=c)


