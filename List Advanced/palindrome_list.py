def palindrome_filter(word):
    if word == word[::-1]:
        return word


words = input().split(" ")
palindrome = input()
palindrome_lst = [word for word in words if palindrome_filter(word)]

print(palindrome_lst)
print(f"Found palindrome {palindrome_lst.count(palindrome)} times")