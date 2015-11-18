__author__ = 'kmisk'
"""http://learnpythonthehardway.org/book/ex6.html"""

x = "There are {} types of people" .format(10)
binary = "binary"
do_not = "don't"
y = "Those who know {} and those who {}" .format(binary, do_not)

print(x)
print(y)

print("I said: {}." .format(x))
print("I also said: '{}'." .format(y))

hilarius = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation .format(hilarius))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)