### Write a function that generates palindrome string
### The function will take two arguments f(n, m)
### n: the length of palindrome, m: number of different characters

import random

def reverse(string):
  return string[::-1]


def extend(lst, size):

  if len(lst) >= size:
    return lst[:size+1]
  else:
    return extend(lst + lst, size)


def generate_palindrome(length, num_char):

  assert 0 <= num_char <= 94, (
      "Invalid number of characters")

  assert length >= 0, (
      "Invalid length for a string")
  
  if length == 0 or num_char == 0:
    return ""
  
  ascii_numbers = random.sample(range(33, 127), num_char)
  rand_chars = [chr(i) for i in ascii_numbers]
  rand_chars = extend(rand_chars, length // 2)

  first_half = random.sample(rand_chars, length // 2)
  second_half = reverse(first_half)
  middle = "" if length // 2 == 0 else random.sample(rand_chars, 1)

  return "".join(first_half + middle + second_half)
