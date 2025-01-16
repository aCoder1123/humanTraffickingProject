import json
import requests
from pprint import pprint

inFile = open("allFlights.tsv", "r")

flightList = inFile.read().split("\n")
flightList.pop(0)
allNodesList = []

for flight in flightList:
    flightData = flight.split("\t")
    allNodesList += flightData

allNodesList = list(set(allNodesList))
placesDict = {}
countryToContinentFile = open("Countries by continents.csv").read().split("\n")
countryToContinentFile.pop(0)
countryToContinentDict = {}

for country in countryToContinentFile:
    countryToContinentDict[country.split(",")[1]] = country.split(",")[0]

codesList = json.loads(open("CountryCodes.json").read())

allNodesList.remove("")
allNodesList.sort()

dataList = []
for node in allNodesList:
    response = ''
    try:
        print(node)
        res = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={node}&limit=1&appid=5da5999914549a585e1b005b89ad2444").text
        response = res
        countryData = json.loads(res)[0]
        country = ""
        dataList.append(json.loads(res))
        for i in codesList:
            if i["alpha-2"] == countryData["country"]:
                country = i["name"]

        continent = countryToContinentDict[country.split(",")[0]]
        placesDict[node.lower()] = {"name": node, "country": country, "countryCode": countryData["country"],
                                    "continent": continent, "lat": countryData["lat"], "lon": countryData["lon"]}
        if "state" in countryData.keys():
            placesDict[node.lower()]["state"] = countryData["state"]
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(f"Error at node: <{node}>")
        print(message)
        pprint(response)
        response = ''
        inString = input("Would you like to continue (y/n): ")
        if inString.lower() == "n": break

outFile = open("cityData2.json", "w")
outFile.write(json.dumps(placesDict, indent=4))
outFile.close()

with open("fullCountryData.json", "w") as file:
    file.write(json.dumps(dataList, indent=4))
    file.close()