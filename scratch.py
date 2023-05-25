numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
names = ["Aminah", "Aisha", "Cynthia", "Mwende",]
#print first index as a mispled value
names[0] = "Amina"
print(names[0:3])
print(names)
#insert a value at the beginning of a list.
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1)
print(numbers)
#remove a value on a list
numbers = [1, 2, 3, 4, 5]
numbers.remove(4)
print(numbers)
#clear values in a list
numbers =[1, 2, 3, 4, 5]
numbers.clear()
print(numbers)