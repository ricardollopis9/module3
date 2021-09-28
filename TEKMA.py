zone3 = 0
zone4 = 0
zone5 = 0
cont = 0
age = int(input("Introduce la edad: "))
bpm = int(input("Introduce bpm: "))

while True:
    bpm = int(input("Introduce bpm: "))
    if bpm < 1:
        break

    cont += 1
    print("bpm: " , bpm)

    if bpm < int((220 - age) * 0.7) :
        zone3 += 1
    elif bpm < int((220 - age) * 0.8):
        zone4 += 1
    elif bpm < int((220 - age) * 0.9):
        zone5 += 1

    
    

zone3 = zone3 / cont * 100
print("Zona3 (<" , int((220 - age) * 0.7) , "): " , zone3 , "%")

zone4 = zone4 / cont * 100
print("Zona4 (<" , int((220 - age) * 0.8) , "): " , zone4 , "%")

zone5 = zone5 / cont * 100
print("Zona5 (<" , int((220 - age) * 0.9) , "): " , zone5 , "%")