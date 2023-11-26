from matplotlib import pyplot as plt

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# recebe duas listas como argumentos: a lista friends para o eixo x e a lista minutes para o eixo y
plt.scatter(friends, minutes)
# nomeia cada posição
for label, friend_count, minute_count in zip(labels, friends, minutes):
    # plt.annotate(label, xy=(friend_count, minute_count), xytext=(5, -5), textcoords='offset points')
    plt.annotate(label,
    xy=(friend_count, minute_count), # coloca o rótulo com sua posição
    xytext=(5, -5), # mas compensa um pouco
    textcoords='offset points')
plt.title("Minutos Diários vs. Número de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("minutos diários passados no site")
plt.show()

'''
função annotate é usada para adicionar rótulos a cada ponto no gráfico; ela recebe os 
seguintes argumentos:

    label: O rótulo associado ao ponto;
    xy: As coordenadas (friends, minutes) do ponto onde o rótulo será colocado;
    xytext: Um deslocamento de 5 unidades para a direita e -5 unidades para baixo 
        em relação ao ponto para posicionar o rótulo de forma mais clara;
    textcoords='offset points': Especifica que o deslocamento (xytext) é fornecido 
        em coordenadas de pontos;

'''