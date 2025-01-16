import json

validFlightList = []

with open("validFlights.tsv") as file:
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


flightDataList = []

for flight in validFlightList:
    print(flight)
    flightData = {
        "destination": {
            "city": "",
            "lat": 0,
            "long": 0,
            "state": ""
        },
        "origin": {
            "country": "",
            "city": "",
            "lat": 0,
            "long": 0
        },

        "carriers": []
    }

    if flight in aaList:
        flightData["carriers"].append("aa")
    if flight in amxList:
        flightData["carriers"].append("amx")
    if flight in spiritList:
        flightData["carriers"].append("spirit")
    if flight in unitedList:
        flightData["carriers"].append("united")
    
    print(flightData)
    break

    flightDataList.append(flightData)


# outfile = open("fullValidFlightData.json", 'w')
# outfile.write(json.dumps({"allFlights": flightDataList}))
# outfile.close()
