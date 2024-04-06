label = "label"
ans = ""

for char in label:
    # conver char to unicode integer
    char = ord(char)
    
    # xor with 13
    char = char ^ 13
    
    # convert to char
    char = chr(char)
    
    ans += char

print(ans)