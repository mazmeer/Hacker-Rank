def is_leap(year):
    leap = False
    
    if year == year%4:
        if year == year%100 and year != year%400:
            leap = False
            
        if year == year%100 and year == year%400:
            leap = True
    print(leap)     
    return leap
    

year = int(input())