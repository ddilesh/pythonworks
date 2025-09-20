class person:
    def __init__(self,name):
        self.name=name;
class employee(person):
    def __init__(self,name,employeeid):
        super().__init__(name)
        self.employeeid=employeeid

class manager(employee):
    def __init__(self, teamsize,employeeid,name):
        super().__init__(name,employeeid)
        self.teamsize=teamsize

    def showdetails(self):
        print(f"name : {self.name}")
        print(f"employeeid : {self.employeeid}")
        print(f"teamsize :{self.teamsize}")
m1 =manager("Alice", 101, 8)
m1.showdetails()


        
