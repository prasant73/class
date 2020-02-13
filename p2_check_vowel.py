
def check_vowel(ch):
    if ch[0].lower() in ["a", "e", "i", "o", "u"]:
        return "Is a vowel"
    else:
        return "not a vowel"

# driver code
ch = input("Enter a letter : ")

print(check_vowel(ch))


# "A", "E" "I", "O", "U", 
