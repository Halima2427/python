class human:
    """this halima syed from panruti 
    studied mtch in smvec"""
    def __init__(self,n,o):
        self.name=n
        self.occupation=o

    def do_work(self):
        print("self is:",self)
        if self.occupation=='leader':
            print(self.name,"is a leaader ")
        elif self.occupation=='olympics player':
            print(self.name,"is a olympics player")
    
    def speaks(self):
        print(self.name,"says hello!!!!")

    def _del_(self):
        class_name=self.__class__.__name__
        print(class_name,"destroyed")

        

print(human.__doc__)    
hit=human("syed","leader")
hit.do_work()
hit.speaks()


mar=human("halima","olympics player")
mar.do_work()
mar.speaks()