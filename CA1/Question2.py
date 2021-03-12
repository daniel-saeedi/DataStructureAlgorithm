def is_palindrome(s):
    return s == s[::-1]

def palindrome_exists(string) :
    characters = set()
    found = False
    for char in string :
        if not char in characters :
            characters.add(char)
            j = 0
            while j < len(string) + 1:
                new_string = string[:j] + char + string[j:]
                if is_palindrome(new_string) :
                    found = True
                    break
                j += 1
    return found

def main() : 
    commands = int(input())
    i = 0
    while i < commands :
        string = input()
        if string == "" :
            continue
        if palindrome_exists(string) == True:
            print("YES")
        else : 
            print("NO")
        i += 1 

main()