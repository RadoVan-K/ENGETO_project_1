
# První projekt do Engeto Online Python Akademie

# autor: Radovan Krejčíř
# email: krejcir.rad@gmail.com
# discord: Radovan K.#3299

# data import

import task_template

# objects

users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

TEXTS_len = len(task_template.TEXTS)

text_1 = task_template.TEXTS[0]
text_2 = task_template.TEXTS[1]
text_3 = task_template.TEXTS[2]

text_1_list = text_1.split()
text_2_list = text_2.split()
text_3_list = text_3.split()

letters = []

# graphical

line = 45 * '-'

head = 'LEN|      OCCURENCES     |NR.'

# Welcome and text selection

curr_user = input("Welcome, enter your user name: \n")

password = input('Enter your password: \n')

print(line)

if curr_user in users.keys() and password == users.get(curr_user):
    print('Hi', curr_user + '!')
    print('We have', TEXTS_len, ' texts available.')
    print(line)

else:
    print('Username and password invalid!')
    print(line)
    exit()

selection = input('Select a text for analysis: \n')

print(line)

if int(selection) == 1:
    sel_text = text_1_list
elif int(selection) == 2:
    sel_text = text_2_list
elif int(selection) == 3:
    sel_text = text_3_list
else:
    print('Only text 1-3 are available.')
    exit()

# Text analysis

sel_text_words = len(sel_text)
sel_text_title = []
sel_text_upper = []
sel_text_lower = []
sel_text_num = []
sel_text_sum = []

for w1 in sel_text:
    if w1.istitle():
        sel_text_title.append(w1)

for w1 in sel_text:
    if w1.isupper():
        sel_text_upper.append(w1)

for w1 in sel_text:
    if w1.islower():
        sel_text_lower.append(w1)

for w1 in sel_text:
    if w1.isnumeric():
        sel_text_num.append(w1)

sel_text_num_int = [int(i) for i in sel_text_num]

print('There are', sel_text_words, 'words in the selected text.')
print('There are', len(sel_text_title), 'titlecase words.')
print('There are', len(sel_text_upper), 'uppercase words.')
print('There are', len(sel_text_lower), 'lowercase words.')
print('There are', len(sel_text_num), 'numeric strings.')
print('The sum of all the numbers is', sum(sel_text_num_int), '.')

print(line)

# graphical

print(head)
print(line)

for i in sel_text:
    letters.append(len(i))

word_lengths = list(range(1,max(letters) + 1))
word_freq = []

for i in word_lengths:
    word_freq.append(letters.count(i))

for i in word_lengths:
    print('{num:3}'.format(num=i)
          + '|'
          + word_freq[i-1] * '*'
          + (21 - word_freq[i-1]) * ' '
          + '|'
          + str(word_freq[i-1]))

# End of story :)





















