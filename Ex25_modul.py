__author__ = 'herczkumihalybalazs'
import Ex25

sentence = "All good things come to those who wait."
words = Ex25.break_words(sentence)
print(words)

sorted_words = Ex25.sort_words(words)
print(sorted_words)
print(Ex25.print_first_word(words))
print(Ex25.print_last_word(words))
print(words)
print(Ex25.print_first_word(sorted_words))
print(Ex25.print_last_word(sorted_words))
print(sorted_words)
sorted_words = Ex25.sort_sentence(sentence)
print(sorted_words)
print(Ex25.print_first_and_last(sentence))
print(Ex25.print_first_and_last_sorted(sentence))

