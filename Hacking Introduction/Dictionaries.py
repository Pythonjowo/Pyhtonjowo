drink = {"White Rusian": 7, "Old Fashion": 10, "Lemon Drop": 8}
print(drink)

employeers = {"Finance":["Bob","Linda","Tina"],"IT":["Gene","Lousie","Teedy"], "HR": ["Jimmy","Jr.","Mort"]}
print(employeers)
print('\n')
employeers['Legal'] = ["Mr. Frond"] #Add New Key:Value Pair
print(employeers)

employeers.update({"Sales": ["Andie","Ollie"]})
print(employeers)

drink['White Russian'] : 8
print(drink)

print(drink.get("White Russian"))
