#!/usr/bin/python3 

#THIS PROGRAM SHOWS USING THE VARIABLE TO USE FOR LOWER, UPPER AND TITLE
#ALSO USES LSTRIP, RSTRIP AND STRIP

person = "Eric"
print("hello ," + person.title() + " would you like to learn some Python today?")
person = "eRic"
print("lowercase: " + person.lower() + "\nuppercase: " + person.upper() + "\ntitle: " + person.title())
famous_person = "Albert Einstein"
msg = ' once said, "A person who never made a mistake never tried anything new."'
print(famous_person + msg)
funny_name = "  shakeSpEare  "
print("\n" + funny_name.lstrip().title() + "\n" + funny_name.rstrip().title() + "\n" + funny_name.strip().title())
