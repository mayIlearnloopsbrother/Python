#!/usr/bin/python3

#THIS PROGRAM USES LISTS AND ITS INDEX
#ALSO USES INSERT, APPEND REMOVE

fren = ['greg', 'leg', 'egg']
print("come to dinner " + fren[0].title() + "\ncome dinner " + fren[1].title() + "\nkom dino " + fren[2].title())
print("\no dear " + fren[0].title() + " cannot make it")
fren[0] = 'breg'
print("come to dinner " + fren[0].title() + "\ncome dinner " + fren[1].title() + "\nkom dino " + fren[2].title())
print("\nfound bigger table " + fren[0].title() + "\nbigger table " + fren[1].title() + "\nbig table " + fren[2].title())
fren.insert(0, 'mheg')
fren.insert(2, 'wheg')
fren.append('reg')
print("\ncome dino " + fren[0].title() + "\ndinner come " + fren[1].title() + "\nkom dinnor " + fren[2].title() + "\ndinnor com " + fren[3].title() +  "\ndinnor com " + fren[4].title() +  "\ndinnor com " + fren[5].title())  
print("\nO NOOO.. CAN ONLY INVITE TWO PEOPLE")
print("sowwy can't invite u to dino " + fren.pop(0).title())
print("sowwy can't invite u to dino " + fren.pop(0).title())
print("sowwy can't invite u to dino " + fren.pop(0).title())
print("sowwy can't invite u to dino " + fren.pop(0).title())
print("you are invited " + fren[0].title() + "\nyou are invited " + fren[1].title())
fren.remove('egg')
fren.remove('reg')
print(fren)
