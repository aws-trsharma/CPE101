def str_rot_13(str):
   list1 = []
   for char in str:
      val = ord(char)
      if char.isalpha()==True:
         if char.islower()==True:
            if char <= "m":
               val = ord(char) + 13
            elif char > "m":
               val = ord(char) - 13
         elif char.isupper() == True:
            if char <= "M":
               val = ord(char) + 13
            elif char > "M":
               val = ord(char) - 13
      list1.append(chr(val))
   list2 = ''.join(list1)
   return list2
def str_translate_101(string, old_char, new_char):
   string1 = [c for c in string]
   string1 = [new_char if c == old_char else c for c in string]
   string2 = ''.join(string1)
   return string2


