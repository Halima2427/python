class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
        self.tail=None

    #INSERTING THE NODE BY SINGLY LINKED LIST
    #---------------------------------------
    
    def ins_at_beg(self,data):
        newnode=Node(data)
        if(self.head==None):
            self.head=self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode

    def ins_at_end(self,data):
        newnode=Node(data)
        if(self.head==None):
            self.head=self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode


    def ins_at_pos(self,data,pos):
        newnode=Node(data)
        if(self.head==None):
            self.head=self.tail=newnode
        else:
            temp=self.head
            for i in range(1,pos):
                temp=temp.next
            newnode.next=temp.next
            temp.next=newnode
    

    #DELETING THE NODE BY SINGLY LINKED LIST
    #---------------------------------------
    def del_at_beg(self):
        if(self.head==None):
            print("List is empty")
        else:
            temp1=self.head
            self.head=temp1.next
            temp1=None 

    def del_at_end(self):
        if(self.head==None):
            print("There is no node in tail")
        else:
            temp1=self.head
            while (temp1.next!=None):
                if(temp1.next==self.tail):
                    break
                temp1=temp1.next
            temp1.next=None
            self.tail=temp1
    def del_at_pos(self,pos):
        if(self.head==None):
            print("list is empty")
        else:
            if pos is 0:
                print("go to option delete at beginning")
                return
            curnode=self.head
            curpos=0
            while True:
                if curpos==pos:
                    prevnode.next=curnode.next
                    curnode.next=None
                    break
                prevnode=curnode
                curnode=curnode.next
                curpos+=1
#Search
    def search(self,data):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while temp!=None:
                if temp.data==data:
                    print("value found")
                else:
                    print("value not found")
                temp=temp.next
            
#update
    def update(self,data,data1):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.data is not data):
                if(temp.next is not None):
                    temp=temp.next
                break
            temp.data=data1
            


#Display
    def display(self):
            temp=self.head
            while(temp is not None):
                print(temp.data,end=" ")
                temp=temp.next

    
sll1=Sll()
print("-----------WELCOME TO SINGLY LINKED  LIST----------")
while(True):
    print("Enter the option 1.Insert 2.Delete 3.Search 4.Update 5.Display")
    option=input()

    if option=="1":
        print("Enter the choice 1.At Beginning 2.At End 3.At Any Position ")
        choose=input()
        if choose=="1":
            data=input("enter the data :")
            sll1.ins_at_beg(data)
        elif choose=="2":
            data=input("enter the data :")
            sll1.ins_at_end(data)
        elif choose=="3":
            data=input("enter the data :")
            pos=int(input("enter the position:"))
            sll1.ins_at_pos(data,pos)      
            
    if option=="2":
        print("Enter the choice 1.At Beg 2.At End 3.At Any Position")
        choose=input()                       
        if choose=="1":
            sll1.del_at_beg()    
        elif choose=="2":
            sll1.del_at_end()
        elif choose=="3":
            print("Enter pos to be deleted")
            pos=int(input())
            sll1.del_at_pos(pos)
        
    if option=="3":
        data=input("Enter value to be searched  :")
        sll1.search(data)

    if option=="4":
        data=input("Enter the value to be updated")
        data1=input("Enter the new value")
        sll1.update(data,data1)

    if option=="5":
        sll1.display()
    
    



   





    