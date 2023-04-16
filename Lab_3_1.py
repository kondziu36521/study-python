
from PIL import Image
import numpy as np
from skimage import io, feature
import os
import csv


path_concrete = r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_1_concrete\concrete-texture.jpg"
path_concrete_direction = r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_1_concrete\samples/"
path_wood = r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_2_oak_wood\teksture_wood.png"
path_wood_direction = r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_2_oak_wood\samples/"
path_brick = r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_3_brick\brick_teksture.jpg"
path_brick_direction = r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_3_brick\samples/"


def crop_image(width_cut, height_cut):

    img_concrete = Image.open(path_concrete)
    img_wood = Image.open(path_wood)
    img_brick = Image.open(path_brick)

    width, height = img_concrete.size

    # oblicz liczbę próbek w poziomie i w pionie
    num_samples_x = width // width_cut
    num_samples_y = height // height_cut

    i_c = 0

    # przejdź przez wszystkie próbki i wytnij je
    for y in range(num_samples_y):
        for x in range(num_samples_x):
            # wytnij próbkę o wymiarach 128x128 pikseli
            left = x * width_cut
            upper = y * height_cut
            right = left + width_cut
            lower = upper + height_cut
            sample = img_concrete.crop((left, upper, right, lower))

            # Przekształć obraz do skali szarości
            sample = sample.convert('L')

            # Zmień głębię jasności na 5 bitów (64 poziomy)
            bit_depth = 64
            sample = sample.point(lambda x: int(x * (bit_depth - 1) / 255))  # konwersja wartości pikseli z 0-255 na 0-63

            # zapisz próbkę do pliku
            filename = f'concrete_sample_{i_c}.png'
            sample.save(path_concrete_direction+filename)
            i_c = i_c+1
    width, height = img_wood.size

    # oblicz liczbę próbek w poziomie i w pionie
    num_samples_x = width // width_cut
    num_samples_y = height // height_cut


    i_w = 0
    # przejdź przez wszystkie próbki i wytnij je
    for y in range(num_samples_y):
        for x in range(num_samples_x):
            # wytnij próbkę o wymiarach 128x128 pikseli
            left = x * width_cut
            upper = y * height_cut
            right = left + width_cut
            lower = upper + height_cut
            sample = img_wood.crop((left, upper, right, lower))

            # Przekształć obraz do skali szarości
            sample = sample.convert('L')

            # Zmień głębię jasności na 5 bitów (64 poziomy)
            bit_depth = 64
            sample = sample.point(lambda x: int(x * (bit_depth - 1) / 255))  # konwersja wartości pikseli z 0-255 na 0-63

            # zapisz próbkę do pliku
            filename = f'wood_sample_{i_w}.png'
            sample.save(path_wood_direction + filename)
            i_w = i_w + 1
    width, height = img_brick.size

    # oblicz liczbę próbek w poziomie i w pionie
    num_samples_x = width // width_cut
    num_samples_y = height // height_cut

    i_b = 0
    # przejdź przez wszystkie próbki i wytnij je
    for y in range(num_samples_y):
        for x in range(num_samples_x):
            # wytnij próbkę o wymiarach 128x128 pikseli
            left = x * width_cut
            upper = y * height_cut
            right = left + width_cut
            lower = upper + height_cut
            sample = img_brick.crop((left, upper, right, lower))

            # Przekształć obraz do skali szarości
            sample = sample.convert('L')

            # Zmień głębię jasności na 5 bitów (64 poziomy)
            bit_depth = 64
            sample = sample.point(lambda x: int(x * (bit_depth - 1) / 255))  # konwersja wartości pikseli z 0-255 na 0-63

            # zapisz próbkę do pliku
            filename = f'brick_sample_{i_b}.png'
            sample.save(path_brick_direction + filename)
            i_b = i_b + 1
    return 0

crop_image(128, 128)


extensions = (".jpg", ".jpeg", ".png")
file_list = [file for file in os.listdir(path_concrete_direction) if file.endswith(extensions)]


with open(r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_1_concrete\concretecsv.csv", mode='w', newline='') as plik_csv:
    writer = csv.writer(plik_csv)

    # zapisz nagłówki
    writer.writerow(['Odleglosc', 'Kierunek','Kategoria', 'dissimilarity', 'correlation', 'contrast', 'energy', 'homogeneity', 'ASM'])

    for file_name in file_list:
        file_path = os.path.join(path_concrete_direction, file_name)
        concrete_sample = io.imread(file_path, as_gray=True)

        # Określ odległości i kierunki GLCM
        distances = [1, 3, 5]
        angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]

        glcm = {}
        for d in distances:
            for a in angles:
                glcm[(d, a)] = feature.graycomatrix(concrete_sample, distances=[d], angles=[a])


        features = {}

        for key in glcm:
            d, a = key
            features[key] = {"category": 'concrete',
                             "dissimilarity": feature.graycoprops(glcm[key], 'dissimilarity')[0][0],
                             "correlation": feature.graycoprops(glcm[key], 'correlation')[0][0],
                             "contrast": feature.graycoprops(glcm[key], 'contrast')[0][0],
                             "energy": feature.graycoprops(glcm[key], 'energy')[0][0],
                             "homogeneity": feature.graycoprops(glcm[key], 'homogeneity')[0][0],
                             "ASM": feature.graycoprops(glcm[key], 'ASM')[0][0]}

        wiersz = []

        for key in features:
            #print("Odległość: {}, Kierunek: {}".format(key[0], key[1]))
            wiersz.append(key[0])
            wiersz.append(key[1])
            for k in features[key]:
                #print("{}: {}".format(k, features[key][k]))
                wiersz.append(features[key][k])
            writer.writerow(wiersz)
            wiersz.clear()


file_list = [file for file in os.listdir(path_wood_direction) if file.endswith(extensions)]

with open(r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_2_oak_wood\woodcsv.csv", mode='w', newline='') as plik_csv:
    writer = csv.writer(plik_csv)

    # zapisz nagłówki
    writer.writerow(['Odleglosc', 'Kierunek','Kategoria', 'dissimilarity', 'correlation', 'contrast', 'energy', 'homogeneity', 'ASM'])

    for file_name in file_list:
        file_path = os.path.join(path_wood_direction, file_name)
        wood_sample = io.imread(file_path, as_gray=True)

        # Określ odległości i kierunki GLCM
        distances = [1, 3, 5]
        angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]

        glcm = {}
        for d in distances:
            for a in angles:
                glcm[(d, a)] = feature.graycomatrix(wood_sample, distances=[d], angles=[a])


        features = {}

        for key in glcm:
            d, a = key
            features[key] = {"category": 'wood',
                             "dissimilarity": feature.graycoprops(glcm[key], 'dissimilarity')[0][0],
                             "correlation": feature.graycoprops(glcm[key], 'correlation')[0][0],
                             "contrast": feature.graycoprops(glcm[key], 'contrast')[0][0],
                             "energy": feature.graycoprops(glcm[key], 'energy')[0][0],
                             "homogeneity": feature.graycoprops(glcm[key], 'homogeneity')[0][0],
                             "ASM": feature.graycoprops(glcm[key], 'ASM')[0][0]}

        wiersz = []

        for key in features:
            #print("Odległość: {}, Kierunek: {}".format(key[0], key[1]))
            wiersz.append(key[0])
            wiersz.append(key[1])
            for k in features[key]:
                #print("{}: {}".format(k, features[key][k]))
                wiersz.append(features[key][k])
            writer.writerow(wiersz)
            wiersz.clear()



file_list = [file for file in os.listdir(path_brick_direction) if file.endswith(extensions)]

with open(r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_3_brick\brickcsv.csv", mode='w', newline='') as plik_csv:
    writer = csv.writer(plik_csv)

    # zapisz nagłówki
    writer.writerow(['Odleglosc', 'Kierunek','Kategoria', 'dissimilarity', 'correlation', 'contrast', 'energy', 'homogeneity', 'ASM'])

    for file_name in file_list:
        file_path = os.path.join(path_brick_direction, file_name)
        brick_sample = io.imread(file_path, as_gray=True)

        # Określ odległości i kierunki GLCM
        distances = [1, 3, 5]
        angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]

        glcm = {}
        for d in distances:
            for a in angles:
                glcm[(d, a)] = feature.graycomatrix(brick_sample, distances=[d], angles=[a])


        features = {}

        for key in glcm:
            d, a = key
            features[key] = {"category": 'brick',
                             "dissimilarity": feature.graycoprops(glcm[key], 'dissimilarity')[0][0],
                             "correlation": feature.graycoprops(glcm[key], 'correlation')[0][0],
                             "contrast": feature.graycoprops(glcm[key], 'contrast')[0][0],
                             "energy": feature.graycoprops(glcm[key], 'energy')[0][0],
                             "homogeneity": feature.graycoprops(glcm[key], 'homogeneity')[0][0],
                             "ASM": feature.graycoprops(glcm[key], 'ASM')[0][0]}

        wiersz = []

        for key in features:
            #print("Odległość: {}, Kierunek: {}".format(key[0], key[1]))
            wiersz.append(key[0])
            wiersz.append(key[1])
            for k in features[key]:
                #print("{}: {}".format(k, features[key][k]))
                wiersz.append(features[key][k])
            writer.writerow(wiersz)
            wiersz.clear()

