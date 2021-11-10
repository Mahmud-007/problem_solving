array=[0,19,7,12,3,5,17,10,1,2]
length = len(array)

def left_child(parent):
    return parent*2

def right_child(parent):
    return parent*2+1

def find_parent(child):
    return child // 2

def max_heap(i):
    # for the easy calculation heap element will be form array[1] index
    # so the heap elements will be l = len(array)-1
    l = length-1

    left = left_child(i)
    right = right_child(i)

    if (left<l and array[left]>array[i]):
        largest=left
    elif(right<l and array[right]>array[i]):
        largest=right
    else:
        largest=i

    if (largest!=i):
        print(i)
        #print(array[i],"before",array[largest])
    
        array[i],array[largest] = array[largest],array[i]
        #print(array[i],"after",array[largest])
        max_heap(largest)
    
    
def print_heap():
    for i in range(1,length):
        print(array[i])

def heap_sort():
    i = length-1
    while(i>1):
        array[i],array[1]=array[1],array[i]
        i-=1
        max_heap(1)

def main():
    print_heap()
    # i=length 
    # while(i>=1):
    #     max_heap(i)
    #     i-=1
    heap_sort()
    print("AFTER")
    print_heap()

if __name__ == '__main__':
    main()
