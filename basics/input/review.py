word = str(input("Input a word or phrase of choice."))
number = int(input("Input a integer, a decimal or string will not work."))
print("\nHere is your word/phrase printed {} times.".format(number))
word = "\t" + word + "\n"
print(word*number)