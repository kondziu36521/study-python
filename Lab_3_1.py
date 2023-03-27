
from PIL import Image



def crop_image():

    img_size = [[0, 0], [0, 0], [0, 0]]
    count_image = []
    path_concrete = r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_1_concrete\concrete-texture.jpg"
    path_wood = r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_2_oak_wood\teksture_wood.png"
    path_brick = r"C:\Users\33kon\PycharmProjects\study-python\Python\Teksture_3_brick\brick_teksture.jpg"
    img_concrete = Image.open(path_concrete)
    img_wood=Image.open(path_wood)
    img_brick=Image.open(path_brick)

    width, height = img_concrete.size

    # oblicz liczbę próbek w poziomie i w pionie
    num_samples_x = width // 128
    num_samples_y = height // 128

    # przejdź przez wszystkie próbki i wytnij je
    for y in range(num_samples_y):
        for x in range(num_samples_x):
            # wytnij próbkę o wymiarach 128x128 pikseli
            left = x * 128
            upper = y * 128
            right = left + 128
            lower = upper + 128
            sample = img_concrete.crop((left, upper, right, lower))

            # zapisz próbkę do pliku
            filename = f'concrete_sample_{x}_{y}.png'
            sample.save(path_concrete+filename)

    width, height = img_wood.size

    # oblicz liczbę próbek w poziomie i w pionie
    num_samples_x = width // 128
    num_samples_y = height // 128

    # przejdź przez wszystkie próbki i wytnij je
    for y in range(num_samples_y):
        for x in range(num_samples_x):
            # wytnij próbkę o wymiarach 128x128 pikseli
            left = x * 128
            upper = y * 128
            right = left + 128
            lower = upper + 128
            sample = img_wood.crop((left, upper, right, lower))

            # zapisz próbkę do pliku
            filename = f'wood_sample_{x}_{y}.png'
            sample.save(path_wood + filename)

    width, height = img_brick.size

    # oblicz liczbę próbek w poziomie i w pionie
    num_samples_x = width // 128
    num_samples_y = height // 128

    # przejdź przez wszystkie próbki i wytnij je
    for y in range(num_samples_y):
        for x in range(num_samples_x):
            # wytnij próbkę o wymiarach 128x128 pikseli
            left = x * 128
            upper = y * 128
            right = left + 128
            lower = upper + 128
            sample = img_brick.crop((left, upper, right, lower))

            # zapisz próbkę do pliku
            filename = f'brick_sample_{x}_{y}.png'
            sample.save(path_brick + filename)
    return 0

print( crop_image() )
