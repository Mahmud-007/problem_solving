
def getsumBIT(tree,index):
	sum = 0 
	index = index+1
	while index > 0:
		sum += tree[index]
		index -= index & (-index)
	return sum


def updateBIT(tree, n, index, value):
	index+= 1
	while index<= n:
		tree[index] += value
		index+= index& (-index)


def constructBIT(arr, n):
	tree = [0]*(n+1)
	for i in range(n):
		updateBIT(tree, n, i, arr[i])
	return tree



freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
tree = constructBIT(freq,len(freq))
print("Sum of elements in arr[0..5] is " + str(getsumBIT(tree,5)))
freq[3] += 6
updateBIT(tree, len(freq), 3, 6)
print("Sum of elements in arr[0..5]"+
					" after update is " + str(getsumBIT(tree,5)))


