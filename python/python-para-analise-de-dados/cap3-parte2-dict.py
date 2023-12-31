# revisão - estruturas de dados, funções, arquivos

# dictionary com pares chave-valor

d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
d1[7] = 'an integer'
print(d1)         # {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}
print(d1['a'])    # some value
print('b' in d1)  # True

# podemos apagar valores com 'del' ou pop()

del d1['a']
print(d1)  # {'b': [1, 2, 3, 4], 7: 'an integer'}
val = d1.pop(7)
print(val) # an integer
print(d1)  # {'b': [1, 2, 3, 4]}

# keys(), values() iteradores para chaves e valores do dicionário

d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
print(list(d1.keys()))   # ['a', 'b']
print(list(d1.values())) # ['some value', [1, 2, 3, 4]]

# podemos combinar um dicionário a outro com update()

d1.update({'b': 'foo', 'c': 12})
print(d1) # {'a': 'some value', 'b': 'foo', 'c': 12}

# criando dicionários a partir de outras sequências

key_list = [0, 1, 2]
value_list = ['fus', 'ro', 'dah']
mapping = {}
for key, value in zip(key_list, value_list):
  mapping[key] = value
print(mapping) # {0: 'fus', 1: 'ro', 2: 'dah'}

mapping = dict(zip(range(5), reversed(range(5))))
print(mapping) # {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}

# valores default

# a seguinte lógica é comum

# if key in some_dict:
#   value = some_dict[key]
# else:
#   value = default_value

# get() devolverá None por padrão se a chave não estiver presente

# value = some_dict.get(key, default_value)

# criando uma classificação de acordo com a primeira letra das palavras

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
  letter = word[0]
  if letter not in by_letter:
    by_letter[letter] = [word]
  else:
    by_letter[letter].append(word)
print(by_letter) # {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}

# setdefault() serve exatamente para isso

by_letter = {}
for word in words:
  letter = word[0]
  by_letter.setdefault(letter, []).append(word)
print(by_letter) # {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}

# o módulo collections tem uma classe útil chamada defaultdict

from collections import defaultdict

by_letter = defaultdict(list)
for word in words:
  by_letter[word[0]].append(word)
print(dict(by_letter)) # {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}

# valores de um dict podem ser qualquer objeto, mas chaves devem ser valores imutáveis
# assim, têm de ser usados tipo como int, float, string ou tuplas (hashability!)
# é possível verificar se um objeto é hashable (pode ser usado como chave em um dict)

# função hash()

print(hash('string'))
print(hash((1, 2, (2, 3))))
# print(hash((1, 2, [3, 4]))) # falha porque listas são mutáveis

# para usar uma lista como chave, basta convertê-la em tupla

# set é um conjunto ou coleção não ordenada de elementos únicos

print(set([2, 2, 2, 1, 1, 3, 3])) # {1, 2, 3}

# sets aceitam operações matemáticas de conjuntos

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

# união

print(a.union(b)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(a|b)        # {1, 2, 3, 4, 5, 6, 7, 8}

# intersecção

print(a.intersection(b))  # {3, 4, 5}
print(a&b)                # {3, 4, 5}

# métodos comuns: add(), clear(), remove(), pop(), union(), update(), intersection(),
# intersection_update(), difference(), difference_update(), symmetric_difference(),
# symmetric_difference_update(), issubset(), issuperset(), isdisjoint()

# list, set e dict comprehensions

# list comprehension

# my_list = [expr for val in collection if condition]

# que equivale a

# result = []
# for val in collection:
#   if condition:
#     result.append(expr)

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
arr = [x.upper() for x in strings if len(x) > 2]
print(arr) # ['BAT', 'CAR', 'DOVE', 'PYTHON']

# dict comprehension

# dict_comp = {expr-chave : expr-valor for value in collection if condition}

# set comprehension

# set_comp = {expr for value in collection if condition}

# list comprehensions aninhadas

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
print(flattened)