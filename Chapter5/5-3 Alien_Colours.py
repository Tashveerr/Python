5-3 #Simple if statement

alien_colours = 'green'
if alien_colours == 'green':
	print('Player earned +5points')

#if else statement
alien_colours = 'yellow'
if alien_colours == 'green':
	print('Player earned +5points')
else:	
	print('No points')

5-4
alien_colours = 'green'
if alien_colours == 'green':
	print('Player earned 5points')
else:	
	print('Player earned 10 points')

alien_colours = 'yellow'
if alien_colours == 'green':
	print('Player earned 5points')
else:	
	print('Player earned 10 points')


5-5 

alien_colours = 'green'
if alien_colours == 'green':
	print('Player earned 5points')
elif alien_colours == 'yellow':
	print('Player earned 10 points')

else :
	print('Player earned 15 points')

alien_colours = 'yellow'
if alien_colours == 'green':
	print('Player earned 5points')
elif alien_colours == 'yellow':
	print('Player earned 10 points')

else :
	print('Player earned 15 points')

alien_colours = 'red'
if alien_colours == 'green':
	print('Player earned 5points')
elif alien_colours == 'yellow':
	print('Player earned 10 points')

else :
	print('Player earned 15 points')

5-6 #if-elif-else chain

age = 65 
if age < 2:
	print('Person is a baby')

elif age >= 2 and age < 4:
	print('Person is a toddler')

elif age >= 4 and age < 13:
	print('Person is a kid')

elif age >= 13 and age < 20:
	print('Person is a teenager')

elif age >= 20 and age <65:
	print('Person is an adult')

else:
	print('Person is an elder')

