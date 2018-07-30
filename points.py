def create():
	with open("out.obj", 'w') as f:
		f.write("# OBJ file\n")
		f.write("o Point_Cloud.001\n")
		f.close()

def pointswrite(x,y,z):
	with open("out.obj", 'a+') as f:
		f.write("v "+str(x)+" "+str(y)+" "+str(z)+" "+"\n")
		f.close()

def finish(point):
	with open("out.obj", 'a+') as f:
		for n in point:
			pointswrite(n[0], n[1], n[2])
#create()
#a = [[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5],[6,6,6]]
#finish(a)
