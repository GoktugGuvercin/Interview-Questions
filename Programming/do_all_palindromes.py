### Write a function that re-arranges a string into its all palindrome versions
### f("xxyy") --> ["xyyx", "yxxy"]
### f("xxyyzz") --> ["xyzzyx", "xzyyzx", "zxyyxz", "zyxxyz", "yxzzxy", "yzxxzy"]


from itertools import permutations

def do_all_palindromes(string):

  char_dict = {}
  half, middle = "", ""
  all_palindromes = []

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
  
  all_perms = ["".join(i) for i in permutations(half)]
  all_perms = list(set(all_perms))

  for perm in all_perms:
    all_palindromes.append(perm + middle + reverse(perm))
  
  return all_palindromes
