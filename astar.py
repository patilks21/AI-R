
class Node:

	def __init__(self, f=0, g=999999, h=0, name=0):
		self.f = f
		self.g = g
		self.h = h
		self.name = name
	
	def setNeighbours(self, neighbours={}):
		self.neighbours = neighbours



# assume a 5 node bidirectional graph as follows
graph=[]
heuristics=[]

n=int(input("no of nodes"))
for i in range(n):
	z=[]
	graph.append(z)
	for j in range(n):
		graph[i].append(int(input()))
for i in range(n):
	heuristics.append(int(input("heuristic value")))
Name=[]
for i in range(n):
	a=Node(h=heuristics[i], name=str(i))
	Name.append(a)
for i in range(n):
	ls=[]
	for j in range(n):
		if graph[i][j]!=-1:
			ls.append(Name[j])
	Name[i].setNeighbours(ls)



startNode = Name[int(input("Enter start node"))]
goalNode = Name[int(input("Enter goal node"))]


def astar(start,goal):

	closedSet = set([])
	openSet = set([start])

	cameFrom = {}
	
	start.g = 0
	start.f = start.h


	while len(openSet)!=0:

		current = findNodeWithLowestFScore(openSet)

		if current==goal:
			return contruct_path(cameFrom, current)

		openSet.remove(current)
		closedSet.add(current)

		#print(current.name, current.f, current.g, current.h)

		for neighbour in current.neighbours:

			#print(neighbour.name, neighbour.f, neighbour.g, neighbour.h)

			if neighbour in closedSet:
				continue

			if neighbour not in openSet:
				openSet.add(neighbour)


			tentative_gScore = current.g + graph[int(current.name)][int(neighbour.name)]
			#print(tentative_gScore)
			if tentative_gScore >= neighbour.g:
				continue

			cameFrom[neighbour] = current
			neighbour.g = tentative_gScore
			neighbour.f = neighbour.g + neighbour.h



	return -1

def findNodeWithLowestFScore(openSet):
	fScore = 999999
	node = None
	for eachNode in openSet:
		if eachNode.f < fScore:
			fScore = eachNode.f
			node = eachNode

	return node


def contruct_path(cameFrom, current):

	totalPath = []
	while current in cameFrom.keys():
		current = cameFrom[current]
		totalPath.append(current)

	return totalPath



if __name__=="__main__":
	
	
	path = astar(startNode, goalNode)

	print("Path is : ", end="" )
	for node in path[::-1]:
		print(str(node.name) + "-->", end="")	
	print(goalNode.name)

	print("\nCost = " + str(goalNode.g))
