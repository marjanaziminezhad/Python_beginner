 
    Download the file cyano.tar.gz. It contains FASTA files which were downloaded from a database of Cyanobacterial strains.

    What file type is cyano.tar.gz?
        (base) marjan@marjan-VirtualBox:~/Downloads$ file cyano.tar.gz
cyano.tar.gz: gzip compressed data, last modified: Thu Sep 12 14:59:53 2019, from Unix, original size modulo 2^32 849920
    Unpack the archive on the command line. (Hint)
        (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2$ tar -zxvf cyano.tar.gz 
    List the directory contents. You can pipe the output of the ls command into less - which advantage does this have?
        (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2$ cd ./cyanotype_db_orig
        base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ ls |less
        with less the content is not opened directly in the script, but opened separately which makes it easier to scroll through the content, search for stuff and the terminal is not full with the whole content.

    How many files does the archive contain? (Hint)
         (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ ls -1 | wc -l
342
    What file type does the archive contain? Are the files large or small?
        (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ file 0343_HM486730_Trichodesmium_thiebautii_H9-4_\(a.k.a._H94\)___G.fasta 
0343_HM486730_Trichodesmium_thiebautii_H9-4_(a.k.a._H94)___G.fasta: ASCII text, with very long lines, with CRLF line terminators
(base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ wc -c 0343_HM486730_Trichodesmium_thiebautii_H9-4_\(a.k.a._H94\)___G.fasta 
702 0343_HM486730_Trichodesmium_thiebautii_H9-4_(a.k.a._H94)___G.fasta

    base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ file 0343_HM486730_Trichodesmium_thiebautii_H9-4_\(a.k.a._H94\)___G.fasta 
0343_HM486730_Trichodesmium_thiebautii_H9-4_(a.k.a._H94)___G.fasta: ASCII text, with very long lines, with CRLF line terminators

(base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ ll -h | less 

    List all files where "Cyano" is part of the file name. How many such files are there? Perform this task using:
        ls (info about wildcards and pathname expansion is here and here)
            (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ ls *Cyano* *cyano* | wc -l
                25
(           base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ ls *Cyano* *cyano*

        the find command; e.g., the general syntax to find a file that ends in .txt in the current directory or subdirectories is find . -name "*.txt"
        (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ find *cyano* *Cyano*
0006_NZ_KB904821_filamentous_cyanobacterium_sp._ESFC-1___G.fasta
0022_NZ_AP012549_unidentified_cyanobacterium_EtSB___G,co-culture.fasta
0060_LICO01000137_unidentified_cyanobacterium_(Cyanobium_sp.)_BACL30_MAG-120619-bin27___G.fasta
0103_JPSP01000003_Atelocyanobacterium_thalassa_SIO64986___(T),G,u.fasta
0171_CP001842_Atelocyanobacterium_thalassa_ALOHA_(phylotype_UCYN-A)___G,u.fasta
0256_ALWA01000027_unidentified_cyanobacterium_PCC_7702___G.fasta
0290_AF132931_Stanieria_cyanosphaera_PCC_7437___(T),R,G.fasta

    (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ echo *cyano* | wc -w
7
(base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ find *cyano* | nl
     1  0006_NZ_KB904821_filamentous_cyanobacterium_sp._ESFC-1___G.fasta
     2  0022_NZ_AP012549_unidentified_cyanobacterium_EtSB___G,co-culture.fasta
     3  0060_LICO01000137_unidentified_cyanobacterium_(Cyanobium_sp.)_BACL30_MAG-120619-bin27___G.fasta
     4  0103_JPSP01000003_Atelocyanobacterium_thalassa_SIO64986___(T),G,u.fasta
     5  0171_CP001842_Atelocyanobacterium_thalassa_ALOHA_(phylotype_UCYN-A)___G,u.fasta
     6  0256_ALWA01000027_unidentified_cyanobacterium_PCC_7702___G.fasta
     7  0290_AF132931_Stanieria_cyanosphaera_PCC_7437___(T),R,G.fasta

    Can you identify the strains that have the motif TGAAAAGTG in their sequence? You can use grep, which has a useful option for such cases, --recursive. The syntax is grep --recursive PATTERN DIRECTORY. What is the short option form of the --recursive option?
    grep -r -l TGAAAGTG 
    # -l prints the name of each input file from which output would normally have been printed
    # The short term for --recursive is -r. Reads all files under each directory. If no file operand is given, grep searches the working directory.


    Concatenate all files into one and give it a meaningful name. (Hint)
        (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ grep --recursive TGAAAAGTG 
        (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ cat *.fasta > CyanoDATA.txt

0275_AGRF01000080_Prochloron_didemni_P1-Palau___r_,G,u_.fasta:GATGAACGCTGGCGGTATGCTTAACACATGCAAGTCGAACGAACTCTTCGGAGTTAGTGGCGGACGGGTGAGTAACGCGTGAGAATCTACCTCAAGGACGGGGACAACAGCAGGAAACTGGTGCTAATACCCGATAAGCTGAAAAGTGAAAGATTTATTGCCGAGAGAGGAGCTCGCGTCCGATTAGCTAGTTGGAAGGGTAAAAGCCTACCAAGGCGACGATCGGTAGCTGGTCTGAGAGGATGATCAGCCACACTGGGACTGAGACACGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATTTTCCGCAATGGGCGAAAGCCTGACGGAGCAATACCGCGTGAGGGAAGAAGGCTTTTGGGTTGTAAACCTCTTTTGTCAGGGAAGAAGAATTGACGGTACCTGAAGAAAAAGCATCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGATGCAAGCGTTATCCGGAATCATTGGGCGTAAAGGGTCCGCAGGTGGCGAATAAAGTCTGCTGTTAAAGACCGGGGCTAAACTCCGGAAAGGCAGTGGAAACTGATTAGCTAGAGTACGGTAGGGGTAGAGGGAATTCCCAGTGTAGCGGTGAAATGCGTAGATATTGGGAAGAACACCGGTGGCGAAAGCGCTCTACTAGGCCGAAACTGACACTGAGGGACGAAAGCTAGGGTAGCGAAAGGGATTAGATACCCCTGTAGTCTTAGCGGTAAACGATGGATACTAGGTGTAGCTTGTATCGACCCGAGCTGTGCCGAAGCTAACGCGATAAGTATCCCGCCTGGGGAGTACGCACGCAAGTGTGAAACTCAAAGGAATTGACGGGGGCCCGCACAAGCGGTGGAGTATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCAGGGCTTGACATGTCGCGAATCTAGCGGAAACGTTAGAGTGCCTTAGGGAATGCGAACACAGGTGGTGCATGGCTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTCGTCCTTAGTTGCCAATATTAAGTTAGGCACTCTAGGGAGACTGCCGGGGACAACTCGGAGGAAGGTGGGGATGACGTCAAGTCAGCATGCCCCTTACGTCCTGGGCGACACACGTACTACAATGGTTGGGACAAAGGGCAGCAAACTCGCGAGAGTAAGCGAATCTCATCAAACCCAGCCACAGTTCAGATTGCAGGCTGCAACTCGCCTGCATGAAGTAGGAATCGCTAGTAATCGCAGGTCAGCATACTGCGGTGAATTCGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGAAGCTGGCTACGCCCGAAGTCGTTACCCTAACCCGGTTTTGGGAGGGGGATGCCGAAGGTAGAGCTAGTGACTGGGGTGAAGTCGTAACAAGGTAGCCGTACCGGAA
0003_X63141_Prochloron_didemni___t,r_,u.fasta:GATGAACGCTGGCGGTATGCTTAACACATGCAAGTCGAACGAACTCTTCGGAGTTAGTGGCGGACGGGTGAGTAACGCGTGAGAATCTACCTCAAGGACGGGGACAACAGCAGGAAACTGGTGCTAATACCCGATAAGCTGAAAAGTGAAAGATTTATTGCCGAGAGAGGAGCTCGCGTCCGATTAGCTAGTTGGAAGGGTAAAAGCCTACCAAGGCGACGATCGGTAGCTGGTCTGAGAGGATGATCAGCCACACTGGGACTGAGACACGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATTTTCCGCAATGGGCGAAAGCCTGACGGAGCAATACCGCGTGAGGGAAGAAGGCTTTTGGGTTGTAAACCTCTTTTGTCAGGGAAGAAGAATTGACGGTACCTGAAGAAAAAGCATCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGATGCAAGCGTTATCCGGAATCATTGGGCGTAAAGGGTCCGCAGGTGGCGAATAAAGTCTGCTGTTAAAGACCGGGGCTAAACTCCGGAAAGGCAGTGGAAACTGATTAGCTAGAGTACGGTAGGGGTAGAGGGAATTCCCAGTGTAGCGGTGAAATGCGTAGATATTGGGAAGAACACCGGTGGCGAAAGCGCTCTACTAGGCCGAAACTGACACTGAGGGACGAAAGCTAGGGTAGCGAAAGGGATTAGATACCCCTGTAGTCTTAGCGGTAAACGATGGATACTAGGTGTAGCTTGTATCGACCCGAGCTGTGCCGAAGCTAACGCGATAAGTATCCCGCCTGGGGAGTACGCACGCAAGTGTGAAACTCAAAGGAATTGACGGGGGCCCGCACAAGCGGTGGAGTATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCAGGGCTTGACATGTCGCGAATCTAGCGGAAACGTTAGAGTGCCTTAGGGAATGCGAACACAGGTGGTGCATGGCTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTCGTCCTTAGTTGCCAATATTAAGTTAGGCACTCTAGGGAGACTGCCGGGGACAACTCGGAGGAAGGTGGGGATGACGTCAAGTCAGCATGCCCCTTACGTCCTGGGCGACACACGTACTACAATGGTTGGGACAAAGGGCAGCAAACTCGCGAGAGTAAGCGAATCTCATCAAACCCAGCCACAGTTCAGATTGCAGGCTGCAACTCGCCTGCATGAAGTAGGAATCGCTAGTAATCGCAGGTCAGCATACTGCGGTGAATTCGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGAAGCTGGCTACGCCCGAAGTCGTTACCCTAACCGGTTTTGGGA
0279_AFSJ01000552_Prochloron_didemni_P2-Fiji___G,u.fasta:GATGAACGCTGGCGGTATGCTTAACACATGCAAGTCGAACGGACTCTTCGGAGTTAGTGGCGGACGGGTGAGTAACGCGTGAGAATCTACCTCAAGGACGGGGACAACATCAGGAAACTGGTGCTAATACCCGATAAGCTGAAAAGTGAAAGATTTATTGCCTAGAGATGAGCTCGCGTCCGATTAGCTAGTTGGGAGGGTAAAAGCCTACCAAGGCAGATCGGTAGCTGGTCTGAGAGGATGAGCAGCCACACTGGGACTGAGACACGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATTTTCCGCAATGGGCGAAAGCCTGACGGAGCAATACCGCGTGAGGGAAGAAGGCTTTTGGGTTGTAAACCTCTTTTGTCAGGGAAGAAGAATTGACGGTACCTGAAGAAAAAGCATCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGATGCAAGCGTTATCCGGAATCATTGGGCGTAAAGGGTCCGCAGGTGGCGAATAAAGTCTGCTGTTAAAGACCGGGGCTAAACTCCGGAAAGGCAGTGGAAACTGATTAGCTAGAGTACGGTAGGGGTAGAGGGAATTCCCAGTGTAGCGGTGAAATGCGTAGATATTGGGAAGAACACCGGTGGCGAAAGCGCTCTACTAGGCCGAAACTGACACTGAGGGACGAAAGCTAGGGTAGCGAAAGGGATTAGATACCCCTGTAGTCTTAGCGGTAAACGATGGATACTAGGTGTAGCTTGTATCGACCCGAGCTGTGCCGAAGCTAACGCGATAAGTATCCCGCCTGGGGAGTACGCACGCAAGTGTGAAACTCAAAGGAATTGACGGGGGCCCGCACAAGCGGTGGAGTATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCAGGGCTTGACATGTCGCGAATCTAGCGGAAACGTTAGAGTGCCTTAGGGAATGCGAACACAGGTGGTGCATGGCTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTCGTCCTTAGTTGCCAATATTAAGTTAGGCACTCTAGGGAGACTGCCGGGGACAACTCGGAGGAAGGTGGGGATGACGTCAAGTCAGCATGCCCCTTACGTCCTGGGCGACACACGTACTACAATGGTTGGGACAAAGGGCAGCAACCTCGCGAGAGTAAGCGAATCTCATCAAACCCAGCCACAGTTCAGATTGCAGGCTGCAACTCGCCTGCATGAAGTAGGAATCGCTAGTAATCGCAGGTCAGCATACTGCGGTGAATTCGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGAAGCTGGCTACGCCCGAAGTCGTTACCCTAACCCGGTTTTGGGAGGGGGATGCCGAAGGTAGAGCTAGTGACTGGGGTGAAGTCGTAACAAGGTAGCCGTACCGGAAGG
0329_X78680_Gloeothece_membranacea_PCC_6501___R.fasta:GATGAACGCTGGCGGCGTGCCTAACACATGCAAGTCGAACGGGGTAGAAATACCTAGTGGCGGACGGGTGAGTAACGCGTGAGAATCTGCCTTCAGGATGGGGACAACAGCGGGAAACGGCTGCTAATACCCGATAGGCTGAAAAGTGAAAGATTTATCGCCTGAAGAGGAGCTCGCGTCTGATTAGCTAGTTGGTAGGGTAAAAGCCTACCAAGGCGACGATCAGTAGCTGGTCTGAGAGGATGAGCAGCCACACTGGGACTGAGACACGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATTTTCCGCAATGGGCGAAAGCTGACGGAGCAACGCCGCGTGAGGGAGGAAGGCCCTTGGGTTGTAAACCTCTTTTCTGGGGGAAGAAGTAATGACGGTACCCCAGGAATAAGCATCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGATGCAAGCGTTATCCGGAATCATTGGGCGTAAAGCGTCCGCAGGTGGCTATTCAAGTCTGCTGTCAAAGCATGGAGCTTAACTCCATAGAGGCAGTGGAAACTGAAAGGCTAGAGGCCGGTAGGGGTAGTGGGAATTCCCAGTGTAGCGGTGAAATGCGTAGAGATTGGGAAGAACATCGGTGGCGAAAGCGCACTACTGGGCAGGACCTGACACTGAGGGACGAAAGCTAGGGGAGCAAAAGGGATTAGATACCCCTGTAGTCCTAGCCGTAAACGATGGAGACTAGGCGTAGCTTGTATCGACCCAAGCTGTGCCGAAGCTAACGCGTTAAGTCTCCCGCCTGGGGAGTACGCACGCAAGTGTGAAACTCAAAGGAATTGACGGGGGCCCGCACAAGCGGTGGAGTATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCAGGGCTTGACATCTGGCGAATCAGGGGGAAACCTCGGAGTGCCTTCGGGAGCGCCAAGACAGGTGGTGCATGGCTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTCGTTTTTAGTTGCCATCATTAAGTTGGGCACTCTAGAGAGACTGCCGGTGACAAACCGGAGGAAGGTGGGGATGACGTCAAGTCAGCATGCCCCTTACGTCCTGGGCTACACACGTACTACAATGGTCGGGACAGAGGGCAGCAAACTCGCAAGAGCAAGCGAATCTCATCAAACTCGGCCTCAGTTCAGATTGCAGGCTGCAACTCGCCTGCATGAAGGAGGAATCGCTAGTAATCGCCGGTCAGCATACGGCGGTGAATTCGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGGAGCTGCCACGCCCGAAGTCGTTACCCTAACCCGAAAGGGAGGGGGATGCCGAAGGCAGGGCTAGTGACTGGGGTGAAGTCGTAACAAGGTAGCCGTACCGGAAGGTGTGGCTGGATCACCTCCTTT
0277_AGGA01000118_Prochloron_didemni_P4-Papua_New_Guinea___G,u.fasta:GATGAACGCTGGCGGTATGCTTAACACATGCAAGTCGAACGAACTCTTCGGAGTTAGTGGCGGACGGGTGAGTAACGCGTGAGAATCTACCTCAAGGACGGGGACAACAGCAGGAAACTGGTGCTAATACCCGATAAGCTGAAAAGTGAAAGATTTATTGCCGAGAGAGGAGCTCGCGTCCGATTAGCTAGTTGGAAGGGTAAAAGCCTACCAAGGCGACGATCGGTAGCTGGTCTGAGAGGATGATCAGCCACACTGGGACTGAGACACGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATTTTCCGCAATGGGCGAAAGCCTGACGGAGCAATACCGCGTGAGGGAAGAAGGCTTTTGGGTTGTAAACCTCTTTTGTCAGGGAAGAAGAATTGACGGTACCTGAAGAAAAAGCATCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGATGCAAGCGTTATCCGGAATCATTGGGCGTAAAGGGTCCGCAGGTGGCGAATAAAGTCTGCTGTTAAAGACCGGGGCTAAACTCCGGAAAGGCAGTGGAAACTGATTAGCTAGAGTACGGTAGGGGTAGAGGGAATTCCCAGTGTAGCGGTGAAATGCGTAGATATTGGGAAGAACACCGGTGGCGAAAGCGCTCTACTAGGCCGAAACTGACACTGAGGGACGAAAGCTAGGGTAGCGAAAGGGATTAGATACCCCTGTAGTCTTAGCGGTAAACGATGGATACTAGGTGTAGCTTGTATCGACCCGAGCTGTGCCGAAGCTAACGCGATAAGTATCCCGCCTGGGGAGTACGCACGCAAGTGTGAAACTCAAAGGAATTGACGGGGGCCCGCACAAGCGGTGGAGTATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCAGGGCTTGACATGTCGCGAATCTAGCGGAAACGTTAGAGTGCCTTAGGGAATGCGAACACAGGTGGTGCATGGCTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTCGTCCTTAGTTGCCAATATTAAGTTAGGCACTCTAGGGAGACTGCCGGGGACAACTCGGAGGAAGGTGGGGATGACGTCAAGTCAGCATGCCCCTTACGTCCTGGGCGACACACGTACTACAATGGTTGGGACAAAGGGCAGCAAACTCGCGAGAGTAAGCGAATCTCATCAAACCCAGCCACAGTTCAGATTGCAGGCTGCAACTCGCCTGCATGAAGTAGGAATCGCTAGTAATCGCAGGTCAGCATACTGCGGTGAATTCGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGAAGCTGGCTACGCCCGAAGTCGTTACCCTAACCCGGTTTTGGGAGGGGGATGCCGAAGGTAGAGCTAGTGACTGGGGTGAAGTCGTAACAAGGTAGCCGTACCGGAAGG
0278_AFSK01000854_Prochloron_didemni_P3-Solomon___G,u.fasta:GCTAATACCCGATAAGACTGAAAAGTGAAAGATTTATTGCCGAGAGAGGATCTCGCGTCCGATTAGCTAGTTGGGAGGGTAAAAGCCTACCAAGGCGACGATCGGTAGCTGGTCTGAGAGGATGAGCAGCCACACTGGGACTGAGACACGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATTTTCCGCAATGGGCGAAAGCCTGACGGAGCAATACCGCGTGAGGGAAGAAGGCTTTTGGGTTGTAAACCTCTTTTGTCAGGGAAGAAGAATTGACGGTACCTGAAGAAAAAGCATCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGATGCAAGCGTTATCCGGAATCATTGGGCGTAAAGGGTCCGCAGGTGGCGAATAAAGTCTGCTGTTAAAGACCGGGGCTAAACTCCGGAAAGGCAGTGGAAACTGATTAGCTAGAGTACGGTAGGGGTAGAGGGAATTCCCAGTGTAGCGGTGAAATGCGTAGATATTGGGAAGAACACCGGTGGCGAAAGCGCTCTACTAGGCCGAAACTGACACTGAGGGACGAAAGCTAGGGTAGCGAAAGGGATTAGATACCCCTGTAGTCTTAGCGGTAAACGATGGATACTAGGTGTAGCTTGTATCGACCCGAGCTGTGCCGAAGCTAACGCGATAAGTATCCCGCCTGGGGAGTACGCACGCAAGTGTGAAACTCAAAGGAATTGACGGGGGCCCGCACAAGCGGTGGAGTATGTGGTTTAATTCGATGCAACGCGAAGAACCTTACCAGGGCTTGACATGTCGCGAATCTAGCGGAAACGTTAGAGTGCCTTAGGGAATGCGAACACAGGTGGTGCATGGCTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTCGTCCTTAGTTGCCAATATTAAGTTAGGCACTCTAGGGAGACTGCCGGGGACAACTCGGAGGAAGGTGGGGATGACGTCAAGTCAGCATGCCCCTTACGTCCTGGGCGACACACGTACTACAATGGTTGGGACAAAGGGCAGCAAACTCGCGAGAGTAAGCGAATCTCATCAAACCCAGCCACAGTTCAGATTGCAGGCTGCAACTCGCCTGCATGAAGTAGGAATCGCTAGTAATCGCAGGTCAGCATACTGCGGTGAATTCGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGAAGCTGGCTACGCCCGAAGTCGTTACCCTAACCCGGTTTTGGGAGGGGGATGCCGAAGGTAGAGCTAGTGACTGGGGTGAAGTCGTAACAAGGTAGCCGTACCGGAAGG

Useful: file, tar, ls, less, wc, ll, grep, find, cat

  A simple backup script

The code below is from an old basic Bash guide.

#!/bin/bash        
OF=/var/my-backup-$(date +%Y%m%d).tgz  # OF - output file
tar -cZf $OF /home/me/

    What does it do? making a back up from Home directory
    What type of expansion does it use? 
    (Hint, hint; what does the code file $(ls /usr/bin/* | grep bin/zip) from here do? Give another two examples of code that uses this mechanism.)
        Bash variables and command substitution
        base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ echo $(ls /usr/bin/* | grep bin/zip)
/usr/bin/zip /usr/bin/zipcloak /usr/bin/zipdetails /usr/bin/zipgrep /usr/bin/zipinfo /usr/bin/zipnote /usr/bin/zipsplit
    (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ echo $(ls /usr/bin/* | grep bin/*p)
    (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2/cyanotype_db_orig$ file $(ls /usr/bin/* | grep bin/zip)
    What does the file extension .tgz indicate, and what is the modern file extension for this (hint, hint)?
        every tarred, gzipped or bzipped has a file extension like .tar, .tar.gz or .tgz. but just for human
        I think in the old package repo days, .tgz was used because files on DOS floppies could only have three letter extensions. When this limitation was removed, .tar.gz was used to be more verbose by showing both the archive type (tar) and zipper (gzip).
    When I try to execute the code, I get the error message /bin/sh: 1: compress: not found. What is the problem, and how can it be solved? Test the command/script using a small directory instead of your home directory. After executing the command, what is the only way to make sure that it really ran successfully?
ein compressor ist nicht installiert worden. entweder mit kleinem z oder package installieren.es kann sein dass der Code veraltet ist.
    8  Bash and Biology: FASTA files

FASTA files are plain text files containing a biological sequence. They consist of:

    Single-line header (description, defline), defined by a > symbol. The header contains the unique sequence identifier (the string between > and the first whitespace) and an optional comment (description)
    One or multiple lines of sequence data (amino acid or nucleotide sequence)

Multifasta files contain multiple FASTA formated sequences. They are usually also called FASTA files, and have a file extension like .fasta, .fa, .faa (amino acids), .fna (nucleotide sequence), or other. Example:

>SEQUENCE_1 This is the sequence 1 header line 
MTEITAAMVKELRESTGAGMMDCKNALSETNGDFDKAVQLLREKGLGKAAKKADRLAAEG
LVSVKVSDDFTIAAMRPSYLSYEDLDMTFVENEYKALVAELEKENEERRRLKDPNKPEHK
IPQFASRKQLSDAILKEAEEKIKEELKAQGKPEKIWDNIIPGKMNSFIADNSQLDSKLTL
MGQFYVMDDKKTVEQVIAEKEKEFGGKIKIVEFICFEVGEGLEKKTEDFAAEVAAQL
>SEQUENCE_2 Here can be any kind of additional information/description
SATVSEINSETDFVAKNDQFIALTKDTTAHIQSNSLQSVEELHSSTINGVKFEEYLKSQI
ATIGENLVVRRFATLKAGANGVVNGYLLRQICMH

Many simple file manipulations can be done using Bash utilities. Here are some typical applications:

    Count the number of sequences in the FASTA file
    (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2$ grep '>' Fasta.fa | wc -l
    base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2$ grep -c "^>" file.headers.fa
2
    Explain what that code does: sed 's/>.*/&ADDITIONALTEXT/' file.fa > file.headers.fa (Hint: gnu.org, unix.stackexchange.com)
    adds die things after />.*/
    . matches any charachter and star matches every numb. (number of  repetitions)
    Discard any text after the sequence identifier from the description line
    Explain what this code does: awk '{print $1}' file.fa > output.fa (Hint)
    first word of each line.
cut the first word ( any white space)
Sometimes the separator in some files is not space nor tab but something else. You can specify it using –F option
    Extract only the sequence data from the FASTA file (remove header lines)
    falsch(base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2$ grep -F '>' Fasta.fa 
    (base) marjan@marjan-VirtualBox:~/Documents/Exercise/sheet2$ grep -v -i  ">sequence" Fasta.fa 
    You have a malformatted FASTA file with some empty lines. How do you get rid of them?
    ??awk '/>/ {print $1}' Fasta.fa | tr -d ">"
    Extract only the sequence ids from the FASTA file (Hint: this can be done e.g. with awk + tr, or with egrep + tr)
    ??????
Useful: grep, sed, awk, wc, tr, regular expressions, redirection

Hints:

    You can test your commands on a small FASTA file, containing e.g. the two sequences above.
    Essential regex examples: ryanstutorials.net, likegeeks.com

    9  TED Ed: "Think like a coder", episode 2

Apart from the loop, another basic control flow construct is the conditional. It allows to perform different computations or actions depending on the situation (a condition that evaluates to true or false). Watch this episode and answer the following questions:

    What is a conditional?
        Bash expression is the combination of operators, features, or values used to form a bash conditional statement. Conditional expression could be binary or unary expression which involves numeric, string or any commands whose return status is zero when success
    Can conditionals be nested?
        yes,Sometimes referred to as multiway branching, nested conditionals are the case where the else part of an if statement is itself an if statement.

    Every algorithm should first be formulated as pseudocode. Pseudocode is a plain language description of the steps in an algorithm. It often uses structural conventions of a programming language, but is intended for humans rather than computers (Wikipedia: Pseudocode). In the pseudocode below, the indent defines code blocks, i.e. instructions that have the same indent belong together. For example:

ask user for value of "a"
if a > 5:
    print "yay" 
    print "a is larger than 5" 
else:
    print "oh no"
    print "a is smaller than 5"

In this case, the output will be either "yay" and "a is larger than 5" (if the user-given value of a is larger than 5), or "oh no" and "a is smaller than 5". (What will happen if the user-provided value is 5?)

Your task is to complete the missing "Test for hair color" section in the pseudocode below.

# This code identifies the rebellion leader based on a personal description
# It checks each person for several characteristics, until leader is found
Initialize rebellion_leader = None
While rebellion_leader is None:  # main loop

    # Test for eye color
    Get eye_color of person
    If eye_color is green:
        eye_color_test = ok
    Else:
        Continue (to next person, i.e. next loop iteration)

    # Test for hair color
    Get hair_color of the person
    If the_hair_color is red:
    Get name of the person
        If name of the person has 2 consecutive double letter
            hair_color test = ok
        else:
         continue
     else: 
        hair_color test = ok   

    # Test for glasses
    Get glasses of person
    Get name of person
    If glasses:
        If name has 2 vowels:
            glasses_test = ok
        Else:
            Continue
    Else:  # no glasses
        If name has 3 vowels:
            glasses_test = ok
        Else:
            Continue

    # All tests passed, looks good 
    Set rebellion_leader to person

    import sys  # import module for system-specific functionality


10  Create a range of numbers

space time rechner 
The built-in range function produces a series of integers.
# General syntax: range(start, stop, step)
>>> range(10, 15)  # or print(range(10, 15))
range(10, 15)
The range function is called with 1, 2 or 3 arguments and returns a range object (an object of type range), which represents a series of integers
Range objects support indexing, slicing, equality checks etc.
Ranges can be converted to other types like lists. This is called type conversion or type casting:
>>> list(range(15, 5, -2))  # create list object from range object
[15, 13, 11, 9, 7]
In Python 2, the range function returned a list. But Python 3 is lazy whenever possible, to reduce memory consumption and computational cost. Therefore it introduced a new "range" type. Why does the range object save memory, in comparison to a list object?
A list keeps all its items in memory. E.g., a list with 2000 numbers needs twice as much memory as a list with 1000 numbers
The range object calculates the next item only as you need it ("at runtime"), therefore it takes up a very small and constant amount of memory. E.g., the objects range(10) and range(1000000) require the same amount of memory
See for yourself. The function getsizeof in the sys module returns the size of an object in bytes (docs):
import sys  # import module for system-specific functionality

range1 = range(10)  # create range object and bind name `range1` to it
range2 = range(1000000)  # create another range object
# to double-check that they are different objects, use the `id()` function

print("Size of range(10) is", sys.getsizeof(range1), "bytes") 🡪 48 bytes
print("Size of range(1000000) is", sys.getsizeof(range2), "bytes") 🡪 48 bytes

print("Size of range(10) converted to list is", sys.getsizeof(list(range1)), "bytes") 🡪 136 bytes
print("Size of range(1000000) converted to list is", sys.getsizeof(list(range2)), "bytes")  # how many megabytes? 🡪 8000056 bytes
Print a list of numbers between 1,000 and 10,000 in steps of 100:
[1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000]

print(list(range(1000, 10001, 100)))

duc typing
