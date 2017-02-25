#  File: CreditCard.py



 # This function checks if a credit card number is valid


def is_valid (cc_num):

  cclist = [int(i) for i in str(cc_num)]
  cclist = cclist[::-1]
  
  if len(cclist) != 15 and len(cclist)!=16:
    print ("Not a 15 or 16-digit number ")
    return False

  a= []
  for i in range(len(cclist)):
    if i % 2 == 1:
     s =  2*cclist[i]
     s = s % 10 + s //10
     a.append(s)
    else:
      a.append(cclist[i])

  if ( sum(a) %10 == 0):
    return True
  else:
    print ("Invalid credit card number")
    return False


  # This function returns the type of credit card
def cc_type (cc_num):
  a = ["American Express","Discover","MasterCard","Visa"]
  b = [int(i) for i in str(cc_num)]  
  if b[0:2] == [3,4] or b[0:2] == [3,7]:
    return a[0]
  if b[0:4] == [6,0,1,1] or b[0:3] == [6,4,4] or b[0:2] == [6,5]:
    return a[1]
  if b[0] == 5 and b[1] <=5 :
    return a[2]
  if b[0] == 4:
    return a[3]
  else:
    return ("")



def  main (): 
  card = int(input("Enter a 15 or 16-digit credit card number:"))
  if is_valid(card):
    print("Valid "+str(cc_type(card))+" credit card number")
    



main()
