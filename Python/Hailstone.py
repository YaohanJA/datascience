#  File: Hailstone.py

#  Description:

#  Student Name:Yaohan Jiang    

#  Student UT EID: yj3948           

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created:Sep.27

#  Date Last Modified:

def main():
    lo = int(input("Enter starting number of the range: "))
    hi = int(input("Enter ending number of the range: "))
    n = 1
    max_num = 0
    max_length = 0
    for n in range (lo, hi +1):
        count_div = 0
        orig_num = n
        while n!=1:            
          if n % 2 ==0:
              n = n // 2
              count_div = count_div + 1
          else:
              n = 3*n + 1
              count_div = count_div + 1
        if (count_div >= max_length):
          max_length = count_div
          max_num = orig_num

    print("The num", max_num, "has the longest cycle length of", max_length, ".")          
            
            

main()    
