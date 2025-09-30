class Student:                                    # class creation
    def __init__(self, name, marks):       # creating variables
        self.name = name    
        self.marks = marks                                                          
        print("info added successfully")        
        print("Candidate name", self.name)

    @staticmethod
    def hello():
        print("hello")

    def avg(self):              #  applying methord
        sum  = 0
        for val in (self.marks):            
            sum+= val
        print(f"avg score is: {sum/3}")


s1 = Student("sahil", [50, 55, 60])        # creating an object out of class
s1.avg()                             # calling methord  
s1.hello()     