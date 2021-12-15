def permute(given,l,r):
    if l==r:
        print(returnString(given))
    else:
        for i in range(l,r):
            given[l],given[i] = given[i],given[l]
            permute(given,l+1,r)
            given[l],given[i] = given[i],given[l]

def returnString(list):
    return ''.join(list)

string = "ABCD"
n = len(string)
a = list(string)
permute(a, 0, n)