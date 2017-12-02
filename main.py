
def teamname1():
    return "DET"
def teamname2():
    return "PHI"
def list(teamname):
    # CHIEFS
    if teamname == "KC":
        return ["http://www.espn.com/nfl/matchup?gameId=400951566", "http://www.espn.com/nfl/matchup?gameId=400951636",
                "http://www.espn.com/nfl/matchup?gameId=400951634", "http://www.espn.com/nfl/matchup?gameId=400951752",
                "http://www.espn.com/nfl/matchup?gameId=400951664", "http://www.espn.com/nfl/matchup?gameId=400951776",
                "http://www.espn.com/nfl/matchup?gameId=400951571"]
    # LIONS
    if teamname == "DET":
        return ["http://www.espn.com/nfl/matchup?gameId=400951576", "http://www.espn.com/nfl/matchup?gameId=400951681",
                "http://www.espn.com/nfl/matchup?gameId=400951594", "http://www.espn.com/nfl/matchup?gameId=400951724",
                "http://www.espn.com/nfl/matchup?gameId=400951558", "http://www.espn.com/nfl/matchup?gameId=400951704"]
    # STEELERS
    if teamname == "PIT":
        return ["http://www.espn.com/nfl/matchup?gameId=400951574", "http://www.espn.com/nfl/matchup?gameId=400951643",
                "http://www.espn.com/nfl/matchup?gameId=400951708", "http://www.espn.com/nfl/matchup?gameId=400951655",
                "http://www.espn.com/nfl/matchup?gameId=400951776", "http://www.espn.com/nfl/matchup?gameId=400951609"]
    # RAIDERS
    if teamname == "OAK":
        return ["http://www.espn.com/nfl/matchup?gameId=400951584", "http://www.espn.com/nfl/matchup?gameId=400951669",
                "http://www.espn.com/nfl/matchup?gameId=400951644", "http://www.espn.com/nfl/matchup?gameId=400951744",
                "http://www.espn.com/nfl/matchup?gameId=400951659", "http://www.espn.com/nfl/matchup?gameId=400951779",
                "http://www.espn.com/nfl/matchup?gameId=400951571"]
    # BRONCOS
    if teamname == "DEN":
        return ["http://www.espn.com/nfl/matchup?gameId=400951615","http://www.espn.com/nfl/matchup?gameId=400951673",
                "http://www.espn.com/nfl/matchup?gameId=400951583", "http://www.espn.com/nfl/matchup?gameId=400951744",
                "http://www.espn.com/nfl/matchup?gameId=400951782", "http://www.espn.com/nfl/matchup?gameId=400951624",
                "http://www.espn.com/nfl/matchup?gameId=400951737"]
    # EAGLES
    if teamname == "PHI":
        return ["http://www.espn.com/nfl/matchup?gameId=400951592", "http://www.espn.com/nfl/matchup?gameId=400951636",
                "http://www.espn.com/nfl/matchup?gameId=400951616", "http://www.espn.com/nfl/matchup?gameId=400951738",
                "http://www.espn.com/nfl/matchup?gameId=400951695", "http://www.espn.com/nfl/matchup?gameId=400951641",
                "http://www.espn.com/nfl/matchup?gameId=400951723"]
    # BUCCANEERS
    if teamname == "TB":
        return["http://www.espn.com/nfl/matchup?gameId=400951552","http://www.espn.com/nfl/matchup?gameId=400951645",
               "http://www.espn.com/nfl/matchup?gameId=400951604","http://www.espn.com/nfl/matchup?gameId=400951742",
               "http://www.espn.com/nfl/matchup?gameId=400951770","http://www.espn.com/nfl/matchup?gameId=400951575"]
    # PANTHERS
    if teamname == "CAR":
        return ["http://www.espn.com/nfl/matchup?gameId=400951605","http://www.espn.com/nfl/matchup?gameId=400951630",
                "http://www.espn.com/nfl/matchup?gameId=400951587","http://www.espn.com/nfl/matchup?gameId=400951727",
                "http://www.espn.com/nfl/matchup?gameId=400951558","http://www.espn.com/nfl/matchup?gameId=400951695",
                "http://www.espn.com/nfl/matchup?gameId=400951578"]
    # BILLS
    if teamname == "BUF":
        return ["http://www.espn.com/nfl/matchup?gameId=400951567","http://www.espn.com/nfl/matchup?gameId=400951630",
                "http://www.espn.com/nfl/matchup?gameId=400951583", "http://www.espn.com/nfl/matchup?gameId=400951685",
                "http://www.espn.com/nfl/matchup?gameId=400951554", "http://www.espn.com/nfl/matchup?gameId=400951575"]
    # CHARGERS
    if teamname == "LAC":
        return ["http://www.espn.com/nfl/matchup?gameId=400951615", "http://www.espn.com/nfl/matchup?gameId=400951666",
                "http://www.espn.com/nfl/matchup?gameId=400951634", "http://www.espn.com/nfl/matchup?gameId=400951738"
                ]
    # JETS
    if teamname == "NYJ":
        return ["http://www.espn.com/nfl/matchup?gameId=400951567","http://www.espn.com/nfl/matchup?gameId=400951669",
                "http://www.espn.com/nfl/matchup?gameId=400951611","http://www.espn.com/nfl/matchup?gameId=400951556",
                "http://www.espn.com/nfl/matchup?gameId=400951766", "http://www.espn.com/nfl/matchup?gameId=400951598"]
    # FALCONS
    if teamname == "ATL":
        return ["http://www.espn.com/nfl/matchup?gameId=400951570", "http://www.espn.com/nfl/matchup?gameId=400951679",
                      "http://www.espn.com/nfl/matchup?gameId=400951594", "http://www.espn.com/nfl/matchup?gameId=400951685",
                      "http://www.espn.com/nfl/matchup?gameId=400951697", "http://www.espn.com/nfl/matchup?gameId=400951638"]
    # SAINTS
    if teamname == "NO":
        return ["http://www.espn.co.uk/nfl/matchup?gameId=400951612", "http://www.espn.com/nfl/matchup?gameId=400951639",
                "http://www.espn.com/nfl/matchup?gameId=400951587", "http://www.espn.com/nfl/matchup?gameId=400950241"]
    # VIKINGS
    if teamname == "MIN":
        return ["http://www.espn.co.uk/nfl/matchup?gameId=400951612", "http://www.espn.com/nfl/matchup?gameId=400951643",
                "http://www.espn.com/nfl/matchup?gameId=400951604", "http://www.espn.com/nfl/matchup?gameId=400951724"]
    # BENGALS
    if teamname == "CIN":
        return ["http://www.espn.com/nfl/matchup?gameId=400951572", "http://www.espn.com/nfl/matchup?gameId=400951620",
                "http://www.espn.com/nfl/matchup?gameId=400951712"]
    # RAVENS
    if teamname == "BAL":
        return ["http://www.espn.com/nfl/matchup?gameId=400951572", "http://www.espn.com/nfl/matchup?gameId=400951626",
                "http://www.espn.com/nfl/matchup?gameId=400951579", "http://www.espn.com/nfl/matchup?gameId=400951708"]
    # COLTS
    if teamname == "IND":
        return ['http://www.espn.com/nfl/matchup?gameId=400951597', "http://www.espn.com/nfl/matchup?gameId=400951599",
                "http://www.espn.com/nfl/matchup?gameId=400951747"]
    # RAMS
    if teamname == "LAR":
        return ['http://www.espn.com/nfl/matchup?gameId=400951597', "http://www.espn.com/nfl/matchup?gameId=400951674",
                "http://www.espn.com/nfl/matchup?gameId=400951568", "http://www.espn.com/nfl/matchup?gameId=400951716"]
    # REDSKINS
    if teamname == "WAS":
        return ["http://www.espn.com/nfl/matchup?gameId=400951592", "http://www.espn.com/nfl/matchup?gameId=400951644",
                "http://www.espn.com/nfl/matchup?gameId=400951674", "http://www.espn.com/nfl/matchup?gameId=400951752"]
    # BROWNS
    if teamname == "CLE":
        return ["http://www.espn.com/nfl/matchup?gameId=400951574","http://www.espn.com/nfl/matchup?gameId=400951626",
                "http://www.espn.com/nfl/matchup?gameId=400951599", "http://www.espn.com/nfl/matchup?gameId=400951712"]
    # PATRIOTS
    if teamname == "NE":
        return ["http://www.espn.com/nfl/matchup?gameId=400951566", "http://www.espn.com/nfl/matchup?gameId=400951639",
                "http://www.espn.com/nfl/matchup?gameId=400951607", "http://www.espn.com/nfl/matchup?gameId=400951727"]
    # BEARS
    if teamname == "CHI":
        return ["http://www.espn.com/nfl/matchup?gameId=400951570", "http://www.espn.com/nfl/matchup?gameId=400951645",
                "http://www.espn.com/nfl/matchup?gameId=400951678"]
    # TITANS
    if teamname == "TEN":
        return ["http://www.espn.com/nfl/matchup?gameId=400951584", "http://www.espn.com/nfl/matchup?gameId=400951635",
                "http://www.espn.com/nfl/matchup?gameId=400951623", "http://www.espn.com/nfl/matchup?gameId=400951720"]
    # JAGUARS
    if teamname == "JAX":
        return ["http://www.espn.com/nfl/matchup?gameId=400951580", "http://www.espn.com/nfl/matchup?gameId=400951635",
                "http://www.espn.com/nfl/matchup?gameId=400951579"]
    # TEXANS
    if teamname == "HOU":
        return ["http://www.espn.com/nfl/matchup?gameId=400951580", "http://www.espn.com/nfl/matchup?gameId=400951620",
                "http://www.espn.com/nfl/matchup?gameId=400951607", "http://www.espn.com/nfl/matchup?gameId=400951720"]
    # COWBOYS
    if teamname == "DAL":
        return ["http://www.espn.com/nfl/matchup?gameId=400951608","http://www.espn.com/nfl/matchup?gameId=400951673",
                "http://www.espn.com/nfl/matchup?gameId=400951668", "http://www.espn.com/nfl/matchup?gameId=400951716"]
    # CARDINALS
    if teamname == "ARI":
        return ["http://www.espn.com/nfl/matchup?gameId=400951576", "http://www.espn.com/nfl/matchup?gameId=400951668"]
    # 4e9ers
    if teamname == "SFO":
        return ["http://www.espn.com/nfl/matchup?gameId=400951605", "http://www.espn.com/nfl/matchup?gameId=400951676",
                "http://www.espn.com/nfl/matchup?gameId=400951568"]
    # SEAHAWKS
    if teamname == "SEA":
        return ["http://www.espn.com/nfl/matchup?gameId=400951601", "http://www.espn.com/nfl/matchup?gameId=400951676",
                "http://www.espn.com/nfl/matchup?gameId=400951623", "http://www.espn.com/nfl/matchup?gameId=400951747"]
    # PACKERS
    if teamname == "GB":
        return ["http://www.espn.com/nfl/matchup?gameId=400951601", "http://www.espn.com/nfl/matchup?gameId=400951679",
                "http://www.espn.com/nfl/matchup?gameId=400951678"]
    # GIANTS
    if teamname == "NYG":
        return ["http://www.espn.com/nfl/matchup?gameId=400951608", "http://www.espn.com/nfl/matchup?gameId=400951681",
                "http://www.espn.com/nfl/matchup?gameId=400951616", "http://www.espn.com/nfl/matchup?gameId=400951742"]
    # DOLPHINS
    if teamname == "MIA":
        return ["http://www.espn.com/nfl/matchup?gameId=400951666", "http://www.espn.com/nfl/matchup?gameId=400951611",
                "http://www.espn.com/nfl/matchup?gameId=400950241"]
# HAVE FOUR WEEKS
def masterlist():
    ##if teamname() == "MASTER":
        return ["http://www.espn.com/nfl/matchup?gameId=400951574", "http://www.espn.com/nfl/matchup?gameId=400951566",
            "http://www.espn.com/nfl/matchup?gameId=400951570","http://www.espn.com/nfl/matchup?gameId=400951592",
            "http://www.espn.com/nfl/matchup?gameId=400951567","http://www.espn.com/nfl/matchup?gameId=400951584",
            "http://www.espn.com/nfl/matchup?gameId=400951580","http://www.espn.com/nfl/matchup?gameId=400951669",
            "http://www.espn.com/nfl/matchup?gameId=400951644","http://www.espn.com/nfl/matchup?gameId=400951615",
            "http://www.espn.com/nfl/matchup?gameId=400951673", "http://www.espn.com/nfl/matchup?gameId=400951583",
            "http://www.espn.com/nfl/matchup?gameId=400951576", "http://www.espn.com/nfl/matchup?gameId=400951572",
            "http://www.espn.com/nfl/matchup?gameId=400951597", "http://www.espn.com/nfl/matchup?gameId=400951605",
            "http://www.espn.com/nfl/matchup?gameId=400951601", "http://www.espn.com/nfl/matchup?gameId=400951608",
            "http://www.espn.com/nfl/matchup?gameId=400951612", "http://www.espn.com/nfl/matchup?gameId=400951620",
            "http://www.espn.com/nfl/matchup?gameId=400951636", "http://www.espn.com/nfl/matchup?gameId=400951635",
            "http://www.espn.com/nfl/matchup?gameId=400951645", "http://www.espn.com/nfl/matchup?gameId=400951630",
            "http://www.espn.com/nfl/matchup?gameId=400951626", "http://www.espn.com/nfl/matchup?gameId=400951643",
            "http://www.espn.com/nfl/matchup?gameId=400951639", "http://www.espn.com/nfl/matchup?gameId=400951666",
            "http://www.espn.com/nfl/matchup?gameId=400951676", "http://www.espn.com/nfl/matchup?gameId=400951674",
            "http://www.espn.com/nfl/matchup?gameId=400951679", "http://www.espn.com/nfl/matchup?gameId=400951681",
            "http://www.espn.com/nfl/matchup?gameId=400951568", "http://www.espn.com/nfl/matchup?gameId=400951579",
            "http://www.espn.com/nfl/matchup?gameId=400951594", "http://www.espn.com/nfl/matchup?gameId=400951599",
            "http://www.espn.com/nfl/matchup?gameId=400951587", "http://www.espn.com/nfl/matchup?gameId=400951616",
            "http://www.espn.com/nfl/matchup?gameId=400951611", "http://www.espn.com/nfl/matchup?gameId=400951607",
            "http://www.espn.com/nfl/matchup?gameId=400951604", "http://www.espn.com/nfl/matchup?gameId=400951623",
            "http://www.espn.com/nfl/matchup?gameId=400951634", "http://www.espn.com/nfl/matchup?gameId=400951668",
            "http://www.espn.com/nfl/matchup?gameId=400951678", "http://www.espn.com/nfl/matchup?gameId=400950241",
            "http://www.espn.com/nfl/matchup?gameId=400951720", "http://www.espn.com/nfl/matchup?gameId=400951716",
            "http://www.espn.com/nfl/matchup?gameId=400951712", "http://www.espn.com/nfl/matchup?gameId=400951685",
            "http://www.espn.com/nfl/matchup?gameId=400951708", "http://www.espn.com/nfl/matchup?gameId=400951727",
            "http://www.espn.com/nfl/matchup?gameId=400951724", "http://www.espn.com/nfl/matchup?gameId=400951742",
            "http://www.espn.com/nfl/matchup?gameId=400951738", "http://www.espn.com/nfl/matchup?gameId=400951744",
            "http://www.espn.com/nfl/matchup?gameId=400951747", "http://www.espn.com/nfl/matchup?gameId=400951752"]

