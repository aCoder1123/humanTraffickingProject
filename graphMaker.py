from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:

    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.DiGraph()
        G.add_edges_from(self.visual)
        pos = nx.spring_layout(G, seed=1734289230)
        pprint(pos)
        nodes = nx.draw_networkx_nodes(G, pos, node_color="blue", alpha=.95, node_size=400)
        edges = nx.draw_networkx_edges(
            G,
            pos,
            arrowstyle="->",
            arrowsize=10,
            width=1,
        )
        label_options = {"ec": "k", "fc": "yellow", "alpha": 0.7}
        nx.draw_networkx_labels(G, pos, font_size=8, font_color="black", bbox=label_options)
        
        img = plt.imread("robinsonProjection.jpg")
        plt.imshow(img)
        plt.show()
        


fullDataList = []
for filename in ["validFlights.tsv"]: #["aaOutput.tsv", "amxOutput.tsv", "spiritOutput.tsv", "unitedOutput.tsv"]:
    file = open(filename)
    fileData = file.read().split("\n")
    file.close()
    fileData.pop(0)
    fullDataList += fileData

departuresList = []
destinationsList = []
flightsDict = {}

for flight in fullDataList:
    flightList = flight.split("\t")
    departuresList.append(flightList[0])
    destinationsList.append(flightList[1])

    if flightList[0] in flightsDict and not flightList[1] in flightsDict[flightList[0]]:
        flightsDict[flightList[0]].append(flightList[1])
    else:
        flightsDict[flightList[0]] = [flightList[1]]

allNodesList = list(set(departuresList + destinationsList))
departuresList = list(set(departuresList))
destinationsList = list(set(destinationsList))

pprint(flightsDict)
print(f"There are {len(allNodesList)} nodes total with {len(departuresList)} departure cities and {len(destinationsList)} destination cities.")

G = GraphVisualization()
counter = 0

for node in allNodesList:
    counter += 1
    if node in flightsDict:
        for flight in flightsDict[node]:
            G.addEdge(node, flight)

    # if counter > 5: break

G.visualize()


# dataString = ""

# for node in allNodesList:
#     dataString += f'<node id="{node}"/>'
#     if node in flightsDict:
#         for dest in flightsDict[node]:
#             dataString += f'<edge id="{node}-{dest}" source="{node}" target="{dest}"/>'

# outString = f'<?xml version="1.0" encoding="UTF-8"?><graphml xmlns="http://graphml.graphdrawing.org/xmlns"xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd"><graph id="G" edgedefault="directed">{dataString}</graph></graphml>'

# outFile = open("graph.xml", "w")
# outFile.write(outString)
# outFile.close()
