import animation

def createInsertionSortAnim(aLen):
	sortName = "insertionSort"
	displayName = "Insertion Sort: O(n) -> O($n^2$)"
	animation.createAnimation(sortName,displayName, aLen)

def runinsertionSort(A):
	for i in range(1, len(A)):
		keyVal = A[i]
		j = i-1
		while (j >= 0 and keyVal < A[j]):
			A[j+1] = A[j]
			j -= 1
		A[j+1] = keyVal
		yield A

def swap(A, i, j):
	A[i], A[j] = A[j], A[i]