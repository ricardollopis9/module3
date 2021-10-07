blocks = int(input("Introduce el numero de bloques: "))
height = 0
layer = 1

while layer <= blocks: 
    height += 1
    blocks -= layer
    layer += 1

print(height)

