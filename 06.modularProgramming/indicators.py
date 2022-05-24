"""
@author: Fábio Mori
"""

#Escola Matriz - Class 18: Modular Programming
#File with code of modular programming

def promocao (promocao, valor, pecas):
    valor_desconto=((1-promocao)*valor)*pecas
    valor_real=valor*pecas
    economia=valor_real-valor_desconto
    return(valor_desconto, economia)