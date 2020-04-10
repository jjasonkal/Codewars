# Courier  

🔨Υour friend Python just called you to hang out afterwards but you haven't finished you job yet. You are working at a courier company and you know which deliveries have left so you just need to calculate the time it will take you to complete them.🔨
```
  courier(arr,n)
```
⚫ The arguments of the function is an array with all the locations of the delivery points and n the maximum number of packages you can carry at once.

⚫ It takes 2 minutes to load the packages at the store.

⚫ It takes 2 minutes to hand a package to the consignee.

⚫ Even if there are 2 or more consignees at the same location it will take 2 minutes each to complete the delivery. (For example 9n and 9n)

⚫ If the array is empty return 0.

✅ Your task is to calculate and return the least possible time it will take you (in minutes) to deliver all the packages and return back to the store.
```
        | n |
        |   |
        |   |
 -------+   +-------     X = (0,0) is the location of the courier store
  w       X       e      
 -------+   +-------     There are four directions (West,East,North,South)
        |   |
        |   |
        | s |
```
⚫ The first character is the direction and the second the minutes that it takes to get there if you follow that direction.
```
arr = ["w3", "e5", "n7", "s2", "s1", "w5", "e7", "n13", "w6", "e2", "e4", "e1", "n9"]
```
💡 Example:
```
arr = ["w3", "e5", "n7", "s2", "s1", "w5", "e7", "n13", "w6", "e2", "e4", "e1", "n9"] 
n=3

Route:
📦📦📦You load 3 packages which is 2 minutes
Firstly you go at w6 which is 6 minutes away + 2 minutes the delivery
Secondly you go at w5 which is 1 minutes away from w6 + 2 minutes delivery time
Thirdly you go at w3 which is 2 minutes away from w5 + 2 minutes delivery time
Go back to the store which is 3 minutes away from w3
Time1= 20 minutes

📦📦📦You load 3 packages which is 2 minutes
Firstly you go at e7 which is 7 minutes away + 2 minutes the delivery
Secondly you go at e5 which is 2 minutes away from e7 + 2 minutes delivery time
Thirdly you go at e4 which is 1 minutes away from e5 + 2 minutes delivery time
Go back to the store which is 4 minutes away from e4
Time2= Time1+22 = 42 minutes

📦📦📦You load 3 packages which is 2 minutes
Firstly you go at n13 which is 13 minutes away + 2 minutes the delivery
Secondly you go at n9 which is 4 minutes away from n13 + 2 minutes delivery time
Thirdly you go at n7 which is 2 minutes away from n9 + 2 minutes delivery time
Go back to the store which is 7 minutes away from n7
Time3= Time2+34 = 76 minutes

📦📦You load 2 packages which is 2 minutes
Firstly you go at w2 which is 2 minutes away + 2 minutes the delivery
Secondly you go at w1 which is 1 minutes away from w2 + 2 minutes delivery time
Go back to the store which is 1 minutes away from w1
Time4= Time3+10 = 86 minutes

📦📦You load 2 packages which is 2 minutes
Firstly you go at e2 which is 2 minutes away + 2 minutes the delivery
Secondly you go at e1 which is 1 minutes away from e2 + 2 minutes delivery time
Go back to the store which is 1 minutes away from e1
Total= Time4+10 = 96 minutes
```