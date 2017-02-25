#  File: DNA.py



def main():
  in_file = open("./dna.txt","r")
  #read number of pairs
  num_pairs = in_file.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int(num_pairs)

  
  for i in range(num_pairs):
    a = []
    flag = False
    str1 = in_file.readline()
    str2 = in_file.readline()
    str1 = str1.strip()
    str2 = str2.strip()
    str1 = str1.upper()
    str2 = str2.upper()

    if (len(str1) > len(str2)):
      dna1 = str1
      dna2 = str2
    else:
      dna1 = str2
      dna2 = str1
      
    wnd = len(dna2)
    while (wnd > 1  and flag == False):
      start_idx = 0
      while ((start_idx + wnd) <= len(dna2)):
        sub_strand = dna2[start_idx:start_idx + wnd ]
        if (dna1.find(sub_strand)) > -1:
          a.append(sub_strand)
          flag = True
        start_idx +=1         
      wnd = wnd - 1
    print("Pair" ,str(i+1) +": ", end ="")
    if len(a) == 0:
      print("No Common Sequence Found")
    for i in range(len(a)):
      if i == 0:
        print(a[i])
      else:
        print("        " + a[i])
    print()    

  in_file.close()
main()
  
  
