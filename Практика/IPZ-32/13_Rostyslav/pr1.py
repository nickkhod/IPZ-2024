def process_string(t):

  vowels = "aeiouAEIOU"  
  consonants = ""  

  for char in t:
    if char.isalpha() and char not in vowels:
      consonants += char

  consonants = "".join(sorted(consonants))  

  has_multiple_spaces = t.count(" ") > 1 

  return (consonants, has_multiple_spaces)  


t = input()
result = process_string(t)
print(result) 