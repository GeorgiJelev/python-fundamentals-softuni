word = input()
vowels = ['a', 'o', 'u', 'e', 'i']
remove_vowels = [ch for ch in word if ch.lower() not in vowels]

print("".join(remove_vowels))
