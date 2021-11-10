from queue import *

class FakeStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.current_size=0

    def push(self,item):
        self.q2.put(item)
        self.current_size+=1
        while(not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        self.q1,self.q2 = self.q2,self.q1

    def pop(self):
        if (self.q1.empty()):
            return
        self.q1.get()
        self.current_size-=100

    def top(self):
        if self.q1.empty():
            return -1
        return self.q1.queue[0]

def main():
    s = FakeStack()
    s.push(1)
    s.push(2)
    s.push(3)
 
    print("current size: ", s.current_size)
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
 
    print("current size: ", s.current_size)

if __name__ == "__main__":
    main()