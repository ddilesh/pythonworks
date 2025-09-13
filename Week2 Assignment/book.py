import datetime

class book:
  def  __init__(self,title,author,publicationyear):
   self.title=title
   self.author=author
   self.publicationyear=publicationyear

  def get_age(self):
    current_year=datetime.datetime.now().year
    return current_year-self.publicationyear
book1=book("My book","Hari",2009)
print("Book Age :",book1.get_age(),"Years")
