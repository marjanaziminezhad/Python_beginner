#!/usr/bin/env bash

# Using "strict mode" according to https://olivergondza.github.io/2019/10/01/bash-strict-mode.html
set -euo pipefail
trap 's=$?; echo >&2 "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR  # The trap prints to standard error (>&2)

# The goal is to obtain a very basic overview over the microbial diversity
# of freshwater bacteria associated with Microcystis blooms.
# The data consists of 16S rRNA amplicon sequences of freshwater cyanobacteria.
# Download the FASTQ file from NCBI Sequence Read Archive:
# https://www.ncbi.nlm.nih.gov/sra/SRX7554357[accn] -> https://trace.ncbi.nlm.nih.gov/Traces?run=SRR10885256

### Set variables
# The database file contains all known Cyanobacterial 16S rRNA sequences
db_file=/home/marjan/Documents/Exercise/sheet4/bsp3/cyano_data.fasta     # bind the name db_gfile to our cyano fasta file path 
datafile=/home/marjan/Documents/Exercise/sheet4/bsp3/SRR10885256.fastq  # bind the name datafile to the file we want to compare it to, which was downloaded and extracted from the ncbi link above; it was a fastaq.gz file

### Prepare folder structure
mkdir -p /home/marjan/Documents/Exercise/sheet4/bsp3/cyano/blastn            # make a parent directory 
cd /home/marjan/Documents/Exercise/sheet4/bsp3/cyano/blastn                   # go to the parent direcotry
mkdir -p data db results                    # create three more parent direcotrys within the blasn directory with the name: data, db, and results

### Create BLAST db
cd db                   # go to db directory

ln -s $db_file         # make a symbolic link to the db_file 
db_file=$(basename $db_file)        # basename gives only the filename; the $ character introduces parameter eypansion, command substitution, or arithmetic expansion. 
makeblastdb -dbtype nucl -in $db_file -logfile makeblastdb.log  # application to create blast database; required argument dbtype (string,nucl or prot --> molecule type of database), 
                                                                # optional -in --> input file , -logifle file to which the program log should be redirected
echo "Database done."       #write the database is done
echo

cd ..                       #change directory one level up

### Prepare input data
cd data                     # change directory to data

ln -s $datafile             # create a symbolic link to the datafile
datafile=$(basename $datafile) #basename gibt aus einem pfadnamen den Dateinamen ohne führende Verzeichnisnamen aus

# Convert FASTQ to FASTA 
# https://stackoverflow.com/questions/1542306/converting-fastq-to-fasta-with-sed-awk
sed -n '1~4s/^@/>/p; 2~4p' <$datafile > ${datafile%.fastq*}.fasta && rm $datafile        # -n is for silent; s is for regular expression replacement; we exchange starting @ with >  sed changes the datafile input (<) and redirects it to a new fasta file and the symbolic link SRR*.fastq is removed
# starting on line 1, and every 4th line thereafter, when you see a @ character at the beginning of a line, substitute it with a > character, and print the resulting line; then, starting at line 2, and every 4th line thereafter, just print the line". T
datafile=${datafile%.fastq*}.fasta      # bind name datafile to the new fasta file

# Dataset is too large, let's subsample. Easy way: convert multiline FASTA to single-line FASTA and use `head`
# https://www.biostars.org/p/9262/
cat $datafile | awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);}  END {printf("\n");}' | sed '1d' > tmp #load datafile with cat and pipe awk: the awk converts multiline to single line
# printf formats and prints data; the first printf is only for lines that start with > print a newLine for the previous sequence,
# then the header line on its own line $0 is for whole line, next print the sequence withouth new line;  
# at the END there is a line break 
# sed deletes the first line because it is empty after the awk command (see first printf command) and redirects the data to tmp
mv tmp $datafile    # we rename tmp 
# Take first 100 sequences
head -n 200 <$datafile >${datafile}.subsample  # head -n take the number of lines that are specified (in this case 200 since we want 100 sequences and a sequence has 2 lines)
                                            # and create a new file with subsample at the end of the filename (I checked with wc -l if it is really 200 lines long)
echo "Input data ok."
echo

cd ..  #change direcotry and go one branch up, we are now in the blastn directory again

# Run BLAST
time blastn -query data/${datafile}.subsample -task blastn -db db/$db_file -outfmt 6 > results/${datafile}.subsample.blastn.tab 
# the time command gives us the runtime of our process. -query is the input file name; -task is what to do; -db is blast database name; -outftm is the format output 6 stands for tab, this is redirected to .blast.tab datafile in the results directory
echo "Blast done."
echo

# Evaluate results - get best hit for every query
#cp ~/Downloads/filter_blast.py ~/projects/cyano/blastn/                 # copy the python script that is in the downloads folder to the blastn directory in which we are in right now
python /home/marjan/Documents/Exercise/sheet4/bsp3/filter_blast.py results/${datafile}.subsample.blastn.tab      # run the python script of our blastn file; we could also just write the path of the python file
echo "Processing results done."
echo
