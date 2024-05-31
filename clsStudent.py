


class Stud1:  # outerclass
    def __init__(self, name, roll_no,a,u):
        self.name = name 
        self.roll_no = roll_no
        self.uselap=self.Lap(a,u)
        # self.lap1 = self.Laptop()
    def show(self):  # what method is this? #instance method #accessors
        print(self.name, self.roll_no)   
        # self.lap1.show()
    class Lap: #innerclass
        def __init__(self,model,cpu):
            self.model = model  
            self.cpu = cpu     
        def showval(self):
            print(self.model,self.cpu)    
s1=Stud1("John",9876, "Macbook pro","i5")
print(s1.uselap.cpu)






#     class Laptop:  # innerclass

#         def __init__(self):
#             self.model = 'hp'
#             self.cpu = 'i5'
#             self.ram = '8gb'

#         def show(self):
#             print(self.cpu, self.model, self.ram)


# s1 = Stud1('hari', 26)
# s2 = Stud1('aslam', 42)

# print(s1.show())
# print(s2.show())
   
