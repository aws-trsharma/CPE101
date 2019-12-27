def my_strspn(str1, str2):
    index = 0
    for i in range(len(str1)):
        if str2.find(str1[i]) != -1:
            index +=1
        else:
            break
    return index
def main():
    string1 = input("Enter string1:    ")
    string2 = input("Enter string2:    ")
    val = my_strspn(string1, string2)
    print("Result: ", val)
if __name__ == '__main__':
   main()
