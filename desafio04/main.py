import random
import numpy as np
import matplotlib.pyplot as plt

############################
##### Área de Trabalho #####
############################

# Coloque até 3 valores para rodar o algoritmo várias vezes
# Não exarege nos números, pois o algoritmo pode demorar.
colors = [ 6 ]

# Recebe um pixel (r, g, b) e os centróids atuais (um vetor
# com várias cores). Essa função deve escolher qual o índice
# tem o centróide mais próximo da cor do pixel. Use a função
# distance para fazer isso!
def find_label(pixel, centers):
    label = -1
    
    # Implemente aqui!

    return label

# Inicia pegando k pixels aleatórios da imagem real e 
# colocando na lista centers
def init_centers(img, k):
    centers = []

    # Implemente aqui!

    return np.array(centers)

def kmeans(data, k):
    centers = init_centers(data, k)

    for _ in range(10):
        new_centers = []

        # Algoritmo de treinamento aqui!
        # Use a find_label para facilitar sua vida!

        centers = np.array(new_centers)

    return centers

#############################
## Fim da Área de Trabalho ##
#############################

def distance(a, b):
    return np.linalg.norm(a - b)

def predict(centers, data):
    return np.array([find_label(pixel, centers) for pixel in data])
    
def process(img, colors):
    img = np.array(img, dtype=np.float64) / 255
    w, h, d = tuple(img.shape)
    image_array = np.reshape(img, (w * h, d))

    centers = kmeans(image_array, colors)
    labels = predict(centers, image_array)
    
    return centers[labels].reshape(w, h, -1)

picapau = plt.imread("picapau.jpg")

plt.figure(figsize=(15, 5))

plt.subplot(2, 2, 1)
plt.axis("off")
plt.title("Imagem original")
plt.imshow(picapau)

for i in range(len(colors)):
    plt.subplot(2, 2, 2 + i)
    plt.axis("off")
    plt.title(f"Imagem quantizada ({colors[i]} cores)")
    plt.imshow(process(picapau, colors[i]))

plt.tight_layout()
plt.show()