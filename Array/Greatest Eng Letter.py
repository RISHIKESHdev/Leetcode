def greatestLetter(s):
		letters = set(s)
		greatest = ''

		for ltr in letters:
			if ltr.isupper() and ltr.lower() in letters:
				greatest = max(ltr, greatest)

		return greatest
print(greatestLetter(input()))