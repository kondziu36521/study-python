import csv
import time
from _csv import reader
import random
import math

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.stats import norm
import numpy as np
import pyransac3d as pyrsc
from sklearn.cluster import DBSCAN
from sklearn import metrics


random.seed(a=time.gmtime()[5]+time.gmtime()[4]*60, version=2)

Array_point = [[0, 0, 0]]
Array_k_means = []

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

Array_point.pop(0)


def k_means_devide(num_iter, array):

    # k-means

    clusterer = KMeans(n_clusters=num_iter)
    
    lista = np.array(array)
    
    y_pred = clusterer.fit_predict(lista)
    
    groups = [[]]
    
    for j in range(num_iter):
        for i in range(len(array)):
            if y_pred[i] == j:
                groups.append(array[i]+[j])
    groups.pop(0)
    return groups

Array_k_means = k_means_devide(3, Array_point)


group_0 = []
group_1 = []
group_2 = []

for i in range(len(Array_k_means)):
    if Array_k_means[i][3] == 0:
        group_0.append(Array_k_means[i][:3])
    elif Array_k_means[i][3] == 1:
        group_1.append(Array_k_means[i][:3])
    elif Array_k_means[i][3] == 2:
        group_2.append(Array_k_means[i][:3])


print("Algorytm RANSAC z poradnika \n")

# Algorytm RANSAC

def RANSAC(num_iter, array, thresold):
    it = 0
    while it < num_iter:
            # Losowanie trzech punktow z chmury
        three_points = []
        for i in range(3):
            three_points.append(int(random.random()*len(array)))

        V_a = []
        V_b = []
        V_a=create_vector(array[three_points[0]], array[three_points[2]])
        V_b=create_vector(array[three_points[1]], array[three_points[2]])

        U_a = V_a/np.linalg.norm(V_a)
        U_b = V_b/np.linalg.norm(V_b)

        U_c = np.cross(U_a, U_b)

        D = -np.sum(np.multiply(U_c, array[three_points[2]]))

        distance_all_points = []

        for i in range(len(array)):
            distance_all_points.append(((U_c[0]*array[i][0] + U_c[1]*array[i][1] + U_c[2]*array[i][2]) + D)/np.linalg.norm(U_c))

        if it == 0:
            inliers = np.where(np.abs(distance_all_points) <= thresold)[0]
            U_c_max = U_c

        if len(inliers) <= len(np.where(np.abs(distance_all_points) <= thresold)[0]):
            inliers = np.where(np.abs(distance_all_points) <= thresold)[0]
            U_c_max = U_c
        it = it + 1

    print(U_c_max)

    if abs((sum(distance_all_points)/len(distance_all_points))) < 0.1:
        print("Chmura jest plaszczyzną")

        if abs(U_c_max[2]) < 0.001:
            print("Jest to płaszczyzna pionowa")
        else:
            print("Jest to płaszczyzna pozioma")

    else:
        print("Chmura nie jest plaszczyzną")

    print("\n")
    return 0

# print(distance_all_points)
# print(inliers)

RANSAC(3, group_0, 1)
RANSAC(3, group_1, 1)
RANSAC(3, group_2, 1)


print("PUNKT 6 OPCJA 1")

db = DBSCAN(eps=15, min_samples=100).fit(Array_point)
labels = db.labels_

group_0.clear()
group_1.clear()
group_2.clear()

for i in range(len(labels)):
    if labels[i] == 0:
        group_0.append(Array_point[i])
    elif labels[i] == 1:
        group_1.append(Array_point[i])
    elif labels[i] == 2:
        group_2.append(Array_point[i])


# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)

print("\n")

nump_array1 = np.array(group_0)
nump_array2 = np.array(group_1)
nump_array3 = np.array(group_2)


plane1 = pyrsc.Plane()
eq_1, inl_1 = plane1.fit(nump_array1, 0.1)
plane2 = pyrsc.Plane()
eq_2, inl_2 = plane2.fit(nump_array2, 0.1)
plane3 = pyrsc.Plane()
eq_3, inl_3 = plane3.fit(nump_array3, 0.1)


print(eq_1[:3])

if (abs(eq_1[1]) or abs(eq_1[2])) == 1.0:
    print("Chmura jest plaszczyzną")

    if abs(eq_1[2]) == 0.0:
        print("Jest to płaszczyzna pionowa")
    else:
        print("Jest to płaszczyzna pozioma")

else:
    print("Chmura nie jest plaszczyzną")

print("\n")

print(eq_2[:3])

if (abs(eq_2[1]) or abs(eq_2[2])) == 1.0:
    print("Chmura jest plaszczyzną")

    if abs(eq_2[2]) == 0.0:
        print("Jest to płaszczyzna pionowa")
    else:
        print("Jest to płaszczyzna pozioma")

else:
    print("Chmura nie jest plaszczyzną")

print("\n")

print(eq_3[:3])

if (abs(eq_3[1]) or abs(eq_3[2])) == 1:
    print("Chmura jest plaszczyzną")

    if abs(eq_3[2]) == 0.0:
        print("Jest to płaszczyzna pionowa")
    else:
        print("Jest to płaszczyzna pozioma")

else:
    print("Chmura nie jest plaszczyzną")


print("\n")
