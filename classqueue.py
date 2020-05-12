class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def enque(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.head
            self.head=newnode

    def deque(self):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.next is not None):
                prev = temp
                temp = prev.next
            self.tail=prev
            self.tail.next=None

    def search(self,key):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.data is not key):
                if(temp.next is not None):
                    temp=temp.next
                else:
                    print("Value is not found in the list")
                    break
            else:
                print("Value is found")
            temp=None

    def update(self,newv):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.data=temp

    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

sqq=Queue()
print("Welcome to Queue")
while(True):
    print("Menu")
    print("Which below operations need to be performed?")
    print("1. Enque")
    print("2. Deque")
    print("3. Search")
    print("4. Update")
    print("5. Display")
    print("6. Exit")
    n=int(input())
    if(n is 1):
        print("Enter value to be enqued")
        data=int(input())
        sqq.enque(data)
    elif(n is 2):
        sqq.deque()
    elif(n is 3):
        print("Enter value to be searched")
        data=int(input())
        sqq.search(data)
    elif(n is 4):
        print("Enter the new value")
        data=int(input())
        sqq.update(data)
    elif(n is 5):
        sqq.display()
    elif(n is 6):
        exit()
    else:
        print("Invalid input")
