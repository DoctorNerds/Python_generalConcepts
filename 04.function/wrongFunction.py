"""
@author: F�bio Mori
"""

#Escola Matriz - Aula 16: Funções
#Wrong implemented code

valor_peca=500
numero_pecas=int(input(("Digite o n�mero de pe�as desejadas: ")))

if (numero_pecas<1000):
    desconto=0.1
    valor_desconto=(1-desconto*valor_peca)*numero_pecas
    valor_real=valor_peca*numero_pecas
    economia=valor_real-valor_desconto
    print('O valor a ser pago � de', valor_desconto, 
          'reais e o desconto foi de', economia, 'reais')
    
if (numero_pecas>=1000)&(numero_pecas<=5000):
    desconto=0.3
    valor_desconto=(1-desconto*valor_peca)*numero_pecas
    valor_real=valor_peca*numero_pecas
    economia=valor_real-valor_desconto
    print('O valor a ser pago � de', valor_desconto, 
          'reais e o desconto foi de', economia, 'reais')
    
if (numero_pecas>5000):
    desconto=0.5
    valor_desconto=(1-desconto*valor_peca)*numero_pecas
    valor_real=valor_peca*numero_pecas
    economia=valor_real-valor_desconto
    print('O valor a ser pago � de', valor_desconto, 
          'reais e o desconto foi de', economia, 'reais')
    