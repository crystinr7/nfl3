import requests
import csv
from bs4 import BeautifulSoup
import main

stats = []

# LISTS FOR PROGRAM
players = []
totalmax = []
maxnumber = []
maxTeam = []

pOfXsWins = []
pOfXsLosses = []
probs_win = []
probs_lose = []

outcome = []
prob_t1_win = []
prob_t2_win = []

# Attribute lists

team1list = []
team2list = []
probabilities = []
winner_is = []
points = []
less_likely_to_lose = []
train_team_1_list = []
train_team_2_list = []
##teamnames = []




teamname = "MASTER"


list = main.masterlist()


def createTrainingCSV():
    with open('trainingdata2.csv', 'w') as c:
        writer = csv.writer(c, delimiter=' ',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow("Training Data Team 2 win")


def appendCSV():
    with open("trainingdata2.csv", "a") as f:
        wr = csv.writer(f)
        if winning_team() == 1:
            wr.writerow(train_team_1_list)
        else:
            wr.writerow(train_team_2_list)





def yearstatsForTeam1WIN():
    if winning_team() == 1:
        run_training_attrs()


def yearstatsForTeam2WIN():
    if winning_team() == 2:
        run_training_attrs()


# NAME OF EACH TEAM
def team1():
    return stats[0]


def team2():
    return stats[6]


# RETURNS WINNING TEAM FOR THAT GAME
def winning_team():
    if float(stats[5]) > float(stats[11]):
        return 1
    else:
        return 2







def train_attr1():
    # Grabs first quarter points
    if float(stats[1]) > float(stats[7]):

        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[1]) == float(stats[7]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr2():
    # Grabs second quarter points
    if float(stats[2]) > float(stats[8]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[2]) == float(stats[8]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr3():
    # Grabs third quarter points
    if float(stats[3]) > float(stats[9]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[3]) == float(stats[9]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr4():
    if float(stats[4]) > float(stats[10]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[4]) == float(stats[10]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr5():
    # Grabs first downs
    if float(stats[13]) > float(stats[14]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[13]) == float(stats[14]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr6():
    # Grabs passing first downs
    if float(stats[16]) > float(stats[17]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[16]) == float(stats[17]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr7():
    # Grabs rushing first downs
    if float(stats[19]) > float(stats[20]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[19]) == float(stats[20]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr8():
    # Grabs total yards
    if float(stats[34]) > float(stats[35]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[34]) == float(stats[35]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr9():
    # Grabs yards per play
    if float(stats[40]) > float(stats[41]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[40]) == float(stats[41]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr10():
    # Grabs passing yards
    if float(stats[43]) > float(stats[44]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[43]) == float(stats[44]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr11():
    # grabs yards per pass
    if float(stats[49]) > float(stats[50]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[49]) == float(stats[50]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr12():
    # Grabs rushing yards
    if float(stats[58]) > float(stats[59]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[58]) == float(stats[59]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr13():
    # Grabs yards per rush
    if float(stats[64]) > float(stats[65]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[64]) == float(stats[65]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr14():
    # Grabs turnovers
    if float(stats[73]) > float(stats[74]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(stats[73]) == float(stats[74]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def train_attr15():
    # Grabs possession minutes
    x = stats[85].split(":")
    y = stats[86].split(":")
    if float(x[0]) > float(y[0]):
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    elif float(x[0]) == float(y[0]):
        train_team_1_list.append(0.5)
        train_team_2_list.append(0.5)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


def run_training_attrs():
    train_attr1()
    train_attr2()
    train_attr3()
    train_attr4()
    train_attr5()
    train_attr6()
    train_attr7()
    train_attr8()
    train_attr9()
    train_attr10()
    train_attr11()
    train_attr12()
    train_attr13()
    train_attr14()
    train_attr15()
    if winning_team() == 1:
        train_team_1_list.append(1)
        train_team_2_list.append(0)
    else:
        train_team_1_list.append(0)
        train_team_2_list.append(1)


# PROBABILITY OF OUTCOME
def prob_of_win():
    return 0.5


def prob_of_lose():
    return 0.5


createTrainingCSV()

#teamname1()
for item in list:

    html = requests.get(item).text
    soup = BeautifulSoup(html, 'html5lib')
    # GRAB ALL STAT INFO
    for td_tag in soup.find_all('td'):
        stat = td_tag.text
        stats.append(stat)
        stats = [x.replace('\t', '').replace('\n', '') for x in stats]
    print(stats)
    #yearstatsForTeam1WIN()
    yearstatsForTeam2WIN()

    appendCSV()
    del stats[:]
    del train_team_1_list[:]
    del train_team_2_list[:]
