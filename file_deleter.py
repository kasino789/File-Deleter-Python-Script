"""
Created on Wed Jun 28 21:14:19 2023

@author: Kasino
"""

import os 

#Enter Words here which will delete the files containing those words 
words = ['Mango', 'Apples', 'Guavas', 'Monkeys?', 'Grapes', 'Pineapples' ]

#Enter the main file folder here whose sub-folders will be opened and the corresponding words will be deleted
main = r"C:\Users\User\OneDrive\Desktop"

for root, dirs, files in os.walk(main): 
    # root means the path of the 'root folder(main variable)'
    # files is a list of all the filenames of the sub-folder
        for file_name in files:
            #file_name is individual file name from the files list
            file_path = os.path.join(root, file_name) # concats root folder path with filename to form 'file path'             
            if os.path.exists(file_path):
                for word in words: # Iterate through the words list
                    if(file_path.find(word)>=0):
                        os.remove(file_path)
            else:
                break


# Change the code accordingly for case sensitivity
