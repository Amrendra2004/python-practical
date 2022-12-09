import os

def fname(file):
    num_words = 0
    num_lines = 0

    with open(file, 'r') as f:
        for i in f:
            i = i.strip(os.linesep)
            wordslist = i.split()
            num_lines = num_lines+1
             
            num_words = num_words + len(wordslist)
     
    print("Number of words in text file: ",
          num_words)
     
    print("Number of lines in text file: ",
          num_lines)
fname('text.txt')
