def is_lower_101(list1):
   for char in list1:
      if (char) >= "a" and (char) <= "z":
         bool_val = True
      else:
         return False
   return bool_val
def char_rot_13(char):
    val = ord(char)
    if char.isalpha() == True:
       if char.islower() == True:
          if char <= "m":
             val = ord(char) + 13
          elif char > "m":
             val = ord(char) - 13
       elif char.isupper() == True:
          if char <= "M":
             val = ord(char) + 13
          elif char > "M":
             val = ord(char)-  13
    else:
       return False
    return chr(val)

