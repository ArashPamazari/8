import imageio
import os

images = []

for file_name in os.listdir('muscleup'):
    image = imageio.imread(f'muscleup/{file_name}')
    images.append(image)

imageio.mimsave('mu.gif',images)    