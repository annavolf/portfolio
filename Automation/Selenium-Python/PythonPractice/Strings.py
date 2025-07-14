# Reverse a string

word="erehwoN"
rev_word= ""
for letter in word:
    rev_word=letter+rev_word
print(word)
print(rev_word)

len_word=len(word)
len_rev_word=len(rev_word)

if len_word==len_rev_word:
    print("The lenght is matched")
    print("The lenght is matched".lower())
    print("The lenght is matched".upper())

print ("Now" in word)
print ("Now" in rev_word)

each_word=word.split()
print(each_word)

print("*"*50)
# Christmas Tree

rows=10
for i in range (1,rows+1):
    print("*"*i)

