from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt
import json
import math

positionList = {}
destList = []
originList = []
height = 1030
width = 2000
flightNumDict = {}
departuresList = []
destinationsList = []

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
        
        destSizes = [flightNumDict[i] for i in list(set(destinationsList))]
        originSizes = [flightNumDict[i] for i in list(set(originList))]
        
        nodes = nx.draw_networkx_nodes(G, positionList, nodelist=list(
            set(destinationsList)), node_color="blue", alpha=.95, node_size=destSizes)
        nodes = nx.draw_networkx_nodes(G, positionList, nodelist=list(
            set(originList)), node_size=originSizes, node_color="red", alpha=.95)
        edges = nx.draw_networkx_edges(
            G,
            positionList,
            arrowstyle="->",
            arrowsize=20,
            width=.5,
            alpha=.7

        )
        label_options = {"ec": "k", "fc": "blue", "alpha": 0.7}
        nx.draw_networkx_labels(
            G, positionList, font_size=7, font_color="white", bbox=None)
        img = plt.imread("Equal_Earth_projection.jpg")
        plt.imshow(img)
        plt.subplots_adjust(bottom=0.05, right=1, top=.95, left=0)
        plt.show()


def cordsToPixels(lat, lon):
    A1 = 1.340264
    A2 = -0.081106
    A3 = 0.000893
    A4 = 0.003796
    theta = math.asin(math.sqrt(3)/2 * math.sin(lat * math.pi/180))
    x = (2 * math.sqrt(3) * lon * math.cos(theta)) / \
        (3 * (9 * A4 * theta**8 + 7*A3*theta**6 + 3*A2*theta**2 + A1))
    y = A4 * theta**9 + A3 * theta ** 7 + A2 * theta**3 + A1*theta
    x = x*6.6
    y = y*380
    x += 2060/2
    y = 1008/2 - y
    return [x, y]


fullDataList = []
with open("fullValidFlightData.json") as file:
    fullDataList = json.loads(file.read())
    file.close()


flightsDict = {}
G = GraphVisualization()

destinationDict = {}

print(cordsToPixels(0, 0))
print(cordsToPixels(90, 0))

for flight in fullDataList:
    departuresList.append(flight["origin"]["name"])
    destinationsList.append(flight["destination"]["name"])
    compensation = .4

    G.addEdge(flight["origin"]["name"], flight["destination"]["name"])

    positionList[flight["origin"]["name"]] = cordsToPixels(
        flight["origin"]["lat"], flight["origin"]["lon"])
    positionList[flight["destination"]["name"]] = cordsToPixels(
        flight["destination"]["lat"], flight["destination"]["lon"])
    
    destinationsList.append(flight["destination"]["name"])
    originList.append(flight["origin"]["name"])
    
    if flight["origin"]["name"] in flightNumDict.keys():
        flightNumDict[flight["origin"]["name"]] +=10
    else:
        flightNumDict[flight["origin"]["name"]] = 50
        
    if flight["destination"]["name"] in flightNumDict.keys():
        flightNumDict[flight["destination"]["name"]] +=10
    else:
        flightNumDict[flight["destination"]["name"]] = 50


allNodesList = list(set(departuresList + destinationsList))
departuresList = list(set(departuresList))
destinationsList = list(set(destinationsList))

print(f"There are {len(allNodesList)} nodes total with {len(departuresList)} departure cities and {len(destinationsList)} destination cities.")

G.visualize()
