
T = int(input())

if T > 0:
    if (0 <= T <=5):
        print("NIGHT")
    elif (T <= 11):
        print("MORNING")
    elif(T <= 17):
        print("AFTERNOON")
    elif (T <= 23):
        print("EVENING")
    else:
        print("INVALID")
else:
    print("INVALID")
    
        