
graph=[]
heuristic=[]
ol=[]
cl=[]
def heuristiccost(graph,heuristic,olist,clist):
	cost=[]
	pathlen=0
	for i in range(len(clist)-1):
		pathlen=pathlen+graph[clist[i]][clist[i+1]]
	last=clist[-1]
	for i in range(len(olist)):
		cost[i]=pathlen+graph[last][olist[i]]+heuristic[olist[i]]
	return cost
n=int(input("no. of nodes"))
for i in range(n):
	z=[]
	graph.append(z)
	for j in range(n):
		graph[i].append(0)

e=int(input("no. of edges"))

for i in range(e):
	a=int(input("node 1"))	
	b=int(input("node 2"))
	c=int(input("cost"))
	graph[a][b]=c
	graph[b][a]=c
for i in range(n):
	heuristic.append(int(input("heuristic value for"+str(i))))
current=int(input("enter current node"))
goal=int(input("enter goal node"))

while current!=goal:
	for i in range(n):
		if graph[current][i]!=0:
			ol.append(i)
	cl.append(current)
	olcost=heuristiccost(graph,heuristic,ol,cl)
	pos=olcost.index(min(olcost))
	cl.append(ol[pos])
	current=ol[pos]
	ol.clear()
print(cl)
