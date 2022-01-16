import os
import random
import time
import threading
import random
map= [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],["-","-","-","-","-","-","-","-","-","-"]]
J=[["0"," "," "],["0","0","0"]]
I=[[" "," ", " "," "],["0","0","0","0"]]
L=[[" "," ","0"],["0","0","0"]]
O=[["0","0"],["0","0"]]
S=[[" ","0", "0"],["0","0"," "]]
T=[["0","0", "0"],[" ","0"," "]]
Z=[["0","0", " "],[" ","0","0"]]
#J rotate
J1=[[" ","0"],[" ","0"],["0","0"]]
J3=[["0","0","0"],[" "," ","0"]]
J2=[["0","0"],["0"," "],["0"," "]]
#I Rotate
I1=[["0"],["0"],["0"],["0"]]
#L Rotate
L1=[["0","0","0"],["0"," "," "]]
L2=[["0","0"],[" ","0"],[" ","0"]]
L3=[["0"," "],["0"," "],["0","0"]]
#S Rotate
S1=[["0"," "],["0","0"],[" ","0"]]
#T Rotate
T1=[[" ","0"],["0","0"],[" ","0"]]
T2=[[" ","0"," "],["0","0","0"]]
T3=[["0"," "],["0","0"],["0"," "]]
#Z Rotate
Z1=[[" ","0"],["0","0"],["0"," "]]
os.system('cls' if os.name in ('nt', 'dos') else 'clear')
newmap=map
xdel=2
downx=2
brk=0
right=0
entered_value=""
Block=J
blck=0
rt=0
def printgame():
	mapasd=""
	Jasd=""
	for x in range(22):
		for y in range(10):
			mapasd+=map[x][y]
		mapasd+="\n"
	print(mapasd)
def rotate():
	while True:
		global rt
		global Block
		global blck
		inp=input()
		if(blck==1):
			if(inp=="u"):
				rt+=1
			if(inp=="r"):
				rt-=1
			if(rt==0):
				Block=J
			if(rt==1):
				Block=J1
			if(rt==2):
				Block=J2
			if(rt==3):
				Block=J3
			if(rt==4):
				rt=0
			if(rt<0):
				rt=3
		if(blck==2):
			if(inp=="u"):
				rt+=1
			if(inp=="r"):
				rt-=1
			if(rt==0):
				Block=I
			if(rt==1):
				Block=I1
			if(rt==2):
				rt=0
			if(rt<1):
				rt=3
		if(blck==3):
			if(inp=="u"):
				rt+=1
			if(inp=="r"):
				rt-=1
			if(rt==0):
				Block=L
			if(rt==1):
				Block=L1
			if(rt==2):
				Block=L2
			if(rt==3):
				Block=L3
			if(rt==4):
				rt=0
			if(rt<0):
				rt=3
		if(blck==4):
			Block=O
		if(blck==5):
			if(inp=="u"):
				rt+=1
			if(inp=="r"):
				rt-=1
			if(rt==0):
				Block=S
			if(rt==1):
				Block=S1
			if(rt==2):
				rt=0
			if(rt<0):
				rt=1
		if(blck==6):
			if(inp=="u"):
				rt+=1
			if(inp=="r"):
				rt-=1
			if(rt==0):
				Block=T
			if(rt==1):
				Block=T1
			if(rt==2):
				Block=T2
			if(rt==3):
				Block=T3
			if(rt==4):
				rt=0
			if(rt<0):
				rt=3
		if(blck==7):
			if(inp=="u"):
				rt+=1
			if(inp=="r"):
				rt-=1
			if(rt==0):
				Block=Z
			if(rt==1):
				Block=Z1
			if(rt==2):
				rt=0
			if(rt<0):
				rt=1
def start():
	global brk
	global xdel
	global downx
	global right
	global Block
	global blck
	xdel=2
	downx=2
	brk=0
	right=0
	list1 = [1, 2, 3, 4, 5, 6,7]
	blck=random.choice(list1)
	if(blck==1):
		Block=J
	if(blck==2):
		Block=I
	if(blck==3):
		Block=L
	if(blck==4):
		Block=O
	if(blck==5):
		Block=S
	if(blck==6):
		Block=T
	if(blck==7):
		Block=Z
	alma=0
	try:
		for x in range(6):
			for y in range(6):
				map[x][y+right]=Block[x][y]
	except:
		alma+=1
def move():
	while True:
		global left 
		global right
		inp=""
		inp=input()
		if(inp=="j"):
			right+=1
			os.system('cls' if os.name in ('nt', 'dos') else 'clear')
			printgame()
		if(inp=="f"):
			right-=1
			os.system('cls' if os.name in ('nt', 'dos') else 'clear')
			printgame()
def fasz():
	global right
	while True:
		if(right>10):
			right=10
		if(right<0):
			right=0
def falling():
	global xdel
	global downx
	global brk
	global right
	global Block
	alma=0
	brk=0
	for x in range(20):
		for y in range(10):
			try:
				if(map[downx+1][y+right]!=" "):
					brk+=1
					break	
				map[x+downx][y+right]=Block[x][y]
				map[x+downx+1][y+right]=Block[x+1][y]
			except:
				alma+=0
	for x in range(xdel):
		for y in range(10):
			if(brk==20):
				return
			map[x][y]=" "
	xdel+=1
	downx+=1
start()
th = threading.Thread(target = move)
th.start()
asd = threading.Thread(target = fasz)
asd.start()
rot = threading.Thread(target = rotate)
rot.start()
for x in range(10):
	for x in range(20):
		printgame()
		print(right)
		print(rt)
		print(blck)
		time.sleep(1)
		falling()	
		if(x==20):
			os.system('cls' if os.name in ('nt', 'dos') else 'clear')
			printgame()
			break
		os.system('cls' if os.name in ('nt', 'dos') else 'clear')
	start()
input()