# Feature Extraction with RFE
import numpy as np
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import main
import train
# load data
team1ListW_FS = []
team2ListW_FS = []
findANameW_FS = []
last_line = []
new_answer = []
finalAttributeNumsT1W_FS = []
finalAttributeNumsT2W_FS = []
top_features = []
numOfFeatures = 8
percentagelist1 = []
percentagelist2 = []
indexOfTopFeatures = []
xy1list = []
xy2list = []
newxy1list = []
newxy2list = []
findANameW_WF = []
finalAttributeNumsT1W_WF = []
finalAttributeNumsT2W_WF = []
indices = []

def bulk2():
    url = "/Users/crystinrodrick/PycharmProjects/nfl3/fulltrainingdata.csv"
    #names = ['attr1', 'attr2', 'attr3', 'attr4', 'attr5', 'attr6', 'attr7', 'attr8', 'attr9', 'attr10',
    #         'attr11', 'attr12', 'attr13', 'attr14', 'attr15', 'class']
    names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "class"]
    dataframe = read_csv(url, names=names)
    array = dataframe.values
    X = array[:,0:15]
    Y = array[:,15]
    # feature extraction
    model = LogisticRegression()

    rfe = RFE(model, numOfFeatures)
    fit = rfe.fit(X, Y)

    for i in range(len(names)-1):
        if fit.support_[i] == True:
            #print(names[i])
            top_features.append(names[i])
    runAgainWithFS()
    analyzeFS()


def analyzeFS():

    x = train.getxgivenwin("trainingdata1.csv")
    for item in x:
        xy1list.append(item)
    y = train.getxgivenwin("trainingdata2.csv")
    for item in y:
        xy2list.append(item)
    team1 = xy2list[0]
    team2 = xy2list[1]
    splitteam1 = []
    splitteam2 = []

    biglist = []

    for element in team2:
        biglist.append(element)
    splitteam1.append(biglist[0:15])
    splitteam2.append(biglist[15:])
    for item in splitteam1:
        for i in item:
            newxy1list.append(i)
    for item in splitteam2:
        for i in item:
            newxy2list.append(i)


    for item in top_features:
        x = int(item)
        indexOfTopFeatures.append(x) #For future call in weighted features

        percentagelist1.append(newxy1list[x])
        percentagelist2.append(newxy2list[x])



    # NOW we are going to compare the two selected list

    for item in range(numOfFeatures):
        if percentagelist1[item] > percentagelist2[item]:
            findANameW_FS.append(1)
        elif percentagelist1[item] == percentagelist2[item]:
            findANameW_FS.append(0)
        else:
            findANameW_FS.append(2)
    ones_indexes = all_indices(1, findANameW_FS)

    #print(ones_indexes)
    for i in ones_indexes:
        finalAttributeNumsT1W_FS.append(train.xgivenwin[i])

    del indices[:]
    twos_indexes = all_indices(2, findANameW_FS)
    for i in twos_indexes:
        finalAttributeNumsT2W_FS.append(train.xgivenwin[i*2])


    results2(team1ListW_FS, team2ListW_FS, finalAttributeNumsT1W_FS, finalAttributeNumsT2W_FS)
    final_answer2()


    analyzeWF()
    results3(team1ListW_FS, team2ListW_FS)
    final_answer2()
def all_indices(value, list):

    idx = -1
    while True:
        try:
            idx = list.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices
def runAgainWithFS():
    openCSV2(main.teamname1())
    openCSV2(main.teamname2())

def openCSV2(team):
    with open(team + 'data.csv', 'r') as csvfile:
        next(csvfile)

        lastLine = csvfile.readlines()[-1]
        a = lastLine.split(",")

        for item in a:
            last_line.append(item)
        revised_line = [x.replace('\t', '').replace('\n', '') for x in last_line]

        for item in revised_line:
            #print(item)
            if team == main.teamname1():
                team1ListW_FS.append(item)
            if team == main.teamname2():
                team2ListW_FS.append(item)
        del last_line[:]


def results2(list1, list2, finalAttrs1, finalAttrs2):
    float_t1_List = [float(i) for i in list1]
    float_t2_List = [float(i) for i in list2]

    prob_t1 = np.prod(np.array(finalAttrs1)) * float_t1_List[-1]
    prob_t2 = np.prod(np.array(finalAttrs2)) * float_t2_List[-1]

    t1 = format(prob_t1, '.8f')
    new_answer.append(t1)

    t2 = format(prob_t2, '.8f')
    new_answer.append(t2)
    del float_t1_List[:]
    del float_t2_List[:]
    del newxy1list[:]
    del xy1list[:]
    del newxy2list[:]
    del xy2list[:]


def results3(list1, list2):
    float_t1_List = [float(i) for i in list1]
    float_t2_List = [float(i) for i in list2]
    #print(finalAttributeNumsT1W_WF)
    prob_t1 = np.prod(np.array(finalAttributeNumsT1W_WF)) * float_t1_List[-1]
    prob_t2 = np.prod(np.array(finalAttributeNumsT2W_WF)) * float_t2_List[-1]

    t1 = format(prob_t1, '.10f')
    new_answer.append(t1)

    t2 = format(prob_t2, '.10f')
    new_answer.append(t2)

def analyzeWF():
    """
    for item in top_features:
        x = int(item)
        indexOfTopFeatures.append(x) #For future call in weighted features

        percentagelist1.append(newxy1list[x])
        percentagelist2.append(newxy2list[x])

   

    # NOW we are going to compare the two selected list

    for item in range(numOfFeatures):
        if percentagelist1[item] > percentagelist2[item]:
            findANameW_FS.append(1)
        elif percentagelist1[item] == percentagelist2[item]:
            findANameW_FS.append(0)
        else:
            findANameW_FS.append(2)
    ones_indexes = all_indices(1, findANameW_FS)

    #print(ones_indexes)
    for i in ones_indexes:
        finalAttributeNumsT1W_FS.append(train.xgivenwin[i])

    del indices[:]
    twos_indexes = all_indices(2, findANameW_FS)
    for i in twos_indexes:
        finalAttributeNumsT2W_FS.append(train.xgivenwin[i*2])"""
    # The answer is not correct because it needs to add the followin line in oder for team swap to work

    x = train.getxgivenwin("trainingdata1.csv")
    for item in x:

        xy1list.append(item)
    y = train.getxgivenwin("trainingdata2.csv")
    for item in y:
        xy2list.append(item)
    team1 = xy2list[0]
    team2 = xy2list[1]
    splitteam1 = []
    splitteam2 = []
    # print(team1)
    biglist = []

    for element in team2:
        biglist.append(element)
    splitteam1.append(biglist[0:15])
    splitteam2.append(biglist[15:])
    for item in splitteam1:
        for i in item:
            newxy1list.append(i)
    for item in splitteam2:
        for i in item:
            newxy2list.append(i)
    # NOW we are going to compare the two selected list
    #print(newxy1list)
    for i in range(len(newxy1list)):
        if i in indexOfTopFeatures:
            #print(newxy1list[i])
            weightedList1.append(newxy1list[i] * beta)
            weightedList2.append(newxy2list[i] * beta)
        else:
            weightedList1.append(newxy1list[i])
            weightedList2.append(newxy2list[i])
    #print(weightedList1)
    for item in range(len(newxy1list)):
        if weightedList1[item] > weightedList2[item]:
            findANameW_WF.append(1)
        elif weightedList1[item] == weightedList2[item]:
            findANameW_WF.append(0)
        else:
            findANameW_WF.append(2)
    for i in findANameW_WF:
        if findANameW_WF[i] == 1:
            finalAttributeNumsT1W_WF.append(weightedList1[i])
            finalAttributeNumsT2W_WF.append(0.2)
        elif findANameW_WF[i] == 2:
            finalAttributeNumsT1W_WF.append(0.2)
            finalAttributeNumsT2W_WF.append(weightedList2[i])
        else:
            pass
    return finalAttributeNumsT2W_FS


def final_answer2():
    print(main.teamname1(), new_answer[0], main.teamname2(), new_answer[1])
    if abs(float(new_answer[0]) - float(new_answer[1])) > 0.001:
        print("Game should have at least ten point spread!")
    if new_answer[0] > new_answer[1]:
        print("Team : ", main.teamname1(), " should win!")
    else:
        print("Team : ", main.teamname2(), " should win!")
    del new_answer[:]


############
#Weighted Selection
weightedList1 = []
weightedList2 = []
beta = 1.3
# We can change beta to see how it affect final result




#print(weightedList1)

#bulk2()
#print(percentagelist1)

#print(weightedList1)