import random

taskNum = 200 # number of tasks
vmNum = 30 # number of VMs
genNum = 200 # number of genetic generations 
solNum = 20 # number of generated solutions

tasks = [random.randint(1000, 10000) for _ in range(taskNum)]
VMs = [random.randint(2000, 8000) for _ in range(vmNum)]
taskTime = [random.randint(10, 60) for _ in range(taskNum)]
assign = [0 for _ in range(taskNum)]  # List for assigned tasks
makeSpan = [0 for _ in range(vmNum)]  # list for Time of accepted tasks, so we can get the MakeSpan from it's MAXIMUM Value
msRatio = 0.7
nrtRatio = 0.3
mutationChance = 10 # as in 10% chance of Mutation

def hueristic(tasks, taskTime, VMs) -> tuple:
	solution = [0 for _ in range(taskNum)]  # List for assigned tasks
	makeSpan = [0 for _ in range(vmNum)]  # list for makeSpan

	for i in range(taskNum):
		task = tasks[i]
		vm = min(makeSpan)
		j = makeSpan.index(vm)
		time = task/VMs[j]
		if(makeSpan[j]+time<taskTime[i]):
			solution[i] = j
			makeSpan[j] = makeSpan[j]+time
			makeSpan[j] = round(makeSpan[j],2)
		else:
			solution[j] = -1 # reject the task

	return (makeSpan, solution)

def calcNRT(solution):
	nrt = 0
	for i in range(taskNum):
		if (solution[i] == -1):
			nrt = nrt + 1
	return nrt

def calcMS(solution):
	makeSpan = [0 for _ in range(vmNum)]
	for i in range(len(solution)):
		vm = solution[i]
		if vm>-1:
			mi = tasks[i]
			makeSpan[vm] += mi/VMs[vm]
	result = list(map(lambda x:round(x,2),makeSpan)) # rounding the numbers in the makeSpan list
	return result

def initializeSolutions(solNum):
	solutions = []
	for i in range(solNum):
		solution = [0 for _ in range(taskNum)]
		makeSpan = [0 for _ in range(vmNum)]
		nrt = 0
		for j in range(taskNum):
			task = tasks[j] # task power 
			vm = random.randint(0,vmNum-1) # assign random VM
			time = task/VMs[vm] # calculate runTime
			if(makeSpan[vm]+time<taskTime[j]): # if there is time
				solution[j] = vm
				makeSpan[vm] = makeSpan[vm]+time
			else:
				solution[j] = -1 # reject the task

		solutions.append(solution)
	return solutions

def calcScore(solution):
	nrt=0
	for i in solution:
		if i==-1:
			nrt=nrt+1
	makeSpan = max(calcMS(solution))
	score = round((makeSpan*msRatio)+(nrt*nrtRatio),2)
	return score

def crossOver(s1,s2):
	half = (len(s1)/2)+1
	child1 = s1[:int(half)]+s2[int(half):]
	child2 = s2[:int(half)]+s1[int(half):]
	return child1,child2

def mutation(solution):
	i = random.randint(0, taskNum-1)
	oldVM = solution[i]
	newVM = random.randint(0, vmNum-1)
	if(newVM>=vmNum): # if the VM we got is out of range we give it to the first VM
		newVM = 0
	oldTime = tasks[i]/VMs[oldVM] # get the time for the old VM for we can decrease it 
	newTime = tasks[i]/VMs[newVM] # i is the task
	if(makeSpan[newVM]+newTime<taskTime[i]): # test if the task can be assigned 
		makeSpan[oldVM] = makeSpan[oldVM]-oldTime
		makeSpan[newVM] = makeSpan[newVM]+newTime
		solution[i] = newVM
	else: # reject the task
		solution[i] = -1
	return solution

solutions = initializeSolutions(solNum) # initialize the Solutions

for k in range(genNum): # Genetic code for 100 generations
	solutions.sort(key=calcScore) # sort the solution by their score
	solutions = solutions[:20] # get the 20 best parents
	children = [] # list for children
	for i in range(0,20,1): # crossover the parents to make new children
		p1 = random.randint(0,6) # take two random parents
		p2 = random.randint(6,len(solutions)-1)
		while(p1==p2): # check that the parents are not the same
			p2 = random.randint(0,len(solutions)-1)
		c1, c2 = crossOver(solutions[p1],solutions[p2])
		children.append(c1) # add the crossover to the children list
		children.append(c2)
	solutions = solutions + children # add the created children to our first list

for i in range(solNum): # Mutation time
	j = random.randint(0, 100) # create a random number to determine whether we should mutate or not
	if(j>=(100-mutationChance)):
		mutation(solutions[i])
		#print("Solution "+str(i)+" mutated.")

hueristicMS, hSolution = hueristic(tasks, taskTime, VMs)

genNRT = calcNRT(solutions[0])
hueNRT = calcNRT(hSolution)

print("Genetic NRT (with Mutation): "+str(genNRT))
print("Genetic MakeSpan (100 Gens with Mutation): "+str(max(calcMS(solutions[0])))) # print best solution makeSpan

print("NRT for Hueristic: "+str(hueNRT))
print("Hueristic MakeSpan: "+str(max(hueristicMS)))









	
		
