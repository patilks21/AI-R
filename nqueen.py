n=int(input("enter number of queens"))
q=n
l=[]
qp=[]
for i in range(n):
	z=[]
	l.append(z)
	for j in range(n):
		l[i].append(0)
def colcheck(l,x,y):
	if y>n-1:
		return False
	s=True
	for i in range(n):
		if l[i][y]==1:
			s=False
	if s:
		return True
	else:
		return False
def dcheck(l,x,y):
	x1=x
	y1=y
	y2=y
	s=True
	for i in range(n):
		x1-=1
		y1-=1
		y2-=1
		if y1<n:
			if l[x1][y1]==1:
				s=False
		if y2>-1:
			if l[x1][y2]==1:
				s=False
	if(s):
		return True
	else:
		return False
def addqueen(l,x,y):
	l[x][y]=1
	return l
def check(l,x,y):
	tp=[x,y]
	if qp.count(tp)>1:
		print("x")
		return False
	s=False
	f=colcheck(l,x,y)
	if f:
		s=dcheck(l,x,y)
	if s:
		return True
	else:
		return False
def removequeen(l,x):
	for i in range(n):
		if l[x][i]==1:
			colpos=i
			l[x][i]=0
	return l
def getqueen(l,x):
	for i in range(n):
		if l[x][i]==1:
			return i
x=0
y=0
print(l)		
while q:
	
	res=check(l,x,y)
	if res:
		l=addqueen(l,x,y)
		pos=[x,y]
		qp.append(pos)
		q=q-1
		x=x+1
		y=0
		print(l)
	else:
		y=y+1
		if y>n-1:
			print("bt")
			x=x-1
			y=getqueen(l,x)
			l=removequeen(l,x)
			#pos=[x,y]
			#qp.remove(pos)
			print(l)
			y=y+1
			
	

