#While Loop

count = 0
while (count < 9):
    print("The count is: ", count)
    count = count + 1
print("Good Bye!")

#For Loop
angka = [1,2,3,4,5]
for x in angka:
    print(x)

#contoh perulangan lain

buah = ["Nanas","apel","Jeruk"]
for makanan in buah:
    print(makanan)


i = 2
while(i < 3):
    j = 2
    while(j <= (i/j)):
        if not(i%j):break
        j = j +1
    if (j > i/j) : print(i, "is prime")
print("Good Bye!")

i = 5
j = 10
x = i/j
m = i%j
print(x)
print(m)
