# revisão - erros e exceções

# tratar erros ou exceções em Python é parte importante no desenvolvimento de programas robustos
# a função float() falha se dados de entrada forem inadequados:

print(float('1.2345'))    # 1.2345
# print(float('something')) # ValueError: could not convert string to float: 'something'

# se quiséssemos uma versão de float que falhasse de modo elegante; podemos escrever isso
# fazendo uma função que encapsule a chamada de float em um bloco try/except:

def attempt_float(x):
  try:
    return float(x)
  except:
    return x

print('attempt_float("1.2345"): ' + str(attempt_float('1.2345')))  # 1.2345
print('attempt_float("something"): ' + attempt_float('something')) # something

# o código na parte do bloco except só será executado se float() gerar uma exceção
# note que float é capaz de gerar outras exceções:

# print(float(1, 2)) # TypeError: float expected at most 1 argument, got 2

# e talvez você queira suprimir apenas ValueError, pois um TypeError pode levar a um bug
# no seu programa; para isso, atualizamos nossa função

def attempt_float(x):
  try:
    return float(x)
  except ValueError:
    return x

# podemos capturar vários tipos de exceção escrevendo uma tupla de exceções (parênteses necessários)

def attempt_float(x):
  try:
    return float(x)
  except (ValueError, TypeError):
    return x

# em alguns casos, talvez você não queira suprimir uma exceção, mas que algum código seja executado
# independentemente de o código no bloco try ter sido bem-sucedido ou não; usamos finally:

# f = open(path, 'w')

# try:
#   write_file(f)
# finally:
#   f.close()

# assim, o handle do arquivo sempre será fechado; de forma semelhante, podemos ter um código que só
# execute se o bloco try for bem-sucedido usando else:

# f = open(path, 'w')

# try:
#   write_to_file(f)
# except:
#   print('Failed')
# else:
#   print('Succeeded')
# finally:
#   f.close()

# arquivos e o sistema operacional

# para abrir um arquivo, utilizamos a função open com um caminho de arquivo relativo ou absoluto

path = 'python\python-para-analise-de-dados\\cap3-teste.txt'
f = open(path)

lines = []
for line in f:
  lines.append(line)
print(lines)

# outra maneira de realizar a leitura; código para obter uma lista de linhas de arquivo livres de EOL
# que são os marcadores de fim de linha

lines = [x.rstrip() for x in open(path)]
print(lines)

# usando open para criar objetos de arquivos, é importante fechá-los explicitamente ao término do uso
# do arquivo

f.close()

# o uso da instrução with facilita as coisas, pois logo ao sair do bloco with criado, o arquivo f
# é fechado automaticamente

with open(path) as f:
  lines = [x.rstrip() for x in f]

# se digitássemos "f = open(path, 'w')" um novo arquivo teria sido criado (!), sobrescrevendo qualquer
# um em seu lugar; o modo de abertura 'x' cria um arquivo para escrita, mas falha se o arquivo já existir

# métodos comuns: read, seek, tell
# read devolve determinado número de caracteres

f = open(path)
print(f.read(12)) # Muitas vezes

f2 = open(path, 'rb') # modo binário de leitura
print(f2.read(12)) # b'Muitas vezes'

# read faz a posição do handle do arquivo avançar de acordo com o número de bytes lidos; tell devolve
# a posição atual

print(f.tell())  # 12
print(f2.tell()) # 12

# seek altera a posição do arquivo para o byte indicado como parâmetro:

print(f.seek(3)) # 3
print(f.tell())  # 3
print(f.read(1)) # t
print(f.tell())  # 4

# por fim, lembre-se de sempre fechar os arquivos!

f.close()
f2.close()

# para escrever em um arquivo, usamos os métodos write e writelines
# podemos escrever o .txt do exemplo sem linhas em branco

# o uso do modo 'w' sobrescreve o arquivo!!! Por isso usamos 'r+' para leitura e escrita

with open(path, 'r+') as handle:
  handle.writelines(x for x in open(path) if len(x) > 1)

with open(path) as f:
  lines = f.readlines()

print(lines)