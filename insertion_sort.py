def insertion_sort(unsorted_list):
    l = len(unsorted_list)
    
    for i in range(1,l):
        j=i-1
        temp=unsorted_list[i]
        while(j>=0 and temp<unsorted_list[j]):
            unsorted_list[j+1]=unsorted_list[j]
            j-=1
        unsorted_list[j+1]=temp

    print("printing ans")
    for i in range(l):
        print(unsorted_list[i])

def main():
    n = int(input("size of list: "))
    unsorted_list = []
    for i in range(0,n):
        e = int (input())
        unsorted_list.append(e)

    insertion_sort(unsorted_list)

if __name__ == '__main__':
    main()