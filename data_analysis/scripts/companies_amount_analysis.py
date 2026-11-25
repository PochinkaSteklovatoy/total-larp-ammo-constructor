import pandas as pd
import matplotlib.pyplot as plt

csv_in_path = '../datasets/ammo_parts_companies_datagov.csv'
image_out_path = '../images/companies_created_by_year.png'

licences = pd.read_csv(
    csv_in_path,
    sep=',',              # разделитель — запятая
    encoding='utf-8',     # или 'cp1251', если utf-8 не сработает
    keep_default_na=False # пустые поля остаются '', а не NaN
)

print("COLUMNS:", licences.columns.tolist())
print("SHAPE:", licences.shape)
print("HEAD:\n", licences.head(2))

licences['Дата начала действия'] = pd.to_datetime(licences['Дата начала действия'],format='%d-%m-%Y', errors='coerce').dt.year
amount_by_year = licences.groupby(licences['Дата начала действия']).size()
total_amount = licences.shape[0]

print(amount_by_year)

amount_by_year.plot(kind='bar', figsize=(12, 5))
plt.xlabel('Год')
plt.ylabel('Количество компаний')
plt.title(f'Кол-во созданных компаний по годам, всего {total_amount}')
plt.grid()
plt.tight_layout()
plt.savefig(image_out_path, dpi=150)
plt.show()
