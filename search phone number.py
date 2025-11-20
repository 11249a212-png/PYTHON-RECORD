def isphonenumber(s):
    if len(s) != 12:
        return False

    if s[3] != '-' or s[7] != '-':
        return False

    if not (s[0:3].isdigit() and s[4:7].isdigit() and s[8:12].isdigit()):
        return False

    return True


# Sample test
print("Without regex:")
print(isphonenumber("415-555-4242"))  # True
print(isphonenumber("415-55A-4242"))  # False
print(isphonenumber("415-5555-242"))  # False
