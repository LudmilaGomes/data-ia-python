from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# barras possuem o tamanho padrão de 0.8, então adicionaremos 0.1 às
# coordenadas à esquerda para que cada barra seja centralizada

# função enumerate gera pares de índice e valor da lista movies; 
# o loop for i, _ in enumerate(movies) percorre esses pares e cria uma nova lista xs, 
# adicionando 0.1 à coordenada x para cada barra do gráfico.
xs = [i + 0.1 for i, _ in enumerate(movies)]
# as barras do gráfico com as coordenadas x à esquerda [xs], alturas [num_oscars]
plt.bar(xs, num_oscars, color='red')
plt.ylabel("# de Premiações")
plt.title("Meus Filmes Favoritos")
# nomeia o eixo x com nomes de filmes na barra central
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)
plt.show()