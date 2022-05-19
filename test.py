import string; print((plaintext := input("text? ")).translate(str.maketrans(string.ascii_lowercase, string.ascii_lowercase[(shift := int(input("shift? "))):] + string.ascii_lowercase[:shift])))
