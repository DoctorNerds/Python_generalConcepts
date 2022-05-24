"""
@author: Fábio Mori
"""

#Escola Matriz - Class 16: Function
#Fixed implemented code

valor_peca=500
numero_pecas=int(input(("Digite o número de peças desejadas: ")))

if (numero_pecas<1000):
    desconto=0.01
    valor_desconto=((1-desconto)*valor_peca)*numero_pecas
    valor_real=valor_peca*numero_pecas
    economia=valor_real-valor_desconto
    print('O valor a ser pago é de', valor_desconto, 
          'reais e o desconto foi de', economia, 'reais')
    
if (numero_pecas>=1000)&(numero_pecas<=5000):
    desconto=0.03
    valor_desconto=((1-desconto)*valor_peca)*numero_pecas
    valor_real=valor_peca*numero_pecas
    economia=valor_real-valor_desconto
    print('O valor a ser pago é de', valor_desconto, 
          'reais e o desconto foi de', economia, 'reais')
    
if (numero_pecas>5000):
    desconto=0.05
    valor_desconto=((1-desconto)*valor_peca)*numero_pecas
    valor_real=valor_peca*numero_pecas
    economia=valor_real-valor_desconto
    print('O valor a ser pago é de', valor_desconto, 
          'reais e o desconto foi de', economia, 'reais')