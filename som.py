""" SOM
  Beatriz de Camargo Castex Ferreira - 10728077 - USP São Carlos - IFSC
  07/2020

  Nesse programa vamos implementar um mapa auto-organizado para deep learning,
  que possa ser utilizado para vários datasets diferentes, procurando
  criar clusters para o reconhecimento de padrões.

  BASE DE DADOS: https://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits

  Referências:
  CDT-25: https://www.researchgate.net/publication/340257021
  https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html
  https://scikit-learn.org/stable/modules/classes.html?highlight=datasets#module-sklearn.datasets
  https://github.com/JustGlowing/minisom/blob/master/examples/HandwrittenDigits.ipynb
  https://github.com/abhinavralhan/kohonen-maps/blob/master/gsom-iris-python.ipynb
  http://blog.yhat.com/posts/self-organizing-maps-2.html
  https://towardsdatascience.com/self-organizing-maps-ff5853a118d4
  https://glowingpython.blogspot.com/2013/09/self-organizing-maps.html


  """

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

''' Importar um dataset
 Você pode trocar essa parte e importar qualque base
 dados da forma que quiser, mas vamos usar a base de dígitos escritos a mão
 da UC Irvine que está disponível na biblioteca sci-kit learn. Outras bases de
 dados podem precisar de uma forma diferente de importar. '''

print(
    'How many classes of digits do you want to train the network with? [1 to 10]')
number_of_classes = int(input())
database = 'Digitos Manuscritos com ' + str(number_of_classes) + ' classes'
# Importa base de dados.
digits = datasets.load_digits(n_class=number_of_classes)
data = digits.data  # Coloca os dígitos em uma matriz (sem a label)
label = digits.target  # Coloca os índices em uma matriz (sem os dígitos)

# Normalizar dados
data = data / data.max()

""" ============================ SOM ============================ """


def find_bmu(test_data, net):
    # Encontra o valor de menor distância na rede
    min_distance = 10**20  # um valor absurdo
    i = 0
    for line in net:
        j = 0
        for test_weight in line:
            # Calculamos a distância entre o peso e o test
            distance = np.sum((test_data - test_weight)**2)
            # Encontramos a menor distância:
            if distance < min_distance:
                min_distance = distance
                best_index = [i, j]
            j += 1
        i += 1
    return best_index


# Definir variáveis iniciais
N = 5000  # Número de vezes que vai repetir
net_dim = 20  # Tamanho do córtex
initial_learning_rate = 0.2  # rítimo de aprendizado (alpha)
initial_radius = net_dim / 2  # raio de influência dos nódulos
time = N / np.log(initial_radius)  # tempo de deterioração das constantes
dim = data.shape[1]  # Número de atributos de cada objeto


# 1 - Criar córtex NxN em que cada nódulo tem um vetor de pesos tamanho dim aleatórios
network = np.random.random((net_dim, net_dim, dim))
start_network = network

for t in range(N):
    # 2 - Decair o rítimo de aprendizado e o raio com o tempo:
    learning_rate = initial_learning_rate * np.exp(-t / N)
    radius = initial_radius * np.exp(-t / time)

    # 3 - Escolher um ponto aleatório da base de dados para ser o teste
    test = data[np.random.randint(0, data.shape[0]), :]

    # 4 - Achar a unidade de melhor semelhança (bmu)
    bmu_index = find_bmu(test, network)

    # 5 - Achar os nódulos da rede que estão dentro da área de influência do bmu:
    # Olhamos todos os nódulos da rede
    for i in range(net_dim):
        for j in range(net_dim):
            # Vemos a distância entre ele e o bmu:
            t_dist = np.sum((np.array([i, j]) - bmu_index)**2)
            # Se estiver dentro do raio:
            if t_dist <= radius**2:
                # Calcular influência:
                influence = np.exp(-(t_dist) / (2 * (radius**2)))
                # Morfar vetor para se parecer mais com o dado teste
                to_morph = network[i, j, :]
                weight_morph = to_morph + \
                    (learning_rate * influence * (test - to_morph))
                network[i, j, :] = weight_morph
