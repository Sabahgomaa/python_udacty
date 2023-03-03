# format() Practice
# Use the coding space below to practice using the format() string method.
# # There are no right or wrong answers here, just practice!
# new_str = "The cow jumped over the moon."
# print(new_str.split())
# print(new_str.split(' ', 3))
# print(new_str.split('.'))
# print(new_str.split(None, 3))

# Quiz: String Methods Coding Practice
# Below, we have a string variable that contains the first verse of the poem, If by Rudyard Kipling. Remember, \n is a special sequence of characters that causes a line break (a new line).
#
# verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
# Use the code editor below to answer the following questions about verse and use Test Run to check your output in the quiz at the bottom of this page.
#
# What is the length of the string variable verse?
# What is the index of the first occurrence of the word 'and' in verse?
# What is the index of the last occurrence of the word 'you' in verse?
# What is the count of occurrences of the word 'you' in the verse?
# You will need to refer to Python's string methods documentation.

# Version 1
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

print("Verse has a length of {} characters.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))

# Version 2
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."

length = len(verse)
print(length)
first_idx = verse.find('and')
print(first_idx)
last_idx = verse.rfind('you')
print(last_idx)
count = verse.count('you')
print(count)
print(message.format(length, first_idx, last_idx, count))