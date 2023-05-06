class Fruits:
    category = "Fresh natural fruit"
    def __init__(self,color,name,taste):
        self.name=name
        self.taste=taste
        self.color=color

    def wash(self):
        return f"The {self.color}  {self.name} is {self.taste} and produces {self.category} " 

    def peel(self):
        return f"They are peeling {self.color} {self.name} in the Kitchen but they are {self.category}"      
