class employee:
    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id

class tester(employee):
     def __init__(self, name,employee_id):
      super().__init__(name,employee_id)
   
     def run_tests(self):
       print(f"{self.name} is runnimg automation tests")

p1=tester("Smoke",102)
p2=tester("Regression",405)

p1.run_tests()
p2.run_tests()
        
        