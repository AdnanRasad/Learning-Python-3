import pandas as pd #WE USE THIS LIBRERY 'PANDAS' SO THAT WE CAN USE ONE OF ITS FUNCTION: DATAFRAME
import numpy as np

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }


df1 = pd.DataFrame(dict)
print(df1)


print();
print();

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, 2.3, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']






df = pd.DataFrame(exam_data , index=labels)
print (df)

print();
print();

'''For our data set B, df_B.loc["b"] will result in all the second row being selected.
df_A.iloc[0] and df_B.iloc[0], both will give you the first row of the data set.
.ix[] is the more flexible option. It accepts label based or index positional arguments.'''

'''
if df['qualify'] == 'Yes':
      df['qualify'] = df['qualify'] = 1
else:
      df['qualify'] = df['qualify'] = 0
      https://medium.com/jbennetcodes/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e
'''

df.loc[df['qualify'] == 'yes', 'qualify'] = 1;
df.loc[df['qualify'] == 'no', 'qualify'] = 0;

print(df)