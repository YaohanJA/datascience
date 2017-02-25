#  File: Spiral.py

#  Description:

#  Student Name:Yaohan Jiang	

#  Student UT EID: yj3948

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: Nov.18

#  Date Last Modified:
def spiral(n, target):
    myarray = [[0]* n for i in range(n)]
    x,y = n-1,n-1  # initial location

    direction = 0
    maxval = n*n
    xlimit = [0, n-1]
    ylimit = [0, n-1]

    for i in range(maxval):
        if direction == 0:
            myarray[y][x] = maxval - i
            x -= 1
        elif direction == 1:
            myarray[y][x] = maxval - i
            y -= 1
        elif direction == 2:
            myarray[y][x] = maxval - i
            x += 1
        elif direction == 3:
            myarray[y][x] = maxval - i
            y += 1
            
        if x < xlimit[0] and direction == 0:
            direction = 1
            x = xlimit[0]
            ylimit[1] = ylimit[1] - 1
            y = ylimit[1]
        elif y < ylimit[0] and direction == 1:
            direction = 2
            y = ylimit[0]
            xlimit[0] = xlimit[0] + 1
            x = xlimit[0]
        elif x > xlimit[1] and direction == 2:
            direction = 3
            x = xlimit[1]
            ylimit[0] = ylimit[0] + 1
            y = ylimit[0]
        elif y > ylimit[1] and direction == 3:
            direction = 0
            y = ylimit[1]
            xlimit[1] = xlimit[1] - 1
            x = xlimit[1]
    #print(myarray)

    for i in range(len(myarray)):
        for j in range(len(myarray[i])):
            if myarray[i][j] == target:
               if 0<i<n-1 and 0<j<n-1:
                   print (myarray[i+1][j-1],myarray[i+1][j],myarray[i+1][j+1], end = "\n")
                   print (myarray[i][j-1],myarray[i][j],myarray[i][j+1], end = "\n")
                   print (myarray[i-1][j-1],myarray[i-1][j],myarray[i-1][j+1], end="\n")                  
               else:
                  print("Number on Outer Edge.")  
            #print (myarray[n-i-1][j], end="\t")
        
                  
def main():
    n = eval(input("Enter dimension:"))
    if n % 2 ==0:
      n = n+1
    target = eval(input("Enter number in spiral:"))
    if target > n*n:
      print("Number not in Range.")
    return spiral(n, target)
main()    
    
      
        
    







    
    
      
