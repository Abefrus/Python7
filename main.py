import pandas as pd

ggl = pd.read_csv("GoogleApps.csv")

print('Задання a:')
print("Назва додатку який знаходиться першим в списку:", ggl['App'].head(1))

print('Задання b:')
print("Категорія додатку що знаходиться останнім в списку:",ggl['Category'].tail(1))

print('Задання c:')
print("кількість стовпців:", ggl.shape)

print('Задання d:')
print("Середнє арифметичне:", ggl['Size'].mean(),", медіана:", ggl['Size'].median())

print('Задання e:')
max_reviews_index = ggl['Reviews'].idxmax()

print("Категорія додатку з найбільшою кількістю відгуків:", ggl['Category'].loc[max_reviews_index])

print('Задання f:')
filtered_apps = ggl[(ggl['Price'] > 20) & (ggl['Installs'] > 10000)]

print("Середнє арифметичне рейтингу додатків понад 20 долярів і більше 10000 завантажень:", filtered_apps['Rating'].mean())
