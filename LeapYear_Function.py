def is_leap(year):
    Leap = False
    
    
    if year%400 == 0 :
        Leap = True
        

    elif year%4 == 0 and year%100 != 0:
        Leap = True
        

    
    return Leap
    

year = int(input())
