import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
ds = pd.read_csv(r"D:\Тютин\работы\anime.csv")
ind = range(1, 11)

# Измененные столбцы
name = ds['name'].head(5)
episodes = ds['episodes'].head(5)
rating = ds['rating'].head(5)
members = ds['members'].head(5)
# Линейные графики
plt.figure(figsize=(10, 5))
plt.plot(name, episodes)
plt.title('Линейный график - эпизоды')
plt.xlabel('Название')
plt.ylabel('Эпизоды')
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(name, rating)
plt.title('Линейный график - рейтинг')
plt.xlabel('Название')
plt.ylabel('Рейтинг')
plt.show()

# Столбчатые диаграммы (3 штуки)
plt.figure(figsize=(10, 5))
plt.bar(name, members)
plt.title('Столбчатая диаграмма 1')
plt.xlabel('Название')
plt.ylabel('Мемберс')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(name, episodes)
plt.title('Столбчатая диаграмма 2')
plt.xlabel('Имя')
plt.ylabel('Серии')
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(name, rating, label='Диаграмма 3')
plt.title('Столбчатая диаграмма 3')
plt.xlabel('Имя!')
plt.ylabel('ратинг')
plt.show()

# Круговые диаграммы (2 штуки)
plt.figure(figsize=(10, 5))
place_counts = episodes.value_counts()
place_counts.plot.pie(autopct='%1.1f%%')
plt.title('Серии')
plt.show()

plt.figure(figsize=(10, 5))
rating_counts = rating.value_counts()
rating_counts.plot.pie(autopct='%1.1f%%')
plt.title('Рейтинг')
plt.show()

# Диаграммы рассеяния (2 штуки)
plt.figure(figsize=(10, 5))
plt.scatter(name, episodes)
plt.title('Диаграмма рассеяния 1')
plt.xlabel('Нейм')
plt.ylabel('Эпизодес')
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(name, rating)
plt.title('Диаграмма рассеяния 2')
plt.xlabel('Name')
plt.ylabel('Reiting')
plt.show()

# Гистограммы (3 штуки)
plt.figure(figsize=(10, 5))
plt.hist(rating, bins=20, edgecolor='black')
plt.title('Гистограмма 1')
plt.xlabel('Место')
plt.ylabel('Частота')
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(episodes, bins=20, edgecolor='black')
plt.title('Гистограмма 2')
plt.xlabel('Время прохождения')
plt.ylabel('Частота')
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(members, bins=20, edgecolor='black')
plt.title('Гистограмма 3')
plt.xlabel('Проверено')
plt.ylabel('Частота')
plt.show()
