alien_0 = {'color': 'green', 'points': 5} # chave 'color' e valor 'green'
print(alien_0['color'])  # green
print(alien_0['points']) # 5

# dicionário: coleção de pares chave-valor; cada chave é conectada a um valor
# e podemos usar uma chave para acessar o valor associado

# dicionários são estruturas dinâmicas
print(alien_0) # {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
# a ordem em que armazenamos os pares não importa!

# começando com um dicionário vazio
alien_0 = {}
alien_0['color'] = 'green'
print(alien_0) # {'color': 'green'}

# modificando valores
alien_0['color'] = 'yellow'
print(alien_0) # {'color': 'yellow'}

# removendo pares chave-valor
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points'] # apaga a chave e o valor associado
print(alien_0) # {'color': 'green'}

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
print("Sarah's favorite language is " 
+ favorite_languages['sarah'].title() 
+ '.') # Sarah's favorite language is C

# acessando os valores dos pares de um dicionário com um loop
user_0 = {'username': 'efermi', 'first_n': 'enrico', 'last_n': 'fermi'}
for key, value in user_0.items():
  print('Key: ' + key + ', Value: ' + value)

# items() retorna os itens de um dicionário como uma lista
list_pairs = user_0.items()
print(list_pairs)       # dict_items([('username', 'efermi'), ('first_n', 'enrico'), ('last_n', 'fermi')])
list_pairs = list(list_pairs)
print(list_pairs)       # [('username', 'efermi'), ('first_n', 'enrico'), ('last_n', 'fermi')]
print(list_pairs[0])    # ('username', 'efermi')
print(list_pairs[0][0]) # username

# usando keys()
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for keys in favorite_languages.keys(): # torna o código mais claro
  print(keys.title())
# ==
for names in favorite_languages: # mesmo efeito do uso de keys()
  print(names.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  if name in friends:
    print(name.title())

# podemos usar keys() dessa forma
if 'erin' not in favorite_languages.keys():
  print('Erin, please take our poll!')

# exibindo a lista de keys() de forma ordenada
for name in sorted(favorite_languages.keys()):
  print(name.title())

# usando values()
for value in sorted(favorite_languages.values()):
  print(value.title()) # C Python Python Ruby

# com esse uso, podemos obter valores repetidos! Para que isso não ocorra, podemos usar conjuntos (set)
for value in set(favorite_languages.values()):
  print(value.title()) # C Python Ruby
