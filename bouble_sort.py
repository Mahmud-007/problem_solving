def bouble_sort(unsorted_list):
    l = len(unsorted_list)
    
    for i in range(l):
        for j in range(0,l-i-1):
            if (unsorted_list[j]>unsorted_list[j+1]):
                unsorted_list[j],unsorted_list[j+1] = unsorted_list[j+1],unsorted_list[j]
    #print
    print ("printing ans")
    for i in range(l):
        print(unsorted_list[i])

def main():
    n = int(input("size of list: "))
    unsorted_list = []
    for i in range(0,n):
        e = int (input())
        unsorted_list.append(e)

    bouble_sort(unsorted_list)

if __name__ == '__main__':
    main()