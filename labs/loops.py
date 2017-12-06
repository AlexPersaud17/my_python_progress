##         TO-DO List
## 1.  Run this program to see the output
## 2.  See what happens if you change the comparison
##     in the while-header from 5 to 10 (i.e. count <= 10)
## 3a. See what happens if you comment out the line "count = count + 1"
## 3b. Now uncomment the line mentioned in 3a.
## 4.  Modify the original code provided so that
##     it prints  the following:

##     Program prints the word "Python" 6 times,
##     it prints the line number at the beginning of each line
##     and prints "IS FUN" in the last line (Termination)
##     Output:
##
##    1 Python
##    2 Python
##    3 Python
##    4 Python
##    5 Python
##    6 Python
##    IS FUN!

def main():

    count = 1                       # Initialization
    ITERATIONS = 6 

    while count <= ITERATIONS:               # Processing 
       print(count, "Python")
       count = count + 1
       
    print("IS FUN")                   # Termination


main()
