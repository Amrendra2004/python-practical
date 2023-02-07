import os

def fname(file):
    num_words = 0
    num_lines = 0
    num_words = 0
    num_charc = 0
    with open(file, 'r') as f:
        for i in f:
            i = i.strip(os.linesep)
            wordslist = i.split()
            num_lines = num_lines+1
            
            num_words = num_words + len(wordslist)
            for l in i:
              for j in l:
                     
                    if(j !=" " and j !="\n"):
                        
                        num_charc += 1 
    print("Number of words in text file: ",
          num_words)
     
    print("Number of lines in text file: ",
          num_lines)
    
    print('Number of characters in text file: ',
          num_charc)
    
fname('text.txt')
