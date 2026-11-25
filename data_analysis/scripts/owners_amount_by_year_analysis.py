import pandas as pd
import matplotlib.pyplot as plt

csv_in_path = '../datasets/civilian_firearms_owners_by_year.csv'
image_out_path = '../images/firearm_owners_by_year.png'

owners = pd.read_csv(
    csv_in_path,
    sep=';',
    encoding='utf-8',
    header=None,
    names=['year', 'owners'],
    dtype={'year': int, 'owners': float}
)

print(owners)
plt.plot(owners['year'], owners['owners'])
plt.xlabel('Год')
plt.ylabel('Количество владельцев')
plt.title('Количество владельцев гражданского орудия в РФ, млн. чел.')
plt.grid()
plt.savefig(image_out_path, dpi=150)
plt.show()