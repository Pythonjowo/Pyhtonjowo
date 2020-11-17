wight = int(input("Weight : "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = wight // 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = wight * 0.45
    print("Weight in Kgs: " + str(converted))