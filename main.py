#HW1 Tal Farhan 205611080
import collections
import re
# from matplotlib.colors import is_color_like
import tkinter as tk
from builtins import list

#Note No.1:  A code that allows the user to select a text file he wants from the program folder
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo
#
# readFile=''
# # create the root window
# root = tk.Tk()
# root.title('Tkinter Open File Dialog')
# root.resizable(False, False)
# root.geometry('300x300')
# filetypes = (
#     ('text files', '*.txt'),
# )
# filename = fd.askopenfilename(
#     title='Open a file',
#     initialdir='/',
#     filetypes=filetypes)
# showinfo(
#     title='Selected File',
#     message=filename
# )
# if filename:
#     with open(filename) as file:
#         readFile = file.read()
# # open button
# open_button = ttk.Button(
#     root,
#     text='Open a File',
# )
# open_button.pack(expand=True)
# # run the application
# root.mainloop()

#s1:Finding the number of rows in the file=V
file = open("t1.txt","r")
readFile = file.read()
counterRows = 0
# Reading from file
#Split the rows into a list
listOfRow = readFile.split("\n")
#A loop that counts the items in the list
for i in listOfRow:
    counterRows += 1
#file.close()
print("s1. The number of lines in the file is\n",counterRows)

#s2:Finding the number of words in the file=V
listOfWords= readFile.split()
#Find the length of the list
counterWords=len(listOfWords)
print("s2. The number of words in the file is\n",counterWords)

#ex3:Find the amount of unique words in the file=V
#Convert uppercase letters to lowercase letters
readFile = readFile.lower()
#A list of all the words that appear in the file
words = readFile.split()
#Removes the characters: '.,!;()[]' To bring the word in its basic form
words = [word.strip('.,!;()[]') for word in words]
#Removes belongingness to bring the word to its basic form
words = [word.replace("'s", '') for word in words]
#Go over the list and create a new list without repetitions
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
#sort:Check if words do not repeat themselves
#unique.sort()
#print(unique)
print("s3. The number of unique words in the file:\n",len(unique))

#s3:If meaning is unique in terms of the number of times the word appears then this code meets this requirement
readFile = readFile.lower()
words = re.findall(r'\w+', readFile)
words=[word.strip('.,!;()[]') for word in words]
words=[word.replace("'s", '') for word in words]
most_common2 = collections.Counter(words).most_common()
# print(most_common2)
sumOfUnique=0
for i in most_common2:
    if i[1]==1:
        sumOfUnique+=1
print("s3: The number of words that appear only once in a file:\n",sumOfUnique)

#s4:Finding the average and maximum sentence length

listOfRow = readFile.split(".")
# print(listOfRow)
numList = []
counter=0
counterAll=0
for i in listOfRow:
    numList.append(len(i))
    counter+=1
for i in numList:
    counterAll+=i
#print(numList)
numList.sort()
print("s4a. The average sentence length is:\n",counterAll/counter)
print("s4b. The maximum sentence length is:\n",numList[len(numList)-1])


#s5:Finding the most popular word in the text  =V
readFile = readFile.lower()
words = re.findall(r'\w+',readFile)
most_common2 = collections.Counter(words).most_common()
most_common = collections.Counter(words).most_common(1)
print("s5a. The most popular word in the text:\n",most_common[0])
syntactic=['the','am','is','are',"don't",'that','of','was','were','it','a','an']
result = []
for i in most_common2:
    if(i[0] not in syntactic):
        result.append(i)
print("s5b. The most popular word in the text which has no syntactic meaning:\n",result[0][0],"(",result[0][1],"times)")

#s6:Finding the longest word sequence in a text that does not contain the letter k
listOfWords=readFile.split()
listSul=[]
max=0
#Check after one such sequence is found
listSulOp=[]
maxOp=0
flag=1       #Indicate if this is the first time you are starting to tell a sequence
for i in listOfWords:
    if 'k' not in i:
        if flag!=1: #Sequence was first detected
            listSulOp.append(i)
            maxOp=maxOp+1
        else:       #Next detected sequence (to compare to first detected sequence)
            listSul.append(i)
            max=max+1
    else:
        flag=0      #If k is detected then we will compare which is larger of the sequences
        if maxOp>max:
            max=maxOp
            maxOp=0
            listSul=[]
            listSul=listSulOp.copy()
            listSulOp=[]
#If not after the sequence K
if maxOp>max:
    max=maxOp
    listSul=[]
    listSul=listSulOp.copy()

print("s6. The longest word sequence length in text that does not contain the letter k:\n",max)
print("and the sequence of words:\n",' '.join(map(str,listSul)))

#s8:The names of the colors that appear in the text and their quantity=V
readFile = readFile.lower()
words = re.findall(r'\w+', readFile)
listSumOfColor=[]
listColor=['aqua','white','yellow','red','orange','purple','olive','navy','mint','gray','blue','skyblue','pink','green','orange','purple','black']
for word in words:
    if word in listColor:
        listSumOfColor.append(word)
# print("color:\n",listColor)
most_common = collections.Counter(listSumOfColor).most_common()
print("s8. The names of the colors that appear in the text and their quantity:\n",most_common)


#s7:Finding the largest number indicated in the text
def numbers_to_strings(argument):
    switcher = {
        "zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,
        "eleven":11,"twelve":12,"thirteen":12,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,

    }
    return switcher.get(argument,None)
res = [int(i) for i in readFile.split() if i.isdigit()]
for i in readFile.split():
    if numbers_to_strings(i)!=None:
        num=numbers_to_strings(i)
        res.append(num)
# print("res\n",sorted(res))
res=sorted(res)
if(len(res)>0):
    print("s7. the largest number indicated in the text\n",res[len(res)-1])
else:
    print("s7. There is no number")

#s9: Finding the names of the characters that appear in the text and   the most is common =V
# My assumption is that people's names start with a capital letter
# (of course there can be other words that are not names that start with a capital letter)
readFile = readFile.lower()
words = re.findall(r'\w+', open('test.txt').read())
listUpper=[]
for word in words:
    if word[0].isupper():
        listUpper.append(word)
print("s9a. The names of the characters that appear in the text:\n",listUpper)
most_common = collections.Counter(listUpper).most_common(1)
print("s9b. The most common character name:\n",most_common[0][0],"(",most_common[0][1],"times)")
