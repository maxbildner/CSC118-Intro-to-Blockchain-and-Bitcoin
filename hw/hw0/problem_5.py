# Check if a string is a palindrome: which means it reads the same forwards and 
# backwards. For example the string 'abcdcba' is palindromic.
# 
# Write a program to check if a two-dimensional array of characters reads the same 
# in any direction.
# For example: aaaa\n abba\n abba\n aaaa\n reads the same forwards or backwards 
# from left-to-right, up-to-down.
# 
# Note, the array rows are separated by '\n' .
# The program should output True only if every row and every column is palindromic.
# The two-dimensional array need not be symmetric. In other words column 1 does 
# not have to match row 1, and so on.
# 
# For simplicity, the sizes of the rows should all match, and the sizes of the 
# columns should all match. But the row size does not need to equal the column 
# size.
# 
# Create two text files. Both text files should have n rows and m columns. 
# Keep n and m reasonably sized so that a human can easily tell at a glance 
# whether the rows and columns are palindromic. The first text file should be 
# palindromic. The second should not be palindromic.

from csv import reader
import math


def main():
  # takes in string refering to file name, returns boolean whether all rows/cols are palindromes
  print(check_file('problem_5_1.txt'))    #=> True
  print(check_file('problem_5_2.txt'))    #=> False
  

# takes in string, returns boolean
def check_file(file_name):
  opened_file = open(file_name, 'r')

  # array of strings
  lines = opened_file.read().splitlines()
  # lines == ['aaaa', 'abba', 'abba', 'aaaa']
  # lines == ['aaca', 'abba', 'abda', 'aaaz']
  
  # lines == 
  # [
  #   'aaaa', 
  #   'abba', 
  #   'abba', 
  #   'aaaa',
  # ]
  
  row_idx = 0

  # check if all rows are palindromes
  for row in lines:

    # exit early if row is NOT a palindrome
    if (not is_palindrome(row)):
      return False
    
    # grab column
    col = get_column(lines, row_idx)

    # exit early if column is NOT a palindrome
    if (not is_palindrome(col)):
      return False

    row_idx += 1

  return True
    



# Helper Function, takes in array of strings and column index, returns string
def get_column(array, idx):
  string = ''

  for row in array:
    string += row[idx]
  
  return string
# arr1 = ['aaaa', 'abba', 'abba', 'aaaa']
# print(get_column(arr1, 0))    #=> 'aaaa'



# Helper Function, takes in String, returns Boolean
# "a"     =>  true
# "aa"    =>  true
# "abba"  =>  true
# "abcba" =>  true
# "abca"  =>  false
# "abcaa" =>  false
# "ba"    =>  false
def is_palindrome(str):
  
  str_len = len(str)
  mid_idx = math.floor(str_len/2)
  l = 0
  r = str_len - 1
    
  while l < mid_idx:
    left_char = str[l]
    right_char = str[r]

    if left_char != right_char:
      return False

    l += 1
    r -= 1
  
  return True

# print(is_palindrome("a"))      #=> True
# print(is_palindrome("aa"))     #=> True
# print(is_palindrome("abba"))   #=> True
# print(is_palindrome("abcba"))  #=> True
# print(is_palindrome("abca"))   #=> False
# print(is_palindrome("abcaa"))  #=> False
  

if __name__ == '__main__':
  main()