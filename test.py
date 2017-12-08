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




def attrCompare():
    #print(team1List)
    #print((team2List))
    for item in range(len(team1List)):
        if team1List[item] > team2List[item]:
            findAName.append(1)
        elif team1List[item] == team2List[item]:
            findAName.append(0)
        else:
            findAName.append(2)
    #print(findAName)
#print(findAName)
#print(findAName)

#print(finalAttributeNumsT1)
#print(finalAttributeNumsT2)

def win_team2():
    return team2List[-1]

def results():
    #print(team1List)
    #print(team2List)
    #float_t1_List = [float(i) for i in team1List]
    #float_t2_List = [float(i) for i in team2List]
    team1_prob = float(team1List[-1])
    team2_prob = float(team2List[-1])
    #print(team1_prob)
    #result = np.prod(np.array(mylist))
    prob_t1 = np.prod(np.array(finalAttributeNumsT1)) * team1_prob
    prob_t2 = np.prod(np.array(finalAttributeNumsT2)) * team2_prob

    t1 = format(prob_t1, '.20f')
    answer.append(t1)

    t2 = format(prob_t2, '.20f')
    answer.append(t2)
    #print(answer)



def final_answer():
    print(answer[0], main.teamname1(), answer[1], main.teamname2())
    for item in answer:
        if item == 0:
            answer[item] = 0.0000000001
    #print(abs(float(answer[0]) / float(answer[1])))
    #print(abs(float(answer[1]) / float(answer[0])))
    if abs(float(answer[0]) / float(answer[1])) or abs(float(answer[1]) / float(answer[0])) > 5:
        print("Game should have at least ten point spread!")
    if answer[0] > answer[1]:
        print("Team : ", main.teamname1(), " should win!")

    else:
        print("Team : ", main.teamname2(), " should win!")

def call_x_ys(num):
    dataset = "fulltrainingdata.csv"
    probs_of_X_Y_from_training_set = train.getxgivenwin(dataset)
    probs_of_win_from_training_set = probs_of_X_Y_from_training_set[0]
    probs_of_lose_from_training_set = probs_of_X_Y_from_training_set[1]
    #print(probs_of_win_from_training_set)
    #print(probs_of_lose_from_training_set)
    #dataset1 = main.teamname1()+"data.csv"
    #dataset2 = main.teamname2()+"data.csv"
    #x1 = train.getxgivenwin(dataset1)
    #x2 = train.getxgivenwin(dataset2)
    #x_y_1 = x1[0]
    #n_x_y_1 = x1[1]
    #x_y_2 = x2[0]
    #n_x_y_2 = x2[1]
    #x_y = train.xgivenwin
    #n_x_y = train.notxgivenwin


    # print(team1List[-1])
    # print(team2List[-1])
    #print(findAName)
    for i in range(num):
        ####I beleive you have to add not x_y_1 but the possiblility it leads to a win vs not a win
        if findAName[i] == 1:
            finalAttributeNumsT1.append(probs_of_win_from_training_set[i])
            finalAttributeNumsT2.append(0.2)
        elif findAName[i] == 2:
            finalAttributeNumsT1.append(0.2)
            finalAttributeNumsT2.append(probs_of_win_from_training_set[i])
        else:
            pass
    #print(finalAttributeNumsT1)
    #print(finalAttributeNumsT2)
    return finalAttributeNumsT1, finalAttributeNumsT2

def bulk():
    compareAttrs()
    attrCompare()
    numOfAttrs = 15
    call_x_ys(numOfAttrs)
    results()
    final_answer()
#bulk()
