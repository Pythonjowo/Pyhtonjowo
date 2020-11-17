names = ["Jhony", "Bob","Mosh","Sam","Marry"]
names[0] = "Jhon"
print(names[0:3])

numbers = [1,2,3,4,5,6]
numbers.insert(0, 1)
print(numbers)
print(1 in numbers)
print(10 in numbers)
print(len(numbers))

print("\n")

number = [1,2,3,4,5]
for item in number:
    print(item)

i = 0
while i < len(number):
    print(number[i])
    i = i + 1


numbet = range(5, 10, 2)
print(numbet)
for bum in range(5):
    print(bum)


numb = (1,2,3,4,5)
numb.count(2)
numb.