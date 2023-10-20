#!/bin/bash
# Make a backup set of files
#The break statement tells Bash to leave the loop straight away. It may be that there is a normal situation that should 
#cause the loop to end but there are also exceptional situations in which it should end as well.
#For instance, maybe we are copying files but if the free disk space get's below a certain level we should stop copying.

DIR=$1            #$1 is the positional paramter and holds the command line argument. The result is assigend to(zugewiesen) DIR.
for value in $DIR/*; do         #we start the for loop and go through each value in our directory 
    used=$( df $DIR | tail -1 | awk '{ print $5 }' | sed 's/%//' )      # $(...) allows command substitution, i.e. allows the output of a command to replace the command itself and can be nested" first evaluate this, and then evaluate the rest of the line"
                                                                        # df reports file system disk space useage of our Directory | tail -1 outputs the last line of df | 
                                                                        # awk takes the 5th field of the line | sed cuts % with s/regexp/replacement probier #s/%/abc//''
                                                                        # after this command, used should be bound to a number that is our disk space useage in percent
    if [ $used -gt 90 ]; then               # if our value of used is greater than 90 then
        echo Low disk space 1>&2            # write: Low disk space , 1>$2 means redirect strout (Standard Output, 1) to stderr (Standard Error, 2);
                                            #& indicates that what follows and precedes is a file descriptor, and not a filename. Thus, we use 2>&1. Consider >& to be a redirect merger operator.
                                            # 0 :stdin , 1 :stdout , 2:stderr are three data streams that bash creates to transfer data
                                        
                                           
        break                               # leave the loop 
    fi                                      # fi closes the if statement which means that it should continue with the next line
    cp -r $value $DIR/backup/                  # make a copy of the value in the $Dir/backup/ directory
done                                        # done ends the for loop

#(base) marjan@marjan-VirtualBox:~/Documents$ df Exercise/
#Filesystem     1K-blocks     Used Available Use% Mounted on
#/dev/sda5       71151768 25459680  42032056  38% /
#(base) marjan@marjan-VirtualBox:~/Documents$ df Exercise/ | tail -1
#/dev/sda5       71151768 25459680  42032056  38% /
#(base) marjan@marjan-VirtualBox:~/Documents$ df Exercise/ | tail -1 | awk '{ print $5 }' 
#38%
#(base) marjan@marjan-VirtualBox:~/Documents$ df Exercise/ | tail -1 | awk '{ print $5 }' | sed 's/%//'
#38
#(base) marjan@marjan-VirtualBox:~/Documents$ echo Low disk space 1>&2 
#Low disk space

#base) marjan@marjan-VirtualBox:~/Documents$ sh Exercise/sheet3/4.exercise.sh Exercise
#cp: cannot create regular file 'Exercise/backup/': Not a directory
#cp: -r not specified; omitting directory 'Exercise/sheet1'
#cp: -r not specified; omitting directory 'Exercise/sheet2'
#cp: -r not specified; omitting directory 'Exercise/sheet3'
#(base) marjan@marjan-VirtualBox:~/Documents$ sh Exercise/sheet3/4.exercise.sh Exercise



# mit ls alles DIRs finden und in commands DIR = ein directory 
#for value in $DIR/+ ; do lsor echo  value 
#