# File: Deal.py

# Description:

# Student Name: Yaohan Jiang

# Student UT EID: yj3948

# Course Name: CS 303E

# Unique Number: 51200

# Date Created: Oct.19

# Date Last Modified:
import random

n = eval(input("Enter number of times you want to play: "))
print()
num_time_win_switch = 0
# door that conceals the prize
print("  Prize      Guess       View    New Guess")
for x in range(n):   
  prize = random.randint(1,3)
  guess = random.randint(1,3)
  view = 0
  a = [1, 2, 3]
  a.remove(prize)
  if guess in a:
    a.remove(guess)
  view = a[0]
  new_guess = 6-guess-view
  if prize == new_guess:
    num_time_win_switch +=1
  print (format(prize,"5d"), end = "")
  print(format(guess,"11d"), end = "")
  print( format(view,"11d"), end = "")
  print(format(new_guess,"11d") )     
        
        
p_win_switch = num_time_win_switch / n
P = 1-p_win_switch 


print()
print("Probability of winning if you switch =", format(p_win_switch, "<3.2f"))
print("Probability of winning if you do not switch =", format(P, "<3.2f"))        
            
            



