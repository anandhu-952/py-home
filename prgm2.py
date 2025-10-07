vowels="a,e,i,o,u,A,E,I,O,U"
word=input("Enter the word:")
print("Vowels present in the word are:")
for i in word:
    if i in vowels:
        print(i)
