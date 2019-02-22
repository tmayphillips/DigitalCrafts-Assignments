stack = [] 

class Stack: 
    def push(self,value): 
        stack.append(value) 
        print(f"{value} pushed to stack") 
      
    def pop(self): 
        stack.pop() 
        print("stack popped")

    def __repr__(self):
        return self.value


trial = Stack()
trial.push("abc")
print(stack)
trial.push("...lmn...")
print(stack)
trial.push("xyz")
print(stack)
trial.pop()
print(stack)