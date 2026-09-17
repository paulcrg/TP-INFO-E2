#Crémoux Guiblain Paul - E2 Dijon
#TP 02 - Collections

#Exercice 01

import copy
def ex01():
    a = ['a']
    b = a[:] #--> copy classique à 1 dim
    b = a.copy() #--> copy classique à 1 dim
    b = copy.deepcopy(a) #--> copy complete de toutes les dim
    b[0] = 1
    print(a)
    print(b)

#Exercice 02

#Enoncé

classDict = {
 "class": {
 "student": {
 "name": "Mike",
 "marks": {
 "physics": 70,
 "history": 80
 }
 }
 }
}

#Q1
print(classDict['class']['student']['name'])
#Q2
grade = classDict['class']['student']['marks']['physics'] = 89
#Q3
classDict["class"]["student"]["average"] = (
    sum(classDict["class"]["student"]["marks"].values())
    / len(classDict["class"]["student"]["marks"])
)
#Q4
classDict["class"]["student"] = [classDict["class"]["student"]]
#Q5
classDict["class"]["student"].append({"name": "Ted" ,
    "marks": {
        "physics": 34,
        "history": 99
    }
}
)
#Q6
teddy = 0
for notes in classDict["class"]["student"][1]["marks"].values():
    teddy += notes
print(teddy/len(classDict["class"]["student"][1]["marks"].values()))
#Q7
comptall = 0
comptlen = 0
for std in classDict["class"]["student"]:
    for grades in std["marks"].values():
        comptall += grades
        comptlen += 1

classDict["class"]["average_grade"] = comptall/comptlen

#Q8
print(classDict)