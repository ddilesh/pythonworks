class studentrecord:
    def __init__(self,name,grade,department):
        self.name=name
        self.grade=grade
        self.department=department

    def printinfo(self):
        print("Name of the Student" ,self.name)
        print("Student Grade" ,self.grade)
        print("Student Department" ,self.department)
        
    def updategrade(self,new_grade):
        new_grade=self.grade
        print("Updated grade",new_grade )
if __name__ == "__main__":
    
    student1 = studentrecord("Hari", "A", "Computer Science")
    student2 = studentrecord("Anita", "B+", "Mechanical")
    student3 = studentrecord("Ravi", "C", "Electrical")
  
    Students=[student1,student2,student3]

    print("Each Students info")
    for s in Students:
       s.printinfo()
    print("Update Grade")

    student3.updategrade("B-")

    print("Updated Records")

    for s in Students:
       s.printinfo()

    


        
