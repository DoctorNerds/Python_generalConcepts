"""
@author: Fábio Mori
"""

#Escola Matriz - Aula 16: Function
#Implemented code with function

def calculo (promocao, valor, pecas):
    valor_desconto=((1-promocao)*valor)*pecas
    valor_real=valor*pecas
    economia=valor_real-valor_desconto
    return(valor_desconto, economia)

valor_peca=500
numero_pecas=int(input(("Digite o número de peças desejadas: ")))

if (numero_pecas<1000):
    desconto=0.01
    valor_desconto, economia = calculo(desconto, valor_peca, numero_pecas)
    print('O valor a ser pago é de', valor_desconto, 'reais e o desconto
          foi de', economia, 'reais')
    
if (numero_pecas>=1000)&(numero_pecas<=5000):
    desconto=0.03
    valor_desconto, economia = calculo(desconto, valor_peca, numero_pecas)    
    print('O valor a ser pago é de', valor_desconto, 'reais e o desconto
          foi de', economia, 'reais')
    
if (numero_pecas>5000):
    desconto=0.05
    valor_desconto, economia = calculo(desconto, valor_peca, numero_pecas)    
    print('O valor a ser pago é de', valor_desconto, 'reais e o desconto
          foi de', economia, 'reais')