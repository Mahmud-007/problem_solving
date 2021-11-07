def counting_sort(unsorted_list):
    l = len(unsorted_list)
    store = [0]*100
    max_value = 0
    for i in range(l):
        temp = unsorted_list[i]
        store[temp] = store[temp] + 1
        if (temp > max_value):
            max_value = temp
    if (l>max_value):
        max_value =l
    ans = []
    for i in range(max_value):
        if (store[i]!=0):
            for j in range(store[i]):
                ans.append(i)

    for i in range(len(ans)):
        print(ans[i])

def main():
    n = int(input("size of list: "))
    unsorted_list = []
    for i in range(0,n):
        e = int (input())
        unsorted_list.append(e)

    counting_sort(unsorted_list)

if __name__ == '__main__':
    main()