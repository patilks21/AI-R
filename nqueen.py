n=int(input("enter number of queens"))
q=n
l=[]
for i in range(n):
	z=[]
	l.append(z)
	for j in range(n):
		l[i].append(0)
def addqueen(l,x,y):
	x1=x
	y1=y
	y2=y
	for i in range(n):
		l[i][y]=-1
	for i in range(n-x):
		x1+=1
		y1+=1
		y2-=1
		if y1<n:
			l[x1][y1]=-1
		if y2>-1:
			l[x1][y2]=-1
	l[x][y]=1
	return l
def check(l,x,y):
	f=0
	if l[x][y]==-1 or l[x][y]==1:
		f=1
	if f==1:
		return False
	else:
		return True
x=0
y=0
print(l)		
while q:
	
	res=check(l,x,y)
	if res:
		l=addqueen(l,x,y)
		q=q-1
		x=x+1
		y=0
		print(l)
	else:
		y=y+1
		if y>n-1:
			break;
	

