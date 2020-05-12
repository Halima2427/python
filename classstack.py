class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    def insert(self,value):
        if(self.top==None):
            self.top=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.top
            self.top=newnode

    def delt(self):
        if(self.top==None):
            print("List is empty")
        else:
            temp=self.top
            self.top=temp.next
            temp=None

    def last(self):
        if(self.top==None):
            print("List is empty")
        else:
            temp=self.top
            print("Top pointer points to the value:")
            print(temp.data)

    def display(self):
        temp=self.top
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

ssl=Stack()
print("------------Welcome to Stack Implementation-----------------")
while(True):
    print("Menu")
    print("Which below operations need to be performed?")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    n=int(input())
    if(n is 1):
        print("Enter value to be pushed")
        val=int(input())
        ssl.insert(val)
    if n==2:
        ssl.delt()
    if n==3:
        ssl.last()
    if n==4:
        ssl.display()
    if n==5:
        exit()
    #else:
     #   print("Invalid input")
