import sys

def selection_sort(unsorted_list):
    l = len(unsorted_list)
    for i in range(l):
        pivot = i
        for j in range(i+1,l):
            if (unsorted_list[j] < unsorted_list[pivot]):
                pivot = j
        #swap
        unsorted_list[i],unsorted_list[pivot] = unsorted_list[pivot],unsorted_list[i]
    #printing array
    for i in range(0,l):
        print(i," ",unsorted_list[i])
def main():
    n = int(input("size of list: "))
    unsorted_list = []
    for i in range(0,n):
        e = int (input())
        unsorted_list.append(e)

    selection_sort(unsorted_list)

if __name__ == '__main__':
    main()