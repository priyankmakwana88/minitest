#!/usr/bin/env python3

from sklearn import tree

#DATA-SET CREATION
#WEIGHT 1st attribute : TEXTURE_FACTOR (0 to 1) defined as 2nd attribute of a list

fruit_feature = [[130,0.2],[120,0.19],[135,0.35],[140,0.21],[110,0.12],[160,0.52],[155,0.50],[142,0.61],[151,0.66],[112,0.78],[119,0.44],[172,0.54],[153,0.22],[124,0.21],[135,0.32],[186,0.44],[147,0.23],[168,0.56],[129,0.65],[190,0.7]]

fruit_name = [["apple"],["apple"],["apple"],["apple"],["apple"],["orange"],["orange"],["orange"],["orange"],["orange"],["orange"],["orange"],["apple"],["apple"],["apple"],["orange"],["apple"],["orange"],["orange"],["orange"]]

#INITIALIZE CLASSIFIER
tree_classifier=tree.DecisionTreeClassifier()

#TRAINING THE SYSTEM
trained_data=tree_classifier.fit(fruit_feature,fruit_name)

#PREDICT THE OUTPUT
user_ip_wt=input("Enter weight of fruit : ")
user_ip_tf=input("Enter texture factor of fruit : ")
ip_feature=[user_ip_wt,user_ip_tf]
result=trained_data.predict([ip_feature])
print(result)
