print("Dime tu nota: ")
nota = float(input())

if nota < 5:
    print("Fail")
elif nota < 6:
    print("Enough")
elif nota < 7:
    print("Good")
elif nota < 9:
    print("Very Good")
else: 
    print("Excellent")
