class MyQueue:

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
        

    def push(self, x: int) -> None:
        self.enqueue_stack.append(x)


    def dequeue(self):
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            return
        
        if len(self.dequeue_stack) == 0:
            
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()
        
        
    def pop(self) -> int:
        return self.dequeue()
   
    def peek(self) -> int:
        if len(self.dequeue_stack) > 0:
            return self.dequeue_stack[-1]
    
    def empty(self) -> bool:
        return self.enqueue_stack == []
    
    
    

queue = MyQueue()

queue.push(1)
queue.push(2)

print(queue.peek())
print(queue.pop())
print(queue.empty())