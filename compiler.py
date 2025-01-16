fullDataList = []
for filename in ["aaOutput.tsv", "amxOutput.tsv", "spiritOutput.tsv", "unitedOutput.tsv"]:
    file = open(filename)
    fileData = file.read().split("\n")
    file.close()
    fileData.pop(0)
    fullDataList += fileData

fullDataList = list(set(fullDataList))
fullDataList.sort()

outFile = open("allFlights.tsv", 'w')
outFile.write("Origin\tDestination\n")
for data in fullDataList:
    outFile.write(data + "\n")

outFile.close()
