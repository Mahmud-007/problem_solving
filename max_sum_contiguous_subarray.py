# O(n*n)
def first_approach(array):
    l = len(array)
    max_value = current_value = array[0]
    for i in range(1,l):
        if (array[i]>max_value):
            max_value = array[i]
        current_value = array[i]
        for j in range(i+1,l):
            current_value+=array[j]
            if (current_value>max_value):
                max_value = current_value
    return max_value
def main():
    n = int(input("size of list: "))
    array = []
    for i in range(0,n):
        e = int (input())
        array.append(e)

    print("first approach",first_approach(array))

if __name__ == '__main__':
    main()