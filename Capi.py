Input = input("Enter a sentance in lower case: ").lower()

u = Input.replace(".", " ")	#replacing . ,if there are any
l = u.split(" ")	#splitting the words in the Input string.

for i in l:
	print(i.capitalize()," ", end = "")		#the capitalize method will make the first letter of a word Capital.
print()