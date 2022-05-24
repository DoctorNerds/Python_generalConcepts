"""
@author: Fábio Mori
"""

#Escola Matriz - Class 13: Conditional Operations IF/ELSE

#Exercice inputs: Dictionary of registration number and grades 
notas_sala = {111001: 7, 111002: 10, 111005: 5,
              111008: 4, 111009: 6, 111010: 5.5,
              111011: 3.5}

#Resolution of exercise proposed in README.md

#PART 1
x=int(input("Digite seu número de matrícula: "))

nota=notas_sala[x]

if nota >= 7:
    print("Parabéns, você foi aprovado")
else:
    print("Você não obteve nota necessária para aprovação")
    
#PART 2
if nota == 10:
    print("Parabéns, você obteve a nota máxima")
    
elif 10>nota>=7:
    print("Parabéns, você foi aprovado")
    
elif nota < 7:
    final=((7*2)-nota)
    if final>10:
        print('Você foi reprovado')
    else:
        print('Você ainda não obteve aprovação e precisa obter a nota',
              final, 'no exame final.')

