import main
import csv


numOfAttrs = 15
givenwin = []
givenloss = []
list = []
prob_win = []

def p_x_y(attr, team):
    numOfGames = len(main.list(team))
    with open(team +'data.csv', 'r') as csvfile:
        next(csvfile)
        read = csv.reader(csvfile, delimiter=' ', quotechar=',')
        given_win = 0
        given_loss = 0
        notxgivenwin = 0
        notxgivenloss = 0
        for row in read:
            # This grabs a certain column and reads how many times it happens
            for word in row:

                word = word.split(",")

                for i in range(len(row)): #

                    if '1' in word[attr] and '1' in word[-1]:
                        given_win += 1
                    if '1' in word[attr] and '0' in word[-1]:
                        given_loss += 1
                    if '0' in word[attr] and '1' in word[-1]:
                        notxgivenwin += 1
                    if '0' in word[attr] and '0' in word[-1]:
                        notxgivenloss += 1

        p_not_x_y = given_loss / numOfGames
        p_x_y = given_win / numOfGames
        not_p_x_y = notxgivenwin / numOfGames
        not_p_not_x_y = notxgivenloss / numOfGames

    return p_x_y, p_not_x_y#p_not_x_y

def prob_of_win(team):
    numOfGames = len(main.list(team))
    if team == main.teamname1():

        with open(main.teamname1()+'data.csv', 'r') as csvfile:
            next(csvfile)
            read = csv.reader(csvfile, delimiter=' ', quotechar=',')
            wins = 0
            for row in read:

                for word in row:
                    #print(word)
                    word = word.split(",")
                    #print(word)
                    if '1' in word[-1]:
                        wins += 1
            chances = ((wins / numOfGames) + 0.5) / 2
            #print(chances)
            prob_win.append(chances)
            return (chances)
    else:
        with open(main.teamname2()+'data.csv', 'r') as csvfile:
            next(csvfile)
            read = csv.reader(csvfile, delimiter=' ', quotechar=',')
            wins = 0
            for row in read:

                for word in row:
                    #print(word)
                    word = word.split(",")
                    #print(word)
                    if '1' in word[-1]:
                        wins += 1

            #print(((wins / numOfGames) + 0.5) / 2)
            return (((wins / numOfGames) + 0.5) / 2)
"""def prob_of_lose(team):
    with open(team +'data.csv', 'r') as csvfile:
        next(csvfile)
        read = csv.reader(csvfile, delimiter=' ', quotechar=',')
        wins = 0
        for row in read:



            #print(row)
            for word in row:
                #print(word)
                word = word.split(",")
                #print(word)
                if '0' in word[-1]:
                    wins += 1

        print(((wins/ numOfGames) + 0.5) / 2)
        return (((wins/ numOfGames) + 0.5) / 2)"""

def append_csv():
    team1 = main.teamname1()
    prob_of_win(team=team1)
    with open(team1 + "data.csv", "a") as f:


        for i in range(numOfAttrs):
            givenwin.append(p_x_y(i, team1)[0])
        givenwin.append(prob_of_win(team1))
        #givenloss.append(p_x_y(i)[1])
        wr = csv.writer(f)
        wr.writerow(givenwin)

    team2 = main.teamname2()
    prob_of_win(team=team2)

    del givenwin[:]
    with open(team2 + "data.csv", "a") as f:


        for i in range(numOfAttrs):
            givenwin.append(p_x_y(i, team2)[0])
        givenwin.append(prob_of_win(team2))
        wr = csv.writer(f)
        wr.writerow(givenwin)
        # givenloss.append(p_x_y(i)[1])
    #test.compareAttrs()
def bulk():
    append_csv()

#bulk()
""" We want to grab all data for the season and then put it into a naive bayes testing set from there we analyze
the boosting algorithm. From there we can think about using that algorithm for e=stiment alalysis and see which 
answer is best. """

