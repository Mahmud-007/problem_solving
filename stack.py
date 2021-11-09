max_size=5
def create_stack():
    stack=[]*max_size
    return stack

def push_stack(stack,item):
    if (len(stack)==max_size):
        print("Overflow")
        return 
    stack.append(item)
    print(item,"added")

def pop_stack(stack):
    if (len(stack)==0):
        print("Empty")
        return
    stack.pop()

def main():
    demo_stack = create_stack()
    pop_stack(demo_stack)
    push_stack(demo_stack,"lsdkjf")
    push_stack(demo_stack,"lsdkjf")
    push_stack(demo_stack,"lsdkjf")
    push_stack(demo_stack,"lsdkjf")
    push_stack(demo_stack,5)
    push_stack(demo_stack,5)

if __name__ == '__main__':
    main()