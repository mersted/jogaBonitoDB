import urllib.request
from os import getcwd
from os import sep
from os import mkdir 
import csv
##
#http://www.football-data.co.uk/mmz4281/1314/D1.csv
countries =  ["England","Germany","Spain","Italy","France"]


season = ["1314","1213","1112","1112","1011","0910",
         "0809","0708","0607","0506","0405","0304",
         "0203","0102","0001","9900","9899","9798",
         "9697","9596","9495","9394"]

directory = getcwd()


def query(locale): #takes in the country and scrapes that countries data
    if locale == "England":
        xlc = "E0" #xlc holds the url path of the respective country
    elif locale == "Germany":
        xlc = "D1"
    elif locale == "Italy":
        xlc = "I1"
    elif locale == "Spain":
        xlc = "SP1"
    elif locale == "France":
        xlc = "F1"
    
    newdir = directory + sep + locale + sep #generates a filepath in the form cwd/country/
    mkdir(newdir)    
        
    for year in season: #downloads csv files for each year in the list season
        site = "http://www.football-data.co.uk/mmz4281/" + str(year) + "/" +str(xlc)+ ".csv" #generates the request url
        fpath = newdir + year + ".csv" #the new name for the corresponding csv file
        request = urllib.request.urlretrieve(site,fpath)
        print("Download Done for {0}, {1}".format(locale,year))
     
    print("Finally Done")


# Idea for how to read the data from csv files - Matt Ersted
def gatherData():
    aDict = {}
    for country in countries:
        for year in season:
            filename = directory + sep + country + sep + year + '.csv' 
            with open(filename, 'rb') as f:
                reader = csv.reader(f)
                i = 0
                for row in reader:
                    if i == 0:
                        headers = row
                    else:
                        homeTeam = row[2]
                        gameData = row[1:2] + row[3:23]
                        if homeTeam not in aDict.keys():
                            aDict[homeTeam] = (gameData,)
                        else:
                            aDict[homeTeam] += (gameData,)
                    i += 1


query("Germany")
query("England")
query("Spain")
query("France")
query("Italy")
            
