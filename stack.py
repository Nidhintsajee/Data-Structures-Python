class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
	
s=Stack()
	
s.push(4)
s.push('dog')
s.push(True)
print("Stack: "+str(s.items))
print("Deleted : "+str(s.pop()))
print("Stack: "+str(s.items))
print("Size of Stack : "+str(s.size()))
print("Is Stack empty: "+str(s.isEmpty()))
print("Peek of Stack : "+str(s.peek()))
