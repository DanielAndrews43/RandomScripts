def caesar_shift(s, n):
  import string
  n = n%26
  if (n == 26 or n == -26 or n == 0):
      return s
  ans = []
  letters = list(s)
  for i,char in enumerate(letters):
      if (char.isalpha()):
          num = ord(char) + n
          if (char.isupper()):
              if num > ord('Z'):
                  num -= 26
              elif num < ord('A'):
                  num += 26
          elif (char.islower()):
              if num > ord('z'):
                  num -= 26
              elif num < ord('a'):
                  num += 26
          ans += chr(num)
      else:
          ans += char
  return ''.join(ans)