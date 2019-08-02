encodage()
two_letter_words()
three_letter_words()
four_letter_words()
five_letter_words()
six_letter_words()
seven_letter_words()
eight_letter_words()
print("5 lettres : ")
for e in file:
	if e.mot in text:
		print(e.mot)
print("6 lettres: ")
for e in sle:
	if e.mot in text:
		print(e.mot)
print("7 lettres:")
for e in sele:
	if e.mot in text:
		print(e.mot)

