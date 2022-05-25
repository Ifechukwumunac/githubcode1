# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    # open the file
    new_file = open(filename, "r")
    # read whats in the file, line by line so that when i split it into words it actually does
    # using read reads the file as a str and so when its split its split into letters.
    read_file = new_file.readlines()
    # close the file
    new_file.close()
    return read_file
    # testing 
print(read_file_content('C:\\Users\BUYPC COMPUTERS\AppData\Local\Temp\Temp1_Reading-Text-Files.zip\Reading-Text-Files\story.txt'))

def count_words(text):
  import string
  text = read_file_content(text)
    # [assignment] Add your code here
    # open empty dictionary  
  counts = dict()
  
  for line in text:
      # remove the leading spaces and new line characters
    line = line.strip()

      # convert case to
      #  lower case to avoid case mismatch
    line = line.lower() 

      # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("","", string.punctuation))

    # split it into words
    words = line.split(" ")

    #iterate over each word in words
    for word in words:
        # check if word is in dictionary 
        if word in counts:
         #increment it by 1
         counts[word] += 1
        else:
          # add word to dictionary with count 1, as the number attached to word
          counts[word] = 1
  # return contents of dictionary      
  return counts
# testing it out
print (count_words('C:\\Users\BUYPC COMPUTERS\AppData\Local\Temp\Temp1_Reading-Text-Files.zip\Reading-Text-Files\story.txt'))
