# k of elements in set 1..n
# learned from https://www.geeksforgeeks.org/make-combinations-size-k/


def combination(left, k):
    if (k==0):
        for i in range(len(temp)):
            print(temp[i], end=' ')
        print()

    for i in range(left,n):
        temp.append(a[i])
        combination(i+1,k-1)
        temp.pop()
        
a = [1,2,3,4,5]
temp = []
n = len(a)
combination(0,2)
