def box(word):
  print("-", "-" * len(word), "-")
  print("|", word, "|")
  print("-", "-" * len(word), "-")

def mirror(word):
  mirrored = word[::-1]
  print(word, " ", mirrored)

def repeat(word):
  times = int(input("How many times to repeat?"))
  for x in range(times):
    print(word)

text = input("Please enter a word.")
print("Please choose from the options below.")
print("1) Display in a Box – display the word in an ascii art box")
print("2) Display Lower-case – display the word in lower-case e.g. hello")
print("3) Display Upper-case – display the word in upper-case e.g. HELLO")
print("4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH")
print("5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.")
choice = int(input("Choice: "))

if (choice == 1):
  box(text)
elif (choice == 2):
  print(text.lower())
elif (choice == 3):
  print(text.upper())
elif (choice == 4):
  mirror(text)
elif (choice == 5):
  repeat(text)
else:
  print("Invalid choice.")