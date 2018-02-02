user_input = raw_input("Would you like to make a ceipher, or deceipher?: (c/d)")
user_key = abs(int(raw_input("What is your cipher key?: ")))
user_text = raw_input("What is your text?: ")
while user_key > 26:
    user_key -= 26
print user_key
if user_input == "c":
    user_key = 26 - user_key
letters = [
   "a",
   "b",
   "c",
   "d",
   "e",
   "f",
   "g",
   "h",
   "i",
   "j",
   "k",
   "l",
   "m",
   "n",
   "o",
   "p",
   "q",
   "r",
   "s",
   "t",
   "u",
   "v",
   "w",
   "x",
   "y",
   "z"
]
lower_input = list(user_text.lower())
decipered = []
for i in range(0, len(lower_input)):
    if lower_input[i] == " ":
        decipered.append(" ")
    else:
        letter_index = letters.index(lower_input[i]) - user_key
        decipered.append(letters[letter_index])

print "".join(decipered)
