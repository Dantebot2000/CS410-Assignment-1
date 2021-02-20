#-------------------------------------------------------------------------
# AUTHOR: Dante Martinez
# FILENAME: MartinezDante_DecisionTree.py
# SPECIFICATION: Creates a decision tree from data imported from a data table
# FOR: CS 4200- Assignment #1
# TIME SPENT: 30 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         #print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =
for j in db:
    print(j)
    if j[0] == "Young":
        a = 1
    elif j[0] == "Presbyopic":
        a = 2
    elif j[0] == "Prepresbyopic":
        a = 3
    if j[1] == "Myope":
        b = 1
    elif j[1] == "Hypermetrope":
        b = 2

    if j[2] == "Yes":
        c = 1
    elif j[2] == "No":
        c = 2

    if j[3] == "Normal":
        d = 1
    elif j[3] == "Reduced":
        d = 2

    X.append((a, b, c, d))

print(X)

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =
for j in db:
    if j[4] == "Yes":
        Y.append(1)
    elif j[4] == "No":
        Y.append(2)
#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()


