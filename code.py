#Importing modules; one might need to pip install ACO-pants & pip install matplotlib
import pants, math, random, time
import matplotlib.pyplot as plt


#Defining Variables
xx = []; yy = []; xp = []; yp = []; nodes=[]; p = 100


#Requesting for the amount of nodes.
q =int(input("Nodes: "))


#Start timing, can remove if you do not want to see how long it takes
s = time.time()


#Generating position/coordinates of nodes
for i in range(q):
    x=random.uniform(-10,10)
    y=random.uniform(-10,10)
    nodes.append((x,y))
    xx.append(x)
    yy.append(y)
    
    
# Euclidean function to find next nearest coordinate
def eucl(a,b):
    return math.sqrt(pow(a[1]-b[1],2)+pow(a[0]-b[0],2))


# This is to prevent the code from taking too long to process; [Optional](Remove this and change limit at Line 40 to 100)
if len(str(q)) == 2:
    p = 100
elif len(str(q)) == 3:
    p = 250
    print(f"Iterating Ant-Colony Optimization Algorithm {p} times for {q} Nodes, this may take awhile..")
elif len(str(q)) == 4:
    p = 500
    print(f"Iterating Ant-Colony Optimization Algorithm {p} times for {q} Nodes, this may take awhile..")
else:
    p = 1000
    print(f"Iterating Ant-Colony Optimization Algorithm {p} times for {q} Nodes, this may take awhile..")

    
#Implementing the ACO Algorithm
world=pants.World(nodes,eucl)
solver=pants.Solver(rho=0.5,q=1,t0=0.01,limit=p,ant_count=10)
solution=solver.solve(world)


#Solutions; [Optional](Remove if unwanted)
print(f"Solution Distance: {solution.distance}")
print(f"Coordinates: {solution.tour}")


#Finding the best solution through the iterations of the algorithm.
solutions=solver.solutions(world)
best=float("inf")

for solution in solutions:
    assert solution.distance < best
    best=solution.distance

    
#Timing the end of the process
e= time.time() - s


#Solutions; [Optional](Remove if unwanted)
print(f"Most Optimized Distance: {best}")
print(f"Time Taken: {e:.3f}s")


#Generating the coordinates on the best solution's path.
for i in range(len(solution.tour)):
    xp.append(solution.tour[i][0])
    yp.append(solution.tour[i][-1])
xp.append(solution.tour[0][0])
yp.append(solution.tour[0][-1])

    
#Plotting the coordinates and the best path
plt.scatter(xx,yy,s=5,c='r')
plt.title(f"{q} Scattered Nodes")
plt.plot(xp,yp,c='g')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
