from PIL import Image
import numpy as np


# TASK 1
print('\nЗадание 1\n')
path = input('Введите путь к файлу: ')
try:
    image = Image.open(path)
    arr = np.asarray(image)

except FileNotFoundError:
    print('Файл не существует!')