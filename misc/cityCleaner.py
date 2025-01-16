import json
from pprint import pprint

dataFile = open("cities.json", "r")
data = json.loads(dataFile.read())["results"]
dataFile.close()

outputDict = {}

for city in data:
    outputDict[city["name"]] = {"location": city["location"], "name": city["name"], "country": city["country"]["name"], "continent": city["country"]["continent"]["name"], "population": city["population"]}

outputFile = open("citiesCleaned.json", "w")
outputFile.write(json.dumps(outputDict, indent=4))



