#  File: ISBN.py

#  Description:

#  Student Name: Yaohan Jiang   

#  Student UT EID: yj3948

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created:

#  Date Last Modified:

def partial_sums(iterable):
  total = 0
  for i in iterable:
    total += i
    yield total

def is_valid(isbn):    
  if len(isbn) !=10:
    return False

  for i in range(0, 9):
    if not isbn[i].isdigit():
      return False      
    digit_in = []
    
  for i in range(0,9):      
    digit_in.append(int(isbn[i]))
  if isbn[9] == "X":
    digit_in.append(10)
  else:
    digit_in.append(int(isbn[9]))
    
  s1 = list(partial_sums(digit_in))
  s2 = list(partial_sums(s1))
        
  if s2[9] % 11 !=0:
    return False
    
  return True
        
      
    
def main():
  in_file = open("./isbn.txt","r")
  out_file = open("./isbnOut.txt","a")
 
  for isbn in in_file:
    isbn = isbn.strip()
    isbn_ori = isbn
    isbn = isbn.replace("-","")
    isbn = isbn.upper()
    if is_valid(isbn):
      out_file.write(isbn_ori + "\t" + "valid" + "\n")
    else:
      out_file.write(isbn_ori + "\t" + "invalid" + "\n")
      
  in_file.close()
  out_file.close()
main()    
    

   
