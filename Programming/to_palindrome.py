### Write a function that checks if a given string can be re-arranged into a palindrome or not
### "xxyy" --> "xyyx" (True), "xxyz" (False)


def can_be_palindrome(string):
  
  count = 0
  char_map = {}

  for c in string:
    if c in char_map:
      char_map[c] += 1
    else:
      char_map[c] = 1

  for val in char_map.values():
    if val % 2 != 0:
      count += 1
  
  if count >= 2:
    return False
  else:
  	return True