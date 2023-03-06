import random

taskNum = 300 # number of tasks
vmNum = 15 # number of VMs

tasks = [random.randint(1000, 10000) for _ in range(taskNum)]
VMs = [random.randint(2000, 8000) for _ in range(vmNum)]
taskTime = [random.randint(10, 60) for _ in range(taskNum)]
assign = [0 for _ in range(taskNum)]  # List for assigned tasks
makeSpan = [0 for _ in range(vmNum)]  # list for Time of accepted tasks, so we can get the MakeSpan from it's MAXIMUM Value

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

hueristicMS, hSolution = hueristic(tasks, taskTime, VMs)
print(hueristicMS, "\n", hSolution, "\n")