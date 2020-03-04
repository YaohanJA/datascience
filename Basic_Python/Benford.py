#  Description:


def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()

  total_num = 0
  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]
    total_num +=1
    
    # make entries in the dictionary
    if pop_num[0] in pop_freq:
      pop_freq[pop_num[0]] = pop_freq[pop_num[0]] +1
      
  #print(total_num)    

            #print()  

  # close the file
  in_file.close()

  #print(pop_freq.items())
  # write out the result
  print("Digit	Count	%")
  for i in range(1,10):  
    print(str(i) + format(pop_freq[str(i)], "11d"), end = "    ") 
    print(format(pop_freq[str(i)]/total_num *100, "<3.1f"))
  
main()




