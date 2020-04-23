s= input()
def swap_case(s):
    for x in range(0, len(s)):
        if s[x].isupper == True:
            s[x].lower()
        else:
            s[x].upper()
    return s


print (swap_case(s))