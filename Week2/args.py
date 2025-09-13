def calculate_salary(basic,hra,da,bonus=0) :
    totalsal=basic+hra+da+bonus
    return totalsal

totalwithbonus=calculate_salary(1000,100,30,70)
totalwithoutbonus=calculate_salary(1000,100,30)
print(totalwithbonus)
print(totalwithoutbonus)