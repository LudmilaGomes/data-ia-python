import numpy as np

# np.loadtxt, np.genfromtxt
dataset = np.genfromtxt('C:\\Users\\ludmi\\OneDrive\\Documentos\\Meus Códigos (Folder VSCode)\\musica-ia\\inteligencia-artificial\\numpy\\housing.csv', delimiter=',', dtype=np.float64)
print(dataset.shape)

# np.loadtxt did't work