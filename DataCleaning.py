import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Book6.csv')
X1 = dataset.iloc[4:, 0].values
X = dataset.iloc[1:36, 1:10:2].values
y = dataset.iloc[1:36, 2:11:2].values
z = dataset.iloc[1:36, 11:].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'median', axis = 0)
imputer = imputer.fit(X[:,0:])
X[:, 0:] = imputer.transform(X[:, 0:])
imputer = imputer.fit(y[:,0:])
y[:, 0:] = imputer.transform(y[:, 0:])
imputer = imputer.fit(z[:,0:])
z[:, 0:] = imputer.transform(z[:, 0:])

import pickle
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

filename = "Book6_copy.csv"
pickle.dump(regressor, open(filename, 'wb'))

y_pred = regressor.predict(X_test)
print('Linear Regression R squared": %.4f' % regressor.score(X_test, y_test))

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Disease cases vs deaths(Training set)')
plt.xlabel('Cases')
plt.ylabel('Death')
plt.show()

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Disease cases vs deaths(Test set)')
plt.xlabel('Cases')
plt.ylabel('Death')
plt.show()

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[1].hist(z[:, 0], bins=None)

labels = 'Acute Diarrhoeal', 'Malaria', 'Acute Respiratory', 'Japanese Encephalitis', 'Viral Hepatitis'
state = input("Enter the State: ")
index = np.where(X1 == state)

size = y[index].astype(int)
sizes=[]
for i in range(5):
    sizes.append(size[0,i])
labels = list(labels)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()

fig.savefig('pie_chart.png')

print("Doctors Avaliable: ",end=" ")
print(z[int(index[0]), 0])
