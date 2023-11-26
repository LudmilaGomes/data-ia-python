from matplotlib import pyplot as plt
from collections import Counter

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
# é definida uma função lambda chamada decile; essa função arredonda cada 
# nota para o decil correspondente, ou seja, cada nota é arredondada para 
# o múltiplo de 10 mais próximo (por exemplo, 87 seria arredondado para 80)
decile = lambda grade: grade // 10 * 10

# cria um histograma usando a função Counter. A expressão 'decile(grade) for 
# grade in grades' aplica a função decile a cada nota da lista grades, criando 
# assim uma lista com os valores dos decis de cada nota. O Counter conta a 
# ocorrência de cada valor de decil, resultando em um dicionário que mapeia o 
# decil para a contagem de notas correspondentes.
histogram = Counter(decile(grade) for grade in grades)

print([decile(grade) for grade in grades])        # [80, 90, 90, 80, 70, 0, 80, 80, 100, 60, 70, 70, 0]
print(Counter(decile(grade) for grade in grades)) # Counter({80: 4, 70: 3, 90: 2, 0: 2, 100: 1, 60: 1})

plt.bar([x - 4 for x in histogram.keys()],  # move cada barra para a esquerda em 4
         histogram.values(),                # dá para cada barra sua altura correta
         8,                                 # dá para cada barra a largura de 8
         color='black')                     # define a cor das barras como sendo preta

plt.axis([-5, 105, 0, 5]) # eixo x de –5 até 105, eixo y de 0 até 5
plt.xticks([10 * i for i in range(11)]) # rótulos do eixo x em 0, 10, …, 100
plt.xlabel("Decil")
plt.ylabel("# de Alunos")
plt.title("Distribuição das Notas do Teste 1")
plt.show()