#!/bin/bash
#chmod +x bash.sh to make it readble 
# sh ./bash.sh to call it
#sh ./bash.sh $1(first arg) $2 (2nd arg) ...
my_name=$1  # assign value of positional parameter to variable
temp=$2 
temp_F=$(($2*18/10+32)) #The Bash shell has a large list of supported arithmetic operators to do math calculations. They work with the let, declare, and arithmetic expansion methods described further below in this post.
num_of_arg=$# #($#) Expands to the number of positional parameters in decimal. 

echo "Hello, $my_name  \nits $temp °C = $temp_F Fahrenheit outside. \nI have $# arguments" # \n splites the line

echo $1
echo "$my_name"