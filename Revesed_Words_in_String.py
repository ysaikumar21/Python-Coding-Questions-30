def Reversed_Words(string):
    words=string.split()
    reversed_words=reversed(words)
    return ' '.join(reversed_words)

string=input(str("Enter a string contains atleast few Words : "))
reversed_string=Reversed_Words(string)
print(reversed_string)