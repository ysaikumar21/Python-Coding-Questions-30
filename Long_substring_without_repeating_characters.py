def Long_Substring(string):
    start=0
    char_index={}
    max_length=0
    for end in range(len(string)):
        char=string[end]
        if char in char_index:
            start=max(char_index[char]+1,start)
        char_index[char]=end
        max_length=max(max_length,end-start+1)
    return max_length
string=input(str("Enter a String : "))
Without_repeating_characters=Long_Substring(string)
print(Without_repeating_characters)