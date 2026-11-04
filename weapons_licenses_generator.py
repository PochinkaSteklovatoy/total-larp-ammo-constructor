from datetime import datetime, timedelta
import random
import csv


notes_amt = 1000

firearm_types = ['Гладкоствольное длинноствольное', 'С нарезным стволом', 'Комбинированное']
state_types = ['Выдано', 'Аннулировано']

firearm_weights = [59, 37, 4]
state_weights = [95, 5]

#Генерация случайных дат
start_date = datetime(1993, 5, 20)
end_date = datetime(2026, 12, 31)
delta_days = (end_date - start_date).days
random_offsets = random.choices(range(delta_days + 1), k=notes_amt)

dates = [start_date + timedelta(days=offset) for offset in random_offsets]


firearms = random.choices(firearm_types, weights=firearm_weights, k=notes_amt)
note_ids = random.choices(range(0, notes_amt*10000), k=notes_amt)
states = random.choices(state_types, weights=state_weights, k=notes_amt)

print(note_ids[0], states[0], firearms[0], dates[0].strftime('%Y-%m-%d'))
with open("datasets_for_analysis/generated_weapons_licenses_data.csv", "w", newline="", encoding='utf-8-sig') as file_output:
    writer = csv.writer(file_output, delimiter=";")
    for i in range(notes_amt):
        writer.writerow([note_ids[i], states[i], firearms[i], dates[i].strftime('%Y-%m-%d')])