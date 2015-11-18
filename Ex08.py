__author__ = 'kmisk'
"""http://learnpythonthehardway.org/book/ex8.html"""

formatter = "{} {} {} {}"

print(formatter .format(1,2,3,4))
print(formatter .format("one", "two", "three", "four"))
print(formatter .format(True, False, False, True))
print(formatter .format(formatter,formatter,formatter,formatter))
print(formatter .format("I had thos thing",
                        "That you could type up right",
                        "But it didn't sing.",
                        "So I said goodnight."))