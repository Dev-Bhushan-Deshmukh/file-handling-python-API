f=open('dummy-para.txt','r')
# print(f.read())
countline=0
countword=0
charcount=0

for i in f:
    countline=countline+1
    linelen=len(i.split())
    wordlist=i.split()
    countword=countword+linelen
    for word in wordlist:
        wordlen=len(word)
        charcount=charcount+wordlen

    print()

print("countline:-->",countline)
print("countword:-->",countword)
print("countchar:-->",charcount)