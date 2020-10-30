
#conditional Statments
def drink(money):
    if money >= 2:
        return "You've Gt yourself a Drink"
    else:
        return "No drink For YOu"

print(drink(3))
print(drink(1))
print('\n')
def alcohol(age,money):
    if (age >= 21) and (money >=5):
        return "We're Getting a Drink"
    elif (age >= 21) and (money <= 5):
        return "Come back with more Money"
    elif (age < 21) and (money >= 5):
        return "Nice Try,Kid!"
    else:
        return "You 're too poor and too Young "
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))

