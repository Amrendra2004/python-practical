import os
def fname(file):

    with open(file, 'r') as f:
        for i in f:
            if len(i)!=0:
                print(i[::-1])
            
fname('text.txt')

