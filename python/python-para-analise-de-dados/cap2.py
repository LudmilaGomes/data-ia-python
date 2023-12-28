# revisão - básico da linguagem

# expressões ternárias: if-else em uma linha

var1 = 34 if 50 > 2 else 30
print(var1) # 34
var2 = 34 if 50 < 2 else 30
print(var2) # 30

# range(): devolve iterador com sequência de inteiros

print(range(0, 10))           # range(0, 10)
print(list(range(0, 10)))     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 20, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(list(range(5, 0, -1)))  # [5, 4, 3, 2, 1]
# range() gera inteiros até o limite superior, sem incluir seu valor

# uso comum: range(len('variavel'))
seq = [1, 2, 3, 4, 5]
for i in range(len(seq)):
  print(seq[i]) # 1 2 3 4 5

soma = 0
for valor in range(100000):
  if valor % 3 == 0 or valor % 5 == 0:
    soma += valor
# apesar de usar gerar um intervalo muito grande, o uso de memória é baixo!

# pass: instrução 'no-op' (semelhante ao uso de apenas ';' em uma linha; não executa nenhuma instrução)

x = 34
if x < 0:
  print('Negativo')
elif x == 0:
  pass
else:
  print('Positivo') # Positivo

# datetime, date, time

from datetime import datetime, date, time

dt = datetime(2023, 12, 28, 13, 15, 14)
print(dt.day)     # 28
print(dt.month)   # 12
# retirar date e time de datetime
print(dt.date())  # 2023-12-28
print(dt.time())  # 13:15:14
# formatando
print(dt.strftime('%d/%m/%Y %H:%d')) # 28/12/2023 13:28
# conversão de string em datetime
dt = datetime.strptime('20232812', '%Y%d%m')
print(dt) # 2023-12-28 00:00:00
dt = dt.replace(hour=13, minute=21)
print(dt) # 2023-12-28 13:21:00

# None: valor nulo do Python; instância única do NoneType

a = None
print(a is None) # True
b = 5
print(b is None) # False

def add_maybe_mult(a, b, c=None):
  result = a + b
  if c is not None:
    result = result * c
  return result

print(type(None)) # <class 'NoneType'>

# casting de tipos

string = '3.14159'
print(string, type(string)) # 3.14159 <class 'str'>
fval = float(string)
print(fval, type(fval)) # 3.14159 <class 'float'>
int_val = int(fval)
print(int_val, type(int_val)) # 3 <class 'int'>