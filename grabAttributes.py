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
teamnames = []

def teamname():
    teamnames.append(main.teamname1())
    teamnames.append(main.teamname2())

def createTrainingCSV():
    with open(main.masterlist() +'data.csv', 'w') as c:
        writer = csv.writer(c, delimiter=' ',
                                quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(main.masterlist())
def createCSV(team):
    with open(team +'data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                                quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(team)
def appendCSV(team):
    with open(team +"data.csv", "a") as f:
        wr = csv.writer(f)
        if team == team1():
            wr.writerow(team1list)
        else:
            wr.writerow(team2list)

def teamstats(team):
    if team == team1():
        if len(team1list) == 0:
            team1list.append(team1())
        run_attrs()
    if team == team2():
        if len(team2list) == 0:
            team2list.append(team2())
        run_attrs()


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
# LIST OF ATTRIBUTES

# WHO SCORED MORE POINTS IN THE FIRST QUARTER
def attr1():

    # Grabs first quarter points
    if float(stats[1]) > float(stats[7]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[1]) == float(stats[7]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
# WHO SCORED MORE POINTS IN THE SECOND QUARTER
def attr2():
    # Grabs second quarter points
    if float(stats[2]) > float(stats[8]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[2]) == float(stats[8]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
# WHO SCORED MORE POINTS IN THE THIRD QUARTER
def attr3():
    # Grabs third quarter points
    if float(stats[3]) > float(stats[9]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[3]) == float(stats[9]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
# WHO SCORED MORE POINTS IN THE FOURTH QUARTER
def attr4():
    if float(stats[4]) > float(stats[10]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[4]) == float(stats[10]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
def attr5():
    # Grabs first downs
    if float(stats[13]) > float(stats[14]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[13]) == float(stats[14]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
def attr6():
    # Grabs passing first downs
    if float(stats[16]) > float(stats[17]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[16]) == float(stats[17]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
def attr7():
    # Grabs rushing first downs
    if float(stats[19]) > float(stats[20]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[19]) == float(stats[20]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
def attr8():
    # Grabs total yards
    if float(stats[34]) > float(stats[35]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[34]) == float(stats[35]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
def attr9():
    # Grabs yards per play
    if float(stats[40]) > float(stats[41]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[40]) == float(stats[41]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
def attr10():
    # Grabs passing yards
    if float(stats[43]) > float(stats[44]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[43]) == float(stats[44]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
def attr11():
    #grabs yards per pass
    if float(stats[49]) > float(stats[50]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[49]) == float(stats[50]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
def attr12():
    # Grabs rushing yards
    if float(stats[58]) > float(stats[59]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[58]) == float(stats[59]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
def attr13():
    # Grabs yards per rush
    if float(stats[64]) > float(stats[65]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[64]) == float(stats[65]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
def attr14():
    # Grabs turnovers
    if float(stats[73]) > float(stats[74]):
        team1list.append(1)
        team2list.append(0)
    elif float(stats[73]) == float(stats[74]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)
def attr15():
    # Grabs possession minutes
    x = stats[85].split(":")
    y = stats[86].split(":")
    if float(x[0]) > float(y[0]):
        team1list.append(1)
        team2list.append(0)
    elif float(x[0]) == float(y[0]):
        team1list.append(0.5)
        team2list.append(0.5)
    else:
        team1list.append(0)
        team2list.append(1)

def run_attrs():
    # CALLS ALL ATTRIBUTES TO ADD TO THE LIST
    attr1()
    attr2()
    attr3()
    attr4()
    attr5()
    attr6()
    attr7()
    attr8()
    attr9()
    attr10()
    attr11()
    attr12()
    attr13()
    attr14()
    attr15()
    if winning_team() == 1:
        team1list.append(1)
        team2list.append(0)
    else:
        team1list.append(0)
        team2list.append(1)


# PROBABILITY OF OUTCOME
def prob_of_win():
    return 0.5
def prob_of_lose():
    return 0.5
def bulk():
    teamname()
    team = main.teamname1()
    #createTrainingCSV()
    #Writes out first line with team name
    #createCSV(team)

    list = main.list(team)
    for item in list:

        html = requests.get(item).text
        soup = BeautifulSoup(html, 'html5lib')
        # GRAB ALL STAT INFO
        for td_tag in soup.find_all('td'):
            each_stat = td_tag.text
            stats.append(each_stat)
            stat = [x.replace('\t', '').replace('\n', '') for x in stats]

        teamstats(team)
        appendCSV(team)
        del stats[:]
        del team1list[:]
        del team2list[:]
        #del stat[:]

    team2 = main.teamname2()


    list = main.list(team2)
    for item in list:

        html = requests.get(item).text
        soup = BeautifulSoup(html, 'html5lib')
        # GRAB ALL STAT INFO
        for td_tag in soup.find_all('td'):
            each_stat = td_tag.text
            stats.append(each_stat)
            stat = [x.replace('\t', '').replace('\n', '') for x in stats]
        #print(stat)
        teamstats(team2)
        appendCSV(team2)
        del stats[:]
        del team1list[:]
        del team2list[:]

#bulk()