def get_times_table(number):
   result = ""

   print("Times11 Table of : ")  
   for i in range(1,number+1):    
      for j in range(1,number+1):
         
         result +=str(i*j)
         if j !=number:
            result += "\t"

      if i != number:
         result += "\n"

   return result
if __name__=="__main__":
   number = int(input("enter number:"))
   print(get_times_table(number))