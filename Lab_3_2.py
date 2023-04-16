import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# wczytanie pliku CSV
df = pd.read_csv(r'/Python/Teksture_1_concrete/concretecsv.csv', usecols=[0])

y = np.ravel(df.values.tolist())

df = pd.read_csv(r'/Python/Teksture_1_concrete/concretecsv.csv', usecols=[3, 4, 5, 6, 7, 8])

x = df.values.tolist()

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)

# Definicja modelu KNN i trenowanie go na zbiorze treningowym
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Klasyfikacja wektorów cech ze zbioru testowego
y_pred = model.predict(X_test)

# Obliczenie dokładności klasyfikacji
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokładność klasyfikacji dla concrete: {accuracy:.2f}")

# wczytanie pliku CSV
df = pd.read_csv(r'/Python/Teksture_2_oak_wood/woodcsv.csv', usecols=[0])

y = np.ravel(df.values.tolist())

df = pd.read_csv(r'/Python/Teksture_2_oak_wood/woodcsv.csv', usecols=[3, 4, 5, 6, 7, 8])

x = df.values.tolist()

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)

# Definicja modelu KNN i trenowanie go na zbiorze treningowym
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Klasyfikacja wektorów cech ze zbioru testowego
y_pred = model.predict(X_test)

# Obliczenie dokładności klasyfikacji
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokładność klasyfikacji dla wood: {accuracy:.2f}")

# wczytanie pliku CSV
df = pd.read_csv(r'/Python/Teksture_3_brick/brickcsv.csv', usecols=[0])

y = np.ravel(df.values.tolist())

df = pd.read_csv(r'/Python/Teksture_3_brick/brickcsv.csv', usecols=[3, 4, 5, 6, 7, 8])

x = df.values.tolist()

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)

# Definicja modelu KNN i trenowanie go na zbiorze treningowym
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Klasyfikacja wektorów cech ze zbioru testowego
y_pred = model.predict(X_test)

# Obliczenie dokładności klasyfikacji
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokładność klasyfikacji dla brick: {accuracy:.2f}")
