#!/usr/bin/python3


car = 'Subaru'				#this line value starts with Capital letter

print("car == subaru? I predict true." )  
print(car.lower() == 'subaru')			#the use of lower() is used to ignore case sensitivity
print("car == subaru? Due to case-sensitivity I predict false.")
print(car == 'subaru')					#this will be false because of case sensitivity
print("car != subaru? I predict false.")
print(car.lower() != 'subaru')
print("car != audi? I predict true.")
print(car != 'audi')
print("car == audi? I predict false.")
print(car == 'audi')

print("\n")
 
car2 = 'honda_civic'

print("car2 == 'suzuki'? I predict false.")
print(car2 == 'suzuki')
print("car2 == 'honda_civic'? I predict true.")
print(car2 == 'honda_civic')
print ("\n")

cars = ['Subaru','audi']
print("True if Subaru in cars list "  + "\n" + str('Subaru' in cars))

print("\n")

a = 4
b = 2
if a < 3 and b < 3:
	print("a and b are lower than 3")
else:
	print("a and b are greater than 3")



