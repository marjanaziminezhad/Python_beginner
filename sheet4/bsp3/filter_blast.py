#!/usr/bin/env python

"""Filter tabular BLAST: Get best hit for each query.

Hits are ordered by bitscore, so the best hit is simply the first line
with a new query sequence.
"""

import sys

blast_result = sys.argv[1]

with open(blast_result) as fin:
    previous = None
    for line in fin:
        items = line.split()
        if previous == items[0]:
            continue
        else:
            previous = items[0]
            print(line.strip())
