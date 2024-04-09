# -*- coding: utf-8 -*-
"""Project Mining

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MuwuILvWx-5rNxHg3c_jdrIGbThtvG93

# **Logistic Regression**
"""

# Commented out IPython magic to ensure Python compatibility.
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
sns.set(style="white", color_codes=True)

iris = pd.read_csv("/content/Iris.csv")
print(iris.head())

iris["Species"].value_counts()

iris = sns.load_dataset('iris')

sns.FacetGrid(iris, hue="species", height=6).map(plt.scatter, "petal_length", "sepal_width").add_legend()

plt.show()

"""## **Prepare and Summary**"""

# Load the iris dataset from the CSV file
iris = pd.read_csv("/content/Iris.csv")

# Mapping dictionary
flower_mapping = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
iris["species"] = iris["Species"].map(flower_mapping)

print(iris.head())

# Preparing inputs and Split data
X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
y = iris[['Species']].values

sc = StandardScaler()
x_std = sc.fit_transform(X)
class_names, y = np.unique(iris['Species'],return_inverse=True)
class_names

X_train,X_test,y_train,y_test = train_test_split(x_std,y,test_size=0.3,random_state=22)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X, y)

# Accuracy
print(f"Accuracy Score : {model.score(X,y)}")

model_logistic = LogisticRegression()
model_logistic.fit(X_train,y_train)

from sklearn.metrics import accuracy_score, classification_report

y_pred = model_logistic.predict(X_test)
print('-------Classification--------')
print(classification_report(y_test, y_pred))

# Regularization
model = LogisticRegression(C=20,penalty='l2' )
print(model.fit(X,y))

print(f"Accuracy : {model.score(X,y)}")

"""# **Decision Tree**"""

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris = pd.read_csv("/content/Iris.csv")
iris

X_trainset, X_test, y_trainset, y_test = train_test_split(X, y, test_size=0.3, random_state=3)

"""## **Model**"""

SpeciesTree = DecisionTreeClassifier(criterion="entropy", max_depth=4)

SpeciesTree.fit(X_trainset, y_trainset)

"""## **Prediction**"""

predTree = SpeciesTree.predict(X_trainset)

# Check Model
from sklearn import metrics
import matplotlib.pyplot as plt

print("Decision Accuracy : ", metrics.accuracy_score(y_trainset, predTree))

"""## **Visualization**"""

from sklearn import tree

fn = iris.columns[1:5]
cn = iris["Species"].unique().tolist()
SpeciesTree.fit(X, y)

fig, axs = plt.subplots(nrows=1, ncols=1, figsize= (8,8), dpi=300)

tree.plot_tree(SpeciesTree, feature_names=fn, class_names=cn, filled=True)

# New data to predict
# Class = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}

X_new = [[6.3, 3, 1.2, 0.2]]

predTree = SpeciesTree.predict(X_new)
predTree

"""# **Naive Bayes Classifier**"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv("/content/Iris.csv")

x = iris.iloc[:, :-1].values
y = iris.iloc[:, -1].values

# Defining the Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB(fit_prior = False)

mnb.fit(x, y)

# Prediction
y_pred = mnb.predict(x)
print(y_pred)

"""## **Plot a Confusion Matrix**"""

from sklearn.metrics import confusion_matrix

confusion_mat = confusion_matrix(y, y_pred)
labels = ['Setosa', 'Versicolor', 'Virginica']
sns.heatmap(confusion_mat, annot=True, cmap='magma', xticklabels=labels, yticklabels=labels)

plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion matrix")
plt.show()

# Accuracy
from sklearn.metrics import accuracy_score

print(f"Accuracy Score : {accuracy_score(y, y_pred)}")