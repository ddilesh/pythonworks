marks =[78,85,62,90,55,88]
print(max(marks))
print(min(marks))
print(sum(marks)/len(marks))
marks.append(95)
print(marks)
marks.remove(55)
print(marks)
marks.sort() 
print(marks)   
for mark in marks:
    if mark>=75:
        print(mark)