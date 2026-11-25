import pandas as pd
import matplotlib.pyplot as plt

csv_in_path = '../datasets/ammo_parts_companies_rosgvardia.csv'
image_out_path = '../images/сompanies_dynamics_by_year.png'

licences = pd.read_csv(
    csv_in_path,
    sep=';',              # разделитель — точка с запятой
    quotechar='"',        # кавычки как ограничитель строк
    doublequote=True,     # "" внутри значения = экранированная кавычка
    encoding='utf-8',     # или 'cp1251', если utf-8 не сработает
    header=None,          # в файле нет строки заголовка
    dtype=str,            # всё читаем как строки, чтобы не терять ведущие нули
    keep_default_na=False # пустые поля остаются '', а не NaN
)
# print(licences.shape)          # должно быть (N, 26) — 26 полей
# print(licences.iloc[0])        # посмотреть первую строку

# индексы
# 2	issue_date	дата выдачи лицензии
# 3	status	статус (Действует / Признана лицензией… / Прекращена / Аннулирована)
# 11	inn	ИНН (уникальный идентификатор компании)
# 17	event_date_1	дата события (часто дата прекращения/аннулирования)
# 24	event_date_2	вторая дата события (резерв/дубль)

# print(licences.iloc[:,[2,3]].head())
active_criteria = ['Действует',
                   'Признана лицензией на вид деятельности, указанный в пункте '
                   '9.1 части 1 статьи 12 Федерального закона от 04.05.2011 № 99-ФЗ']
inactive_criteria = ['Прекращена', 'Аннулирована']

licences = licences.astype({licences.columns[2]: object})
licences.iloc[:, 2] = pd.to_datetime(licences.iloc[:, 2],format='%d.%m.%Y', errors='coerce').dt.year

active_licences = licences.loc[licences.iloc[:, 3].isin(active_criteria)].iloc[:, [2,3]]
inactive_licences = licences.loc[licences.iloc[:, 3].isin(inactive_criteria)].iloc[:, [2,3]]

active_by_year = active_licences.groupby(active_licences.iloc[:, 0]).size()
inactive_by_year = inactive_licences.groupby(inactive_licences.iloc[:, 0]).size()

diff = active_by_year.subtract(inactive_by_year, fill_value=0).sort_index()
print(diff)

print(active_by_year, inactive_by_year)

active_by_year.plot(figsize=(12, 5), label='Создано')
inactive_by_year.plot(figsize=(12, 5), label='Закрыто')
plt.xlabel('Год')
plt.ylabel('Количество компаний')
plt.title('Созданные и закрытые компании по годам')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(image_out_path , dpi=150)
plt.show()
