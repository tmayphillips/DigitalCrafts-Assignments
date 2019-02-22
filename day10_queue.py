class Queue:
    def __init__(self):
        self.queue = list()
    
    def enqueue(self,value):
        self.queue.insert(0,value)

    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop()
        else:
            return ("Queue Empty!")

    def __repr__(self):
        return self.queue

 

queue = Queue() 

queue.enqueue(10) 
print(queue.queue)
queue.enqueue(12) 
print(queue.queue)
queue.enqueue(45) 
print(queue.queue)
queue.dequeue()  
print("return 10") 
print(queue.queue)
queue.dequeue()  
print("return 12")
print(queue.queue)
queue.dequeue() 
print("returns 45")
print(queue.queue)

queue.dequeue() ## what should happen if there are no items left in the queue

