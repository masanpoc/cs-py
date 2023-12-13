def has_a_vowel(a_str):
    print("Starting...")
    for letter in a_str:
        print("Checking", letter)
        if letter in "aeiou":
            print(letter, "is a vowel, returning True")
            return True
        else:
            print(letter, "is not a vowel, returning False")
            return False
    print("Done!")


has_a_vowel("")
# It only prints "Done" if a_str is empty.
