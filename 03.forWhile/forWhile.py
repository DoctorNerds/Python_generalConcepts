"""
@author: Fábio Mori
"""

#Escola Matriz - Class 14: Conditional Operations FOR/WHILE

#Resolution of exercise proposed in README.md

for i in range (10, 21, 5):
    preco=i
    vendas=1
    receita=vendas*preco
    custo_variavel=(0.1*preco)*vendas
    custo_fixo=100
    custo_total=custo_variavel+custo_fixo
    lucro=receita-custo_total
    if lucro<2000:
        while lucro<2000:
            vendas=vendas+1
            receita=vendas*preco
            custo_variavel=(0.1*preco)*vendas
            custo_total=custo_variavel+custo_fixo
            lucro=receita-custo_total
        print('Para o preço de', preco,' é necessário ter', vendas,
              ' vendas')
    else:
        print('Para o preço de', preco,' é necessário ter', vendas,
              ' vendas')