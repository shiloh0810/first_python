from random import randint
number = randint(1000, 9999)
# print number
guess = str(raw_input("What's your guess?"))
number_list = str(number)

b = 0
for i in guess:
    if i == number_list[0]:
        b += 1
    if i == number_list[1]:
        b += 1
    if i == number_list[2]:
        b += 1
    if i == number_list[3]:
        b += 1

a = 0
i = 0
while i < len(guess):
    if guess[i] == number_list[i]:
        a += 1
    i += 1

print str(a) + 'A' + str(b) + 'B'

if b == 4:
    print "Congrats!"