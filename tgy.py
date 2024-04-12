import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из xsls таблицы
df = pd.read_excel('list of cases.xlsx')

#Создание диаграммы для категории
category_counts = df['Категория'].value_counts()
category_counts.plot(kind='barh', stacked='True', title='Количество дел в разных категориях с 31.12.2023г. по 30.03.2024г.')
plt.show()

# Создание диаграммы для статуса
status_counts = df['Статус'].value_counts()
status_counts.plot(kind='pie', title='Распределение дел по статусам с 31.12.2023г. по 30.03.2024г.')
plt.show()

#Показатели эффективности юристов
lawyers=df['Исполнитель'].value_counts()
lawyers.plot(kind='barh', stacked='True' , title='Распределение по количеству дел с декабря 2023 года по март 2024' )
plt.show()

#Показатели, какими категориями дел занимались те или иные юристы
import seaborn as sns
sns.scatterplot(data=df, x='Статус',y='Организация заказчика').set (title='Активность организаций заявителей с декабря 2023 года по март 2024')
plt.show()