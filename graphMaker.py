from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt
import json
import math

positionList = {}
height = 1030
width = 2000


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
        nodes = nx.draw_networkx_nodes(
            G, positionList, node_color="blue", alpha=.95, node_size=100)
        edges = nx.draw_networkx_edges(
            G,
            positionList,
            arrowstyle="->",
            arrowsize=10,
            width=.7,
            alpha=.8

        )
        label_options = {"ec": "k", "fc": "blue", "alpha": 0.7}
        nx.draw_networkx_labels(
            G, positionList, font_size=7, font_color="white", bbox=None)
        img = plt.imread("Equal_Earth_projection.jpg")
        plt.imshow(img)
        plt.subplots_adjust(bottom=0.1, right=1, top=.9, left=0)
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

departuresList = []
destinationsList = []
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

    # positionList[flight["origin"]["name"]] = [
    #     flight["origin"]["lon"], flight["origin"]["lat"]]
    # positionList[flight["destination"]["name"]] = [
    #     flight["destination"]["lon"], flight["destination"]["lat"]]

    # positionList[flight["origin"]["name"]] = [width * (flight["origin"]["lon"] + 180)/360, (height * (1 - (flight["origin"]["lat"] + 90)/180))]
    # positionList[flight["destination"]["name"]] = [
    #     width * (flight["destination"]["lon"] + 180)/360, (height * (1 - (flight["destination"]["lat"] + 90)/180))]

    positionList[flight["origin"]["name"]] = cordsToPixels(
        flight["origin"]["lat"], flight["origin"]["lon"])
    positionList[flight["destination"]["name"]] = cordsToPixels(
        flight["destination"]["lat"], flight["destination"]["lon"])


allNodesList = list(set(departuresList + destinationsList))
departuresList = list(set(departuresList))
destinationsList = list(set(destinationsList))

print(f"There are {len(allNodesList)} nodes total with {len(departuresList)} departure cities and {len(destinationsList)} destination cities.")

G.visualize()
