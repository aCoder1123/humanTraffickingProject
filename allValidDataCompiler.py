import json
import numpy as np

validFlightList = []

with open("allFlights.tsv") as file:
    validFlightList = file.read().split("\n")[1:-1]
    file.close()

aaList = []
amxList = []
spiritList = []
unitedList = []

with open("WebScraping/aaOutput.tsv") as file:
    flights = file.read().split("\n")
    flights.pop(0)
    aaList = flights
with open("WebScraping/amxOutput.tsv") as file:
    flights = file.read().split("\n")
    flights.pop(0)
    amxList = flights
with open("WebScraping/spiritOutput.tsv") as file:
    flights = file.read().split("\n")
    flights.pop(0)
    spiritList = flights
with open("WebScraping/unitedOutput.tsv") as file:
    flights = file.read().split("\n")
    flights.pop(0)
    unitedList = flights

cityDataDict = {}
with open("cityData2.json") as file:
    cityDataDict = json.loads(file.read())
    file.close()

flightDataList = []

for flight in validFlightList:
    origin, dest, _ = flight.split("\t")
    flightData = {}
    try:
        flightData = {
            "destination": cityDataDict[dest.lower()],
            "origin": cityDataDict[origin.lower()],
            "carriers": []
        }
    except:
        continue

    if flightData["destination"]["country"] != "United States of America" or flightData["origin"]["continent"] not in ["South America", "Asia", "North America", "Africa"] or flightData["origin"]["country"] in ["United States of America", "Canada"] or flightData["destination"]["state"] in ["Hawaii", "Guam"]:
        continue

    if flight in aaList:
        flightData["carriers"].append("aa")
    if flight in amxList:
        flightData["carriers"].append("amx")
    if flight in spiritList:
        flightData["carriers"].append("spirit")
    if flight in unitedList:
        flightData["carriers"].append("united")

    flightDataList.append(flightData)

destinationDict = {}
finalFlightDataList = []
for flight in flightDataList:
    if flight["destination"]["name"] in destinationDict.keys():
        destinationDict[flight["destination"]["name"]] += 1
    else:
        destinationDict[flight["destination"]["name"]] = 1

percentile = int(input("Enter desired percentile (int): "))
nthPercentile = np.percentile(list(destinationDict.values()), percentile)

# print(destinationDict.values())
# print(nthPercentile)
for flight in flightDataList:
    if destinationDict[flight["destination"]["name"]] >= nthPercentile: 
        finalFlightDataList.append(flight)
# ({percentile}pth)
outfile = open(f"fullValidFlightData.json", 'w')
outfile.write(json.dumps(finalFlightDataList, indent=4))
outfile.close()
