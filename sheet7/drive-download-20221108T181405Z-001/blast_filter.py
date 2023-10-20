#!/usr/bin/env python

# import packages
import sys


def open_file(infile):
    """Doing a list of lists from the whole file. Each hit is a list."""

    # Define variables
    table_line = ""
    table_list = []  # generates an empty list

    # Opens the file and writes each line as list into a new list
    with open(infile) as fin:
        for line in fin:  # reads over each line using for loop
            table_line = line.split(
                "\t"
            )  # splits the line at every tab character # removes newline charakter in 12th column
            table_list.append(table_line)  # appends the generated line to the empty
        return table_list


def filter_hits(bitscore, evalue):
    """Filter each list in list according to bitscore and evalue"""
    # Filtering hits by  bitscore and evalue.

    filtered_list = []  # generate an empty list for filtered results
    for hit in open_file(infile):  # iterate over list
        if float(hit[11]) > float(bitscore) and float(hit[10]) < float(
            evalue
        ):  # check if bitscore and evalue, elements of lists are string, therefore convert list item to integer
            filtered_list.append(hit)  # append matching hit to filtered list
    return filtered_list


def max_n(result_n):

    """Check max n for each sequence."""

    results = []
    count = 0

    for hit in filter_hits(bitscore, evalue):

        if hit[0] not in (item for sublist in results for item in sublist):
            count += 1
            results.append(hit)

        elif (
            hit[0] in (item for sublist in results for item in sublist)
            and count < result_n
        ):
            count += 1
            results.append(hit)

    return results


def write_file():
    """Writes a file with elements of each list separated by a \t character."""

    # write lines to a new file
    parsed_line = ""  # generates an empty string called parsed_line, we need it for outputting the file
    output = open("Output_blast.txt", "w")  # determines output file

    for hit in max_n(result_n):  # for loop over our filtered list
        parsed_line = hit  # saves each list in our list as parsed_line
        n = 0  # sets the counter to 0
        while n < (len(parsed_line) - 1):  # while loop adds the tab after each element
            # checks for the length of our parsed line which is 12 and substracts 1 because counting of the columns starts with 0
            # if we use 4 instead of (len(parsed_line) - 1) it makes a tab after every 5 th element in the list
            output.write(
                parsed_line[n] + "\t"
            )  # with this command we write each element of our sub-list into the file separated from the next element with tab
            n += 1  # always count + 1 so the program knows how many entries we have written in our file, after we jump back to the outer for loop and work through the next line
        output.write(parsed_line[n])  # adds last column


# Executes script
if __name__ == "__main__":
    infile = "Testtable.txt"
    bitscore = 9
    evalue = 3
    result_n = 3

    try:
        result_n = int(sys.argv[4])
    except IndexError:
        result_n = 3

    write_file()
