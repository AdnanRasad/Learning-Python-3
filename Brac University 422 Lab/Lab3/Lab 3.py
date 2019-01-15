

import pandas as pd

data = pd.read_csv('diabetes.csv')
print(data)




X = data.iloc[:, :].values #: : MEANS ALL ROWS ALL COLL
from sklearn import preprocessing


X[:, 8] = preprocessing.LabelEncoder().fit_transform(X[:, 8])


Y = pd.DataFrame(X)
print(Y)

#After Printing the second table we can see that 'Yes' is represented by 1 and 'No' is represented by '0'
