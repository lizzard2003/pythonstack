

class Stack:
    def __init__(self) : #init is a constructor 
        # we are creating an object called stack
        self.items= [] # creating an empty list 

    def is_empty(self): # method to check to see if the stack is empty

        return not self.items
    
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self) -> str: # this enables us to use the print statement to inspect our stack 
        return str(self.items)
    
if __name__ == "__main__":
    s = Stack() # the lowecase s is the object this is calling the constructor
    #print(s)
    #print(s.is_empty())
    s.push(3)
    print(s)
    s.push("Hello")
    s.push(9.5)
    s.push(-10)
    print(s)
    print(s.size()) # these are methods and they need the parenthesis to work if you will get an error 
    print(s.pop())
    print(s)
    print(s.peek())