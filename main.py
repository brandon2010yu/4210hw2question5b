# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

# reading the training data
# --> add your Python code here
db = []

with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
# transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# --> add your Python code here
# X =
Sunny = 1
Overcast = 2
Rain = 3
Hot = 1
Mild = 2
Cool = 3
High = 1
Normal = 2
Weak = 1
Strong = 2
X = [[1, 1, 1, 1], [1, 1, 1, 2], [2, 1, 1, 1], [3, 2, 1, 1], [3, 3, 2, 1], [3, 3, 2, 2], [2, 3, 2, 2], [1, 2, 1, 1],
     [1, 3, 2, 1], [3, 2, 2, 1], [1, 2, 2, 2], [2, 2, 1, 2], [2, 1, 2, 1], [3, 2, 1, 2]]

# transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
# Y =
No = 1
Yes = 2
Y = [1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1]

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the data in a csv file
# --> add your Python code here
dt = []

with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dt.append(row)

# printing the header of the solution
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(
    15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

# use your test samples to make probabilistic predictions.
# --> add your Python code here
# -->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]

for i in dt:
    predicted1 = clf.predict_proba([[1, 1, 2, 1]])[0]
    predicted2 = clf.predict_proba([[1, 1, 2, 2]])[0]
    predicted3 = clf.predict_proba([[1, 3, 1, 1]])[0]
    predicted4 = clf.predict_proba([[2, 1, 1, 2]])[0]
    predicted5 = clf.predict_proba([[2, 3, 1, 1]])[0]
    predicted6 = clf.predict_proba([[2, 3, 1, 2]])[0]
    predicted7 = clf.predict_proba([[3, 2, 2, 2]])[0]
    predicted8 = clf.predict_proba([[3, 1, 2, 2]])[0]
    predicted9 = clf.predict_proba([[3, 1, 1, 1]])[0]
    predicted10 = clf.predict_proba([[3, 2, 1, 2]])[0]
confidence1 = predicted1[0]/ (predicted1[0] + predicted1[1])
confidence2 = predicted1[1] / (predicted1[1] + predicted1[0])
confidence3 = max(confidence1,confidence2)
if confidence3 == confidence1:
    play1 = "No"
else:
    play1 = "Yes"

confidence4 = predicted2[0]/ (predicted2[0] + predicted2[1])
confidence5 = predicted2[1] / (predicted2[1] + predicted2[0])
confidence6 = max(confidence4,confidence5)
if confidence6 == confidence4:
    play2 = "No"
else:
    play2 = "Yes"

confidence7 = predicted3[0]/ (predicted3[0] + predicted3[1])
confidence8 = predicted3[1] / (predicted3[1] + predicted3[0])
confidence9 = max(confidence7,confidence8)
if confidence9 == confidence7:
    play3 = "No"
else:
    play3 = "Yes"

confidence10 = predicted4[0]/ (predicted4[0] + predicted4[1])
confidence11 = predicted4[1] / (predicted4[1] + predicted4[0])
confidence12 = max(confidence10,confidence11)
if confidence12 == confidence10:
    play4 = "No"
else:
    play4 = "Yes"

confidence13 = predicted5[0]/ (predicted5[0] + predicted5[1])
confidence14 = predicted5[1] / (predicted5[1] + predicted5[0])
confidence15 = max(confidence13,confidence14)
if confidence15 == confidence13:
    play5 = "No"
else:
    play5 = "Yes"
confidence16 = predicted6[0]/ (predicted6[0] + predicted6[1])
confidence17 = predicted6[1] / (predicted6[1] + predicted6[0])
confidence18 = max(confidence16,confidence17)
if confidence18 == confidence16:
    play6 = "No"
else:
    play6 = "Yes"
confidence19 = predicted7[0]/ (predicted7[0] + predicted7[1])
confidence20 = predicted7[1] / (predicted7[1] + predicted7[0])
confidence21 = max(confidence19,confidence20)
if confidence21 == confidence19:
    play7 = "No"
else:
    play7 = "Yes"
confidence22 = predicted8[0]/ (predicted8[0] + predicted8[1])
confidence23 = predicted8[1] / (predicted8[1] + predicted8[0])
confidence24 = max(confidence22,confidence23)
if confidence24 == confidence22:
    play8 = "No"
else:
    play8 = "Yes"
confidence25 = predicted9[0]/ (predicted9[0] + predicted9[1])
confidence26 = predicted9[1] / (predicted9[1] + predicted9[0])
confidence27 = max(confidence25,confidence26)
if confidence27 == confidence25:
    play9 = "No"
else:
    play9 = "Yes"
confidence28 = predicted10[0]/ (predicted10[0] + predicted10[1])
confidence29 = predicted10[1] / (predicted10[1] + predicted10[0])
confidence30 = max(confidence28,confidence29)
if confidence30 == confidence28:
    play10 = "No"
else:
    play10 = "Yes"
playArray = [play1, play2, play3,play4,play5,play6,play7,play8,play9,play10]
confidenceArray = [confidence3,confidence6,confidence9, confidence12,confidence15,confidence18,confidence21,confidence24,confidence27,confidence30]
a = 0
for j in dt:

    print(j[0].ljust(15), j[1].ljust(15),j[2].ljust(12),j[3].ljust(14),j[4].ljust(
    17), playArray[a].ljust(10),confidenceArray[a] )
    a+=1






