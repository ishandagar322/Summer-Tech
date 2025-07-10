
qwe =[["__","__","__"],["__", "__","__"],["__", "__","__"]]
for i in range(3):
   print(qwe[i])
turns = 0
winner = False
while winner == False: 
   x = int(input("Choose a column:"))
   y = int(input("Choose a row:"))
   if qwe[x][y] == "o" or qwe[x][y] == "x":
      print("You can't go there.")
      x = int(input("Choose a column: "))
      y = int(input("Choose a row:"))
   qwe[x][y] = "x" 
   turns += 1
   print(turns)
   for i in range(3):
      print(qwe[i])
   if qwe[0][0] == "x" and qwe[0][1] == "x" and qwe[0][2] =="x":
      winner = True
      break
   if qwe[1][0] == "x" and qwe[1][1] == "x" and qwe[1][2] =="x":
      winner = True
      break
   if qwe[2][0] == "x" and qwe[2][1] == "x" and qwe[2][2] =="x":
      winner = True
      break
   if qwe[0][1] == "x" and qwe[1][1] == "x" and qwe[2][1] =="x":
      winner = True
      break
   if qwe[0][2] == "x" and qwe[1][2] == "x" and qwe[2][2] =="x":
      winner = True
      break
   if qwe[0][0] == "x" and qwe[1][0] == "x" and qwe[2][0] =="x":
      winner = True
      break
   if qwe[0][0] == "x" and qwe[1][1] == "x" and qwe[2][2] =="x":
      winner = True
      break
   if qwe[0][2] == "x" and qwe[1][1] == "x" and qwe[2][0] =="x":
      winner = True
      break
   elif turns == 9 and winner == False:
      break
   w = int(input("Choose a column: "))
   q = int(input("Choose a row: "))
   if qwe[w][q] == "x" or qwe[w][q] == "o":
      print("You can't go there.")
      w = int(input("Choose a column: "))
      q = int(input("Choose a row:"))
   qwe[w][q] = "o"
   turns += 1 
   print(turns)
   for i in range(3):
      print(qwe[i])
   if qwe[0][0] == "o" and qwe[0][1] == "o" and qwe[0][2] =="o":
      winner = True
   elif qwe[1][0] == "o" and qwe[1][1] == "o" and qwe[1][2] =="o":
      winner = True
   elif qwe[2][0] == "o" and qwe[2][1] == "o" and qwe[2][2] =="o":
      winner = True
   elif qwe[0][1] == "o" and qwe[1][1] == "o" and qwe[2][1] =="o":
      winner = True
   elif qwe[0][2] == "o" and qwe[1][2] == "o" and qwe[2][2] =="o":
      winner = True
   elif qwe[0][0] == "o" and qwe[1][0] == "o" and qwe[2][0] =="o":
      winner = True
   elif qwe[0][0] == "o" and qwe[1][1] == "o" and qwe[2][2] =="o":
      winner = True
   elif qwe[0][2] == "o" and qwe[1][1] == "o" and qwe[2][0] =="o":
      winner = True

