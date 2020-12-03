from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

try:
    # TASK 1
    print('\nЗадание 1\n')
    path = input('Введите путь к файлу: ')
    image = Image.open(path)
    imageColors = np.asarray(image)
    print("Изображение прочитано и записано в массив")
    # TASK 2
    print('\nЗадание 2\n')
    minValueRedChannel = imageColors[:,:,0].min()
    minValueGreenChannel = imageColors[:,:,1].min()
    minValueBlueChannel = imageColors[:,:,2].min()
    maxValueRedChannel = imageColors[:,:,0].max()
    maxValueGreenChannel = imageColors[:,:,1].max()
    maxValueBlueChannel = imageColors[:,:,2].max()
    averageValueRedChannel = imageColors[:,:,0].mean()
    averageValueGreenChannel = imageColors[:,:,1].mean()
    averageValueBlueChannel = imageColors[:,:,2].mean()
    print('Минимальное значение по каналу RED: ', minValueRedChannel)
    print('Минимальное значение по каналу GREEN: ', minValueGreenChannel)
    print('Минимальное значение по каналу BLUE: ', minValueBlueChannel)
    print('Максимальное значение по каналу RED: ', maxValueRedChannel)
    print('Максимальное значение по каналу GREEN: ', maxValueGreenChannel)
    print('Максимальное значение по каналу BLUE: ', maxValueBlueChannel)
    print('Среднее значение по каналу RED: ', averageValueRedChannel)
    print('Среднее значение по каналу GREEN: ', averageValueGreenChannel)
    print('Среднее значение по каналу BLUE: ', averageValueBlueChannel)
    # TASK 3
    print('\nЗадание 3\n')
    grayFactors = [0.299, 0.587, 0.114]
    grayImageСolors = np.uint8(imageColors[:, :, 0] * grayFactors[0] + imageColors[:, :, 1] * grayFactors[1] + imageColors[:, :, 2] * grayFactors[2])
    grayImage = Image.fromarray(grayImageСolors)
    grayImage.save('Lena_grayscaled.png')
    print("Цветное изображение преобразовано в полутоновое и сохранено")
    # TASK 4
    print('\nЗадание 4\n')
    thresholdedImageColors = grayImageСolors.copy()
    thresholdedImageColors[thresholdedImageColors<100] = 0
    thresholdedImage = Image.fromarray(thresholdedImageColors)
    thresholdedImage.save('Lena_thresholded.png')
    print('Изображение с пороговой обработкой сохранено')
    #TASK 5
    print('\nЗадание 5\n')
    fig, ax = plt.subplots()
    ax.hist(thresholdedImageColors)
    ax.set_xlabel('Значения яркости')
    ax.set_ylabel('Количество пикселей')
    print("Гистограмма распредления яркости изображения построена")
    fig.show()
    fig.savefig('hist.png')
except FileNotFoundError:
    print('Файл не существует!')