import pandas as pd
import matplotlib.pyplot as plt

csv_in_path = '../datasets/generated_weapons_licenses_data.csv'
image_out_path = '../images/firearm_licences_by_type.png'

licences = pd.read_csv(csv_in_path, sep=';', encoding='utf-8', keep_default_na=False, header = None)

rifle_amt = (licences.iloc[:,2] == 'Гладкоствольное длинноствольное').sum()
smoothbore_amt = (licences.iloc[:,2] == 'С нарезным стволом').sum()
combined_amt = (licences.iloc[:,2] == 'Комбинированное').sum()

amts = [rifle_amt, smoothbore_amt, combined_amt]
print(amts)

labels = ['Гладкоствольное длинноствольное', 'С нарезным стволом', 'Комбинированное']

plt.pie(amts, labels=labels)
plt.savefig(image_out_path, dpi=150)
plt.show()
