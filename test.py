import train
import numpy as np
import main


answer = []
last_line = []
team1List = []
team2List = []
findAName = []
finalAttributeNumsT1 = []
finalAttributeNumsT2 = []



def compareAttrs():
    openCSV(main.teamname1())
    openCSV(main.teamname2())



def openCSV(team):
    with open(team + 'data.csv', 'r') as csvfile:
        next(csvfile)
        #read = csv.reader(csvfile, delimiter=' ', quotechar=',')
        lastLine = csvfile.readlines()[-1]
        a = lastLine.split(",")

        for item in a:
            last_line.append(item)
        revised_line = [x.replace('\t', '').replace('\n', '') for x in last_line]
        #print(revised_line)
        for item in revised_line:
            #print(item)
            if team == main.teamname1():
                team1List.append(item)
            if team == main.teamname2():
                team2List.append(item)
        del last_line[:]


#print(team1List)
#print(team2List)

def attrCompare():
    for item in range(len(team1List)):
        if team1List[item] > team2List[item]:
            findAName.append(1)
        elif team1List[item] == team2List[item]:
            findAName.append(0)
        else:
            findAName.append(2)

#print(findAName)
#print(findAName)

#print(finalAttributeNumsT1)
#print(finalAttributeNumsT2)

def win_team2():
    return team2List[-1]

def results():
    float_t1_List = [float(i) for i in team1List]
    float_t2_List = [float(i) for i in team2List]

    #result = np.prod(np.array(mylist))
    prob_t1 = np.prod(np.array(finalAttributeNumsT1)) * float_t1_List[-1]
    prob_t2 = np.prod(np.array(finalAttributeNumsT1)) * float_t2_List[-1]
    #prob_t1 = functools.reduce(lambda x, y: x * y if y != 0 and x != 0 else 0.1, finalAttributeNumsT1) * win_team1()
    #prob_t2 = functools.reduce(lambda x, y: x * y if y != 0 and x != 0 else 0.1, finalAttributeNumsT2) * win_team2()

    t1 = format(prob_t1, '.8f')
    answer.append(t1)

    t2 = format(prob_t2, '.8f')
    answer.append(t2)
    #print(answer)



def final_answer():
    if answer[0] > answer[1]:
        print("Team : ", main.teamname1(), " should win!")
    else:
        print("Team : ", main.teamname2(), " should win!")


def bulk():
    compareAttrs()
    attrCompare()
    numOfAttrs = 15
    x_y = train.xgivenwin
    n_x_y = train.notxgivenwin
    # print(x_y)
    # print(n_x_y)

    # print(team1List[-1])
    # print(team2List[-1])
    for i in range(numOfAttrs):

        if findAName[i] == 1:
            finalAttributeNumsT1.append(x_y[i])
            finalAttributeNumsT2.append(n_x_y[i])
        elif findAName[i] == 2:
            finalAttributeNumsT1.append(x_y[i])
            finalAttributeNumsT2.append(n_x_y[i])
        else:
            pass
    results()
    final_answer()
#bulk()