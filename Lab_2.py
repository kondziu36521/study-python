import csv
import time
from _csv import reader
import random
import math

random.seed(a=time.gmtime()[5]+time.gmtime()[4]*60, version=2)

Array_point = [[], []]
three_points= []
V_a=[]
V_b=[]

# Funkcja tworzenia wektorów (odejmowanie wspolrzednych punktow)
def create_vector(point_A ,point_B):
    vector = []
    vector.append(point_A[0] - point_B[0])
    vector.append(point_A[1] - point_B[1])
    vector.append(point_A[2] - point_B[2])
    return vector

# Wczytanie wspolrzednych
with open('Przykladowedane.xyz', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        Array_point.append([float(row[0]), float(row[1]), float(row[2])])

print(len(Array_point))

# Losowanie trzech punktow z chmury
for i in range(3):
    three_points.append(int(random.random()*len(Array_point)-1))

print(Array_point[three_points[0]])
print(Array_point[three_points[1]])

V_a=create_vector(Array_point[three_points[0]], Array_point[three_points[1]])
V_b=create_vector(Array_point[three_points[1]], Array_point[three_points[2]])

print(V_a)
print(V_b)


# k-means


