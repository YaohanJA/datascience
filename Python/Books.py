#  File: Books.py

#  Description: 

#  Student Name:Yaohan Jiang

#  Student UT EID:yj3948

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: Nov.28

#  Date Last Modified:



def parseString(st):
  parsed = []
  st = st.replace("!", " ").replace(".", " ").replace("?", " ").replace(";"," ").replace(":", " ").replace('"'," ")
  st = st.replace("-", " ").replace("'s",' ').replace("' ", " ")

  newst = ""
  for i in range(len(st)):
    if st[i].isalpha() or st[i].isspace() or st[i]=="'":
      newst = newst + st[i]
  for word in newst.split():
      parsed.append(word)
  return parsed


# Returns a dictionary of words and their frequencies
def getWordFreq (file):
  # Create word dictionary from the comprehensive word list
  word_dict = {}
  infile=open("\nwords.txt","r",encoding = 'utf-8')
  for line in infile:
    parsed = parseString(line.rstrip('\n'))
    for word in parsed:
      if word in word_dict:
        word_dict[word]+=1
      else:
        word_dict[word]=1

  infile.close()
 
  file_word_dict={}
  infile=open(file,"r", encoding = 'utf-8') 
  for line in infile:
    parsed = parseString(line.rstrip('\n'))
    for word in parsed:
      if word in file_word_dict:
        file_word_dict[word]+=1
      else:
        file_word_dict[word]=1
  
  new_file_dict={}
  for word in file_word_dict:
    if word[0].islower():
      new_file_dict[word]=file_word_dict[word]
    
  for word in file_word_dict:
    if word[0].isupper():
      if word.lower() in file_word_dict:
        new_file_dict[word.lower()]+=file_word_dict[word]
      else:
        if word.lower() in word_dict:
          new_file_dict[word.lower()]=file_word_dict[word]
          
      
  return (new_file_dict)

  #close file and return word dictionary

def wordComparison(author1, freq1, author2, freq2):
  #initialize counting variables and create set differences
  totalCount1 = 0
  wordCount1 = 0
  for word in freq1:
    totalCount1 += freq1[word]
    wordCount1 += 1
  totalCount2 = 0
  wordCount2 = 0
  for word in freq2:
    totalCount2 += freq2[word]
    wordCount2 += 1
  set1 = set(freq1)
  set2 = set(freq2)
  diff1 = set1 - set2
  diff2 = set2 - set1
  count1 = 0
  for x in diff1:
    count1 += freq1[x]
  count2 = 0
  for x in diff2:
    count2 += freq2[x]
  
  #Print results
  print()
  print(author1)
  print('Total distinct words =', wordCount1)
  print('Total words (including duplicates) =', totalCount1)
  print('Ratio (% of total distinct words to total words) =', \
        wordCount1/totalCount1*100, end = '\n\n')
  print(author2)
  print('Total distinct words =', wordCount2)
  print('Total words (including duplicates) =', totalCount2)
  print('Ratio (% of total distinct words to total words =', \
        wordCount2/totalCount2*100, end = '\n\n')
  print('%s used %d words that %s did not use.' %(author1, len(diff1), author2))
  print('Relative frequency of words used by %s not in common with %s =' \
        %(author1, author2), count1/totalCount1*100, end = '\n\n')
  print('%s used %d words that %s did not use.' %(author2, len(diff2), author1))
  print('Relative frequency of words used by %s not in common with %s =' \
        %(author2, author1), count2/totalCount2*100, end = '\n\n')
  

def main():
  # Enter names of the two books in electronic form
  book1 = input("Enter name of first book: ")
  book2 = input("Enter name of second book: ")

  print()
  
  # Enter names of the two authors
  author1 = input("Enter last name of first author: ")
  author2 = input("Enter last name of second author: ")
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq(book1)
  wordFreq2 = getWordFreq(book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()

