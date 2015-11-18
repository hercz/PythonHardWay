 # -*- coding: utf-8 -*-
__author__ = 'kmisk'
"""http://learnpythonthehardway.org/book/ex5.html"""

my_name = "Zed A. Shaw"
my_age = 35
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = "Blue"
my_teeth = "White"
my_hair = "brown"

print("Let's talk about %s." % my_name)
print("He's %d inches tall" % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy")


print("He's got {} eyes and {} hair." .format(my_eyes, my_hair))


print("His teeth are usually %s depending on the coffee" % my_teeth)

#tricky line
print("if i add {}, {}, and {}, I get {}." .format(my_age, my_height, my_weight, my_height + my_weight))



