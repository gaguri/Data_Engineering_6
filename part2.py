import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/root/lab6/new_file_lab6.csv')
data_filled = data.fillna('Unknown')

genre_counts = data_filled['genre'].value_counts()
plt.figure(figsize=(10, 5))
plt.bar(genre_counts.index, genre_counts.values)
plt.title('Распределение жанров')
plt.xlabel('Жанры')
plt.ylabel('Количество')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('/root/lab6/fig1.png')

rock_df = data_filled[data_filled['genre'] == 'Rock']
artist_counts = rock_df['artist_name'].value_counts().head(10)
plt.figure(figsize=(8, 8))
plt.pie(artist_counts, labels=artist_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Топ-10 исполнителей в жанре рок')
plt.tight_layout()
plt.savefig('/root/lab6/fig2.png')

classical_df = data_filled[data_filled['genre'] == 'Classical']
artist_counts = classical_df['artist_name'].value_counts().head(10)
plt.figure(figsize=(8, 8))
plt.pie(artist_counts, labels=artist_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Топ-10 исполнителей в жанре классика')
plt.tight_layout()
plt.savefig('/root/lab6/fig3.png')

data_dropped1 = data_filled[data_filled['company_name'] != 'Unknown']
company_label_counts = data_dropped1.groupby('company_name')['label_name'].nunique().sort_values(ascending=False)
top_companies = company_label_counts.head(5)
plt.figure(figsize=(10, 6))
plt.barh(top_companies.index, top_companies.values)
plt.title('Топ-5 компаний по количеству лейблов')
plt.xlabel('Количество уникальных лейблов')
plt.ylabel('Компания')
plt.tight_layout()
plt.savefig('/root/lab6/fig4.png')

data_dropped2 = data_filled[data_filled['release_date'] != 'Unknown']
release_trends = data_dropped2['release_date'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.xlim(1850, 2024)
plt.plot(release_trends.index, release_trends.values, marker='o', linestyle='-', color='blue')
plt.title('Количество релизов по годам')
plt.xlabel('Год')
plt.ylabel('Количество релизов')
plt.grid(True)
plt.tight_layout()
plt.savefig('/root/lab6/fig5.png')