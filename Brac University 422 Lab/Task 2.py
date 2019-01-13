import pandas as pd

table_data= {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
            'score': [12.5, 9, 16.5, 2.3, 9, 20, 14.5, 4.5, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}



table = pd.DataFrame(table_data)
print(table)


table.loc[table['qualify'] == 'yes', 'qualify'] = 1;
table.loc[table['qualify'] == 'no', 'qualify'] = 0;

print(table)