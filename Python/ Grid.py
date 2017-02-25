#  File: Grid.py

#  Description:

#  Student Name: Yaohan Jiang

#  Student UT EID: yj3948	

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: Nov. 11

#  Date Last Modified:

def main(): 
  in_file = open("./grid.txt", "r")

  dim = in_file.readline()
  dim = dim.strip()
  dim = int(dim)

  grid = []

  for i in range(dim):
    line = in_file.readline()
    line = line.strip()
    row = line.split()
    for j in range(dim):
      row [j] = int(row[j])
    grid.append(row)
  #print(grid)  
  
  #horizontal
  
  a = []
  for row in grid:
    for i in range (0, dim-3):
      product = 1
      for j in range(i , i+4):
        product = product*row[j] 
      a.append(product)
 
  #vertical
  for j in range(dim):
    for i in range(dim-3):
      product = 1
      for k in range(i, i+4):
        product *= grid[k][j] 
      a.append(product)
          
 
  #print(product) 
  # major diagonal   
  for i in range(dim - 3):
    product = 1
    for j in range(i, i +4):
      product *= grid[j][j]
    a.append(product)

  #other diagonal L to R
  for i in range(dim-3):
    for j in range(dim-3):
      product =1
      for k in range(4):
        product *= grid[i+k][j+k]
      a.append(product)
  

  for i in range(dim-3):
    product = 1
    for j in range(i, i+4):
      product *= grid[j][dim-1-j]
    a.append(product)
  
  for i in range(0, dim -3):
    for j in range(3, dim):
      product =1
      for k in range(4):
        product *= grid[i+k][j-k]
      a.append(product)
  high = max(a)
  print("The greatest product is " + str(high) + ".")

  in_file.close()      
        

main()             
    

