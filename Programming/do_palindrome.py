### Write a function that re-arranges a string into its palindrome version
### f("xxyyzz") --> "xyzzyx"

def do_palindrome(string):

  char_dict = {}
  half, middle = "", ""

  for c in string:
    if c in char_dict:
      char_dict[c] += 1
    else:
      char_dict[c] = 1

  for key, value in char_dict.items():
    if value % 2 == 0:
      half += key * int(value / 2)
    else:
      middle = key
  
  return half + middle + reverse(half)