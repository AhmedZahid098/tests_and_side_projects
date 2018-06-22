#!/usr/bin/bash

# echo commands
echo Hello World!

# variables (uppercase by convention) allowed letters, numbers, underscores
NAME=AHMED
echo "my name is $NAME"

# user input
read -p "Enter your name" NAME
echo "hello $NAME. Nice to meet you"

# Simple if statements and elif
if ["$NAME" == "AHMED"]
then echo "Your name is Ahmed"
elif ["$NAME" == "Ali"]
then
    echo "Your name is Ali"
fi

# COMPARIOSN

# v1 -eq v2 returns true if values are equal
# v1 -ne v2 returns true if values are not equal
# v1 -gt v2 returns true if v1 is greater than v2
# v1 -eq v2 returns true if v1 is greater than or equal v2
# v1 -lt v2 returns true if v1 is less than v2
# v1 -le v2 returns true if v1 is less than or equal to v2
num1=6
num2=5
if ["$num1" -gt "$num2"]
then
    echo "$num1 is greater than $num2"
fi

# File conditions

# -d file   True if the file is a directory
# -e file   True if the file exists (note that this is not particularly portable, thus -f is generally used)
# -f file   True if the provided string is a file
# -g file   True if the group id is set on a file
# -r file   True if the file is readable
# -s file   True if the file has a non-zero size
# -u    True if the user id is set on a file
# -w    True if the file is writable
# -x    True if the file is an executable

File="test.txt"
if [-e "$File"]
then
    echo "file exists"
else
    echo "file doesn't exist"
fi

# CASE STATEMENT
read -p "Are you 21 or over? Y/N " ANSWER
case "$ANSWER" in
    [yY] | [yY][eE][sS])
    echo "You can have a beer :)"
    ;;
    [nN] | [nN][oO])
    echo "Sorry, no drinking"
    ;;
   *)
    echo "Please enter y/yes or n/no"
    ;;
esac

# SIMPLE FOR LOOP
# NAMES="Brad Kevin Alice Mark"
# for NAME in $NAMES
#   do
#     echo "Hello $NAME"
# done

# FOR LOOP TO RENAME FILES
# FILES=$(ls *.txt)
# NEW="new"
# for FILE in $FILES
#   do
#     echo "Renaming $FILE to new-$FILE"
#     mv $FILE $NEW-$FILE
# done

# WHILE LOOP - READ THROUGH A FILE LINE BY LINE
# LINE=1
# while read -r CURRENT_LINE
#   do
#     echo "$LINE: $CURRENT_LINE"
#     ((LINE++))
# done < "./new-1.txt"

# FUNCTION
# function sayHello() {
#   echo "Hello World"
# }
# sayHello

# FUNCTION WITH PARAMS
# function greet() {
#   echo "Hello, I am $1 and I am $2"
# }

# greet "Brad" "36"

# CREATE FOLDER AND WRITE TO A FILE
# mkdir hello
# touch "hello/world.txt"
# echo "Hello World" >> "hello/world.txt"
# echo "Created hello/world.txt"
