# revisão - funções

# funções são usadas para organização e reutilização de código
# declaradas com a palavra reservada def e aquilo que a função devolve com return

def my_function(x, y, z = 1.5):
  if z > 1:
    return z * (x + y)
  else:
    return z / (x + y)

# se a função chegar ao fim e não houver return, a função devolverá None

# argumentos posicionais e nomeados; na função anterior, x e y são posicionais e z, nomeado
# assim, a função anterior pode ser passada das formas a seguir:

my_function(5, 6, z=0.7)
my_function(3.14, 7, 3.5)
my_function(10, 20)

# restrição para os argumentos de função é que argumentos nomeados devem vir depois
# dos argumentos posicionais (se houver); arg nomeados podem ser colocados em qualquer ordem
# também poderíamos ter colocado da seguinte maneira:

my_function(x=5, y=6, z=7)
my_function(y=6, x=5, z=7)

# o que ajuda na legibilidade

# escopo

# há escopo local e global; qualquer variável que receba uma atribuição em uma função
# por padrão é associada ao escopo local; depois que a função ermina de ser executada,
# as variáveis associadas a ela são destruídas

# fazer uma atribuição a uma variável fora do escopo da função é possível, mas essas
# variáveis devem ser declaradas como globais usando a palavra reservada 'global'

# retornando diversos valores

# def f():
#   a = 5
#   b = 6
#   c = 7
#   return a, b, c

# a, b, c = f()

# a função retorna uma tupla de três elementos e estamos desempacotando nas variáveis
# de resultado; também poderíamos ter feito da seguinte forma:

# return_value = f()

# e nesse caso 'return_value' estaria guardando a tupla de três
# uma alternativa possivelmente atraente seria devolver um dicionário em seu lugar:

def f():
  a = 5
  b = 6
  c = 7
  return {'a' : a, 'b' : b, 'c' : c}

print(f()) # {'a': 5, 'b': 6, 'c': 7}

# funções são objetos e muitas construções podem ser expressas de forma mais simples

states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 
'south carolina##', 'West virginia?']

import re

def clean_strings(strings):
  result = []
  for value in strings:
    value = value.strip()
    value = re.sub('[!#?]', '', value)
    value = value.title()
    result.append(value)
  return result

print(clean_strings(states)) # ['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'South Carolina', 'West Virginia']

def remove_punctuation(value):
  return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
  result = []
  for value in strings:
    for function in ops:
      value = function(value)
    result.append(value)
  return result

print(clean_strings(states, clean_ops)) # ['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'South Carolina', 'West Virginia']

# também podemos usar funções como argumentos para outras funções, como a função map, que aplica
# uma função a uma sequência de algum tipo:

for x in map(remove_punctuation, states):
  print(x) # Alabama Georgia Georgia georgia FlOrIda south carolina West virginia

# funções anônimas (lambdas)

def short_functin(x):
  return x * 2

equiv_anon = lambda x: x * 2
print(equiv_anon(2)) # 4

# exige-se menos digitação

def apply_to_list(some_list, f):
  return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
print(apply_to_list(ints, lambda x: x * 2)) # [8, 0, 2, 10, 12]

# ordenando uma lista de strings de acordo com o número de letras distintas em cada string

strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(list(x))))
print(strings) # ['aaaa', 'foo', 'abab', 'bar', 'card']

# funções lambda são chamadas também de anônimas devido ao fato de elas nunca terem um nome
# específico associado a elas quando as declaramos

# currying: aplicação parcial de argumentos

def add_numbers(x, y):
  return x + y

# usando a função acima, podemos derivar dela uma nova função:

add_five = lambda y: add_numbers(5, y)
print(add_five(7)) # 12

# e dizemos que add_numbers sofreu currying

# geradores

# protocolo iterador é um modo genérico de deixar objetos iteráveis; por exemplo, com um dicionário

some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
  print(key) # a b c

# quando escrevemos for key in some_dict, o interpretador Python tenta criar um iterador a partir
# de some_dict

dict_iterator = iter(some_dict)
print(dict_iterator) # <dict_keyiterator object at 0x000001DD54F29DF0>

# um iterador é qualquer objeto que irá produzir objetos ao interpretador quando usado em um
# contexto como um laço for; a maioria dos métodos que espera uma lista também podem ser usados
# com objetos iteráveis (min, max, sum e construtores list e tuple)

print(list(dict_iterator)) # ['a', 'b', 'c']

# um gerador é uma forma de construir um novo objeto iterável; funções usuais executam e 
# devolvem um único resultado de uma só vez, geradores devolvem uma sequência de vários
# resultados em modo lazy, com uma pausa após cada um; para criar um gerador, usamos 
# yield no lugar de return em uma função comum

def squares(n = 10):
  print('Generating squares from 1 to %d.' % (n**2))
  for i in range(1, n + 1):
    yield i ** 2

# quando chamar o gerador, nenhum código será executado:

gen = squares()
print(gen) # <generator object squares at 0x0000022F0D895A80>

# ele só executará quando você lhe solicitar elementos:

for x in gen:
  print(x, end=' ') 
# Generating squares from 1 to 100.
# 1 4 9 16 25 36 49 64 81 100

# podemos criar um gerador usando uma expressão geradora (mais concisa); é um gerador
# análogo a list, dict e set comprehensions; a diferença é o uso de parênteses

gen = (x**2 for x in range(100))
print(gen) # <generator object <genexpr> at 0x000001807EDFE260>

# isso é equivalente a:

def _make_gen():
  for x in range(100):
    yield x**2
gen = _make_gen()

# expressões geradoras podem ser usadas no lugar de list comprehensions como argumentos de função

print(sum(x**2 for x in range(100)))      # 328350
print(dict((i, i**2) for i in range(5)))  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}