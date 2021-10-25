import animation

def createBubbleSortAnim(aLen):
	sortName = "bubbleSort"
	displayName = "Bubble Sort"
	animation.createAnimation(sortName, displayName, aLen)

def runbubbleSort(A):
	swapped = True		
	for i in range(len(A) - 1):
		if not swapped:
			return
		swapped = False			
		for j in range(len(A) - 1 - i):
			if A[j] > A[j + 1]:
				swap(A, j, j + 1)
				swapped = True
			yield A


def swap(A, i, j):
	A[i], A[j] = A[j], A[i]