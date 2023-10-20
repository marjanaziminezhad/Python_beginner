#4  Two ways to print a line: performance considerations


#Generate some dummy text files (askubuntu.com: /dev/urandom, Wikipedia: Base64):

base64 /dev/urandom | head -c 1000000 > dummy1.txt
base64 /dev/urandom | head -c 10000000 > dummy2.txt
base64 /dev/urandom | head -c 100000000 > dummy3.txt
base64 /dev/urandom | head -c 1000000000 > dummy4.txt
#Below are two ways of printing the second line of a file (see grymoire.com, tldr.ostera.io).

sed -n '2p' dummy1.txt #sed -n suppress automatic printing of pattern space
sed '2q; d' dummy1.txt # q [exit-code] Immediately quit the sed script without processing
#any more input, except that if auto-print is not disabled the current
#pattern space will be printed. The exit code argument is a GNU
#extension.
#d Delete pattern space. Start next cycle.
#d From internet: “A useful command deletes every line that matches the restriction.”
#Our script tells the shall to stop processing at line 2 (2q) and deletes line 1 with. Of note, if we
#would set the 5q and 3d the first 5 lines would be used except for line 3 which is deleted with the
#d command. Therefore it is faster, because it does not work with the whole file, but only with the
#first 2 lines. This saves time when working with huge files.

#Both work. But which one is preferable, and why? For short files, there is no difference. However, we might need to print the second line of a very large file. Let's perform an experiment. First, generate some random data:
 
#second one.

#Now, perform a timing experiment:

for file in dummy*.txt; do
    echo
    echo "--- Test subject: $file ---"
    echo "First approach ("2p") : "; time sed -n '2p' $file > /dev/null
    echo
    echo "Second approach ('2q;d') : "; time sed '2q; d' $file > /dev/null
done

    #What is the outcome? Can you explain it?
    #What do "real", "user" and "sys" mean in the output of time? (Hint)


    #Real is wall clock time - time from start to finish of the call. This is all elapsed time including time slices used by other processes and time the process spends blocked (for example if it is waiting for I/O to complete).

    #User is the amount of CPU time spent in user-mode code (outside the kernel) within the process. This is only actual CPU time used in executing the process. Other processes and time the process spends blocked do not count towards this figure.

    #Sys is the amount of CPU time spent in the kernel within the process. This means executing CPU time spent in system calls within the kernel, as opposed to library code, which is still running in user-space. Like 'user', this is only CPU time used by the process. See below for a brief description of kernel mode (also known as 'supervisor' mode) and the system call mechanism.

#< /dev/null is used to instantly send EOF to the program, so that it doesn't wait for input (/dev/null, the null device, 
#is a special file that discards all data written to it, but reports that the write operation succeeded, 
#and provides no data to any process that reads from it, yielding EOF immediately).
#Redirecting /dev/null to stdin will give an immediate EOF to any read call from that process. 
#This is typically useful to detach a process from a tty (such a process is called a daemon). 
#For example, when starting a background process remotely over ssh, you must redirect stdin to prevent the process waiting for local input.
#Another reason to redirect to /dev/null is to prevent an unused file descriptor being created for stdin. 
#This can minimize the total open file handles when you have many long running processes.




