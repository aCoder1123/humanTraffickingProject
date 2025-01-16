import json

infoDict = json.loads(open("cityData.json").read())

inFile = open("allFlights.tsv")
data = inFile.read().split("\n")
inFile.close()
data.pop(0)
outString = "Origin\tDestination\n"

for flight in data:
    flightData = flight.split("\t")
    flightData.remove("")
    if len(flightData) < 2:
        continue
    origin, destination = flightData
    keys = infoDict.keys()
    if (origin in keys and destination in keys and infoDict[origin]["continent"] in ["Asia", "South America", "Oceania"] and infoDict[destination]["country"] == "United States of America"):
        outString += flight + "\n"


outFile = open("validFlights.tsv", "w")
outFile.write(outString)
outFile.close()
