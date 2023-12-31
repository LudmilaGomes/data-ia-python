# revisão - algumas estruturas de dados

# tuplas: sequência de itens imutável

tup = (1, 2, 3) # ou
tup = 1, 2, 3
outra_tup = (1, 2), (3, 4, 5)

# podemos converter qualquer sequência ou iterador

tup = tuple([1, 2, 3, 4])
print(tup) # (1, 2, 3, 4)
tup = tuple('string')
print(tup) # ('s', 't', 'r', 'i', 'n', 'g')

# acessamos os elementos com colchetes

print(tup[0]) # s

# não podemos modificar objetos da tupla; mas se um item for mutável, podemos modificá-lo

tup = (1, 2, 'help', [1, 2])
print(tup) # (1, 2, 'help', [1, 2])
tup[3].append(3)
print(tup) # (1, 2, 'help', [1, 2, 3])

# concatenando tuplas

print(outra_tup + tup) # ((1, 2), (3, 4, 5), 1, 2, 'help', [1, 2, 3])
print(outra_tup*3)     # ((1, 2), (3, 4, 5), (1, 2), (3, 4, 5), (1, 2), (3, 4, 5))
# assim como em listas
lista = [1, 2, 3]; print(lista*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# desempacotando tuplas

tup = (1, 2, 3)
a, b, c = tup
print(a, b, c) # 1 2 3

tup = (4, 5, (6, 7))
a, b, (c, d) = tup
print(d) # 7

a, b = 1, 2 # a = 1, b = 2
b, a = a, b # a = 2, b = 1

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
  # print('a = {0}, b = {1}, c = {2}', format(a, b, c))
  print('a = %d, b = %d, c = %d' % (a, b, c))

values = (1, 2, 3, 4, 5)
a, b, *rest = values
print(a) # 1
print(b) # 2
print(rest) # [3, 4, 5]

# métodos de tupla

a = (1, 2, 2, 2, 2, 3, 4, 2)
print(a.count(2)) # conta quantidade de ocorrências do parâmetro
print(a.index(1)) # indica o índice do primeiro valor do parâmetro passado

# listas: sequência de itens mutável

lista = [1, 2, 3]
print(lista) # [1, 2, 3]
lista[1] = 'peekaboo'
print(lista) # [1, 'peekaboo', 3]
# podemos usar listas para materializar iteradores

# inserção de elementos

lista.append('help') # adiciona ao fim
lista.insert(0, 'socorro') # adiciona na posição especificada
# insert() é custosa do ponto de vista de processamento!
print(lista) # ['socorro', 1, 'peekaboo', 3, 'help']

# deleção de elementos

lista.pop() # remove do fim
print(lista) # ['socorro', 1, 'peekaboo', 3]
lista.pop(0) # remove da posição indicada
print(lista) # [1, 'peekaboo', 3]
lista.remove('peekaboo') # remove o primeiro valor do parâmetro passado encontrado na lista
print(lista) # [1, 3]

# verificamos se a lista possui um valor específico:

print('dwarf' in lista)     # False
print(3 in lista)           # True
print('dwarf' not in lista) # True

# concatenando

nova_lista = [4, None, 'foo'] + lista
print(nova_lista) # [4, None, 'foo', 1, 3]
nova_lista = lista * 4
print(nova_lista) # [1, 3, 1, 3, 1, 3, 1, 3]
# a concatenação com '+' pode ser custosa e, no seu lugar, podemos usar o método extend
outra_lista = ['a', 'b', 'c']
outra_lista.extend(nova_lista)
print(outra_lista) # ['a', 'b', 'c', 1, 3, 1, 3, 1, 3, 1, 3]

# podemos ordenar a lista

lista = [6, 2, 9, 3]
lista.sort()
print(lista) # [2, 3, 6, 9]
lista.sort(reverse=True)
print(lista) # [9, 6, 3, 2]

# busca binária e manutenção de lista ordenada

import bisect

c = [1, 2, 2, 2, 3, 4, 7]
# bisect() retorna a posição em que um valor deve ser inserido para a lista continuar ordenada
print(bisect.bisect(c, 2)) # 4
print(bisect.bisect(c, 5)) # 6
# insort() insere o valor passado no local adequado
bisect.insort(c, 5)
bisect.insort(c, 0)
print(c) # [0, 1, 2, 2, 2, 3, 4, 5, 7]

# fatiamento

seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[1:5]) # [2, 3, 7, 5]

# podemos inserir outros elementos usando fatiamento

seq[3:4] = [6, 3]
print(seq) # [7, 2, 3, 6, 3, 5, 6, 0, 1]

# o elemento no índice 'start' está incluído, mas o índice 'stop' não está
# tanto start quanto stop podem ser omitidos para índices inicial e final

seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[:5]) # [7, 2, 3, 7, 5]
print(seq[5:]) # [6, 0, 1]

# uso de índices negativos fatiam a sequência em relação ao final

seq = 'hello!'
#  H  E  L  L  O  !
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1
print(seq[1:5]) # ello
print(seq[-5:-1]) # ello

# uso de dois pontos faz obtermos elementos alternados

print(seq[::2]) # hlo

# usando ::-1, obtemos a sequência invertida!

print(seq[::-1]) # !olleh

# enumerate

# por conta própria:

# i = 0
# for value in collection:
#   # faz algo com value
#   i += 1

# função embutida que retorna uma tupla (i, value)

# for i, value in enumerate(collection):
  # # faz algo com value

# ao indexar dados, podemos usar enumerate com um dictionary que mapeia valores aos índices
# mas temos que ter valores únicos

some_list = ['foo', 'bar', 'baz']
mapping = {}
for i, v in enumerate(some_list):
  mapping[v] = i
print(mapping) # {'foo': 0, 'bar': 1, 'baz': 2}

# sorted devolve uma lista ordenada sem alterar a sequência

my_list = [6, 5, 1, 3, 9]
print(sorted(my_list)) # [1, 3, 5, 6, 9]
print(my_list)         # [6, 5, 1, 3, 9]

# zip pareia elementos de sequências para criar uma lista de tuplas

seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = list(zip(seq1, seq2))
print(zipped) # [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]

# o número de elementos é determinado pela sequência mais curta

seq3 = [False, True]
print(list(zip(seq1, seq2, seq3))) # [('foo', 'one', False), ('bar', 'two', True)]

# uso comum de enumerate e zip em um laço for

for i, (a, b) in enumerate(zip(seq1, seq2)):
  print('{0}: {1}, {2}'.format(i, a, b))
# 0: foo, one
# 1: bar, two
# 2: baz, three

# zip pode ser usado também como 'unzip':

pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)
print(first_names)  # ('Nolan', 'Roger', 'Schilling')
print(last_names)   # ('Ryan', 'Clemens', 'Curt')

# reversed itera pelos elementos de uma sequência na ordem inversa

print(list(reversed(range(11)))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]