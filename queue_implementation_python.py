max_size=5
def create_queue():
    queue=[]*max_size
    return queue

def enqueue(queue,item):
    if (len(queue)==max_size):
        print("Overflow")
        return 
    queue.append(item)
    print(item,"added")

def dequeue(queue):
    if (len(queue)==0):
        print("Empty")
        return
    item=queue.pop(0)
    print(item,"popped out")

def front(queue):
    print(queue[0],"is now front")

def main():
    demo_queue = create_queue()

    dequeue(demo_queue)

    enqueue(demo_queue,5)
    enqueue(demo_queue,"lsdkjf")
    enqueue(demo_queue,"lsdkjf")
    enqueue(demo_queue,"lsdkjf")

    front(demo_queue)

    enqueue(demo_queue,35)
    enqueue(demo_queue,35)

    front(demo_queue)

    dequeue(demo_queue)

    front(demo_queue)

    dequeue(demo_queue)
    dequeue(demo_queue)
    dequeue(demo_queue)
    dequeue(demo_queue)
    dequeue(demo_queue)
    dequeue(demo_queue)
    

if __name__ == '__main__':
    main()