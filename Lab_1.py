
from scipy.stats import norm
from _csv import writer
import random
import math

random.seed(a='qwerty', version=2)

def cloud_generator(surface, max_x , max_y, max_z, r, num_points):
    x=[]
    y=[]
    z=[]
    match surface:
        # generowanie chmury punktów w plaszczyznie x - y
        case 'horizontal':
            for i in range(num_points):
                x.append(random.random()*max_x)
                y.append(random.random()*max_y)
                z.append(0)
            points = zip(x, y, z)
            return points
        # generowanie chmury punktów w plaszczyznie x - z
        case 'vertical':
            for i in range(num_points):
                x.append(random.random()*max_x)
                y.append(0)
                z.append(random.random()*max_z)
            points = zip(x, y, z)
            return points
        # generowanie chmury punktów w ksztalcie cylindra
        case 'cylinder':
            for i in range(num_points):
                degree=random.random()*360
                x.append(r*math.cos(math.radians(degree)))
                y.append(r*math.sin(math.radians(degree)))
                z.append(random.random()*max_z)
            points = zip(x, y, z)
            return points
        # w przypadku zlego parametru surface wyrzuca chmure o parametrach 0,0,0
        case _:
            points = zip(x, y, z)
            return points

# To samo co wyzej tylko razem
def three_cloud_generator(max_x , max_y, max_z, r, num_points):
    x = []
    y = []
    z = []
    for i in range(num_points):
        x.append(10+random.random() * max_x)
        y.append(10+random.random() * max_y)
        z.append(0)

    for i in range(num_points):
        x.append(random.random() * max_x)
        y.append(0)
        z.append(random.random() * max_z)

    for i in range(num_points):
        degree = random.random() * 360
        x.append(r * math.cos(math.radians(degree))-30)
        y.append(r * math.sin(math.radians(degree)))
        z.append(random.random() * max_z)

    points = zip(x, y, z)
    return points

punkty = three_cloud_generator(max_x=100.0,max_y=20.0,num_points=400,max_z=-10,r=5)

# Zapisywanie do pliku csv wygenerowanej chmury punktow
with open('Przykladowedane.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
    csvwriter = writer(csvfile)
    for p in punkty:
        csvwriter.writerow(p)

