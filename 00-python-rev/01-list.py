# lista: coleção ordenada de itens

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)            # ['trek', 'cannondale', 'redline', 'specialized']

# acesso a itens pelo índice (contagem dos índices começa no 0; primeiro elemento: array[0])

print(bicycles[0])         # trek
print(bicycles[0].title()) # Trek

# acesso ao último elemento de uma lista

print(bicycles[-1]) # specialized
print(bicycles[-2]) # redline

# alterando itens da lista

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[0]) # honda
motorcycles[0] = 'ducati'
print(motorcycles[0]) # ducati

# adição de itens no fim da lista

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']

# adição de itens em qualquer posição

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles) # ['ducati', 'honda', 'yamaha', 'suzuki']

# deleção de itens em qualquer posição

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) # ['yamaha', 'suzuki']

# deleção de itens no fim da lista

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
motorcycles.pop()
print(motorcycles) # ['honda', 'yamaha']
first = motorcycles.pop(0)
print(motorcycles) # ['yamaha']
print(first)       # honda

# deleção de item a partir do valor

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = motorcycles.remove('ducati')
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

# sort

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# apenas apresentar a lista ordenada, mas manter a forma original dela

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(sorted(cars, reverse=True))

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse(), print(cars) # reverte
cars.reverse(), print(cars) # volta ao normal ao reverter novamente

# tamanho da lista

print(len(cars))

# erro de índice: o Python não consegue determinar o índice solicitado
# cars = ['bmw', 'audi', 'toyota', 'subaru'], print(cars[4])

cats = ['titela', 'pretina', 'ze da caixa', 'doce de leite', 'pikachu']
for cat in cats:
  print(cat)

for num in range(1,5): # de 1 a 4
  print(num)

for num in range(0, 11, 2): # de 0 a 10, de dois em dois
  print(num)

num = list(range(1,6))
print(num)

squares = [] # escopo!!!
for value in range(1,11):
  square = value**2
  squares.append(square)

print(squares)

digits = range(1, 10)
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehesion - abrangência de list

squares = [value**2 for value in range(1,11)]
print(squares)

# fatiando uma lista

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # ['charles', 'martina', 'michael']
print(players[1:4]) # ['martina', 'michael', 'florence']
print(players[1:5]) # ['martina', 'michael', 'florence', 'eli']
print(players[:3])  # ['charles', 'martina', 'michael']
print(players[3:])  # ['florence', 'eli']
print(players[2:])  # ['michael', 'florence', 'eli']
print(players[-3:])   # ['michael', 'florence', 'eli']
print(players[-1:])   # ['eli']

# copiando listas

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # cópia
friend_foods = my_foods # referência à mesma lista (se eu alterar my_foods, friend_foods acompanha a mudança)
friend_foods = my_foods.copy() # cópia

# tupla: é uma lista imutável (não podemos alterar ela)
# usamos parênteses no lugar de colchetes

dimensions = (200, 50)
print(dimension)
# dimensions[0] = 250 # gera um erro!

# sobrescrevemos a tupla
dimensions = (400, 100)
print(dimension)

# usamos tuplas quando queremos usar uma lista que não mudar com o decorrer do programa