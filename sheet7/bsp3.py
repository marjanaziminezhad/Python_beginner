{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "could not convert string to float: '--stdin=9013'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m/home/marjan/Documents/Exercise/sheet7/bsp3.ipynb Cell 1\u001b[0m in \u001b[0;36m<cell line: 7>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      <a href='vscode-notebook-cell:/home/marjan/Documents/Exercise/sheet7/bsp3.ipynb#W0sZmlsZQ%3D%3D?line=3'>4</a>\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39msys\u001b[39;00m\n\u001b[1;32m      <a href='vscode-notebook-cell:/home/marjan/Documents/Exercise/sheet7/bsp3.ipynb#W0sZmlsZQ%3D%3D?line=5'>6</a>\u001b[0m infile \u001b[39m=\u001b[39m sys\u001b[39m.\u001b[39margv[\u001b[39m1\u001b[39m]\n\u001b[0;32m----> <a href='vscode-notebook-cell:/home/marjan/Documents/Exercise/sheet7/bsp3.ipynb#W0sZmlsZQ%3D%3D?line=6'>7</a>\u001b[0m MIN_BITSCORE \u001b[39m=\u001b[39m \u001b[39mfloat\u001b[39;49m(sys\u001b[39m.\u001b[39;49margv[\u001b[39m2\u001b[39;49m])\n\u001b[1;32m      <a href='vscode-notebook-cell:/home/marjan/Documents/Exercise/sheet7/bsp3.ipynb#W0sZmlsZQ%3D%3D?line=7'>8</a>\u001b[0m MAX_EVALUE \u001b[39m=\u001b[39m \u001b[39mfloat\u001b[39m(sys\u001b[39m.\u001b[39margv[\u001b[39m3\u001b[39m])\n\u001b[1;32m     <a href='vscode-notebook-cell:/home/marjan/Documents/Exercise/sheet7/bsp3.ipynb#W0sZmlsZQ%3D%3D?line=9'>10</a>\u001b[0m \u001b[39mtry\u001b[39;00m:\n",
      "\u001b[0;31mValueError\u001b[0m: could not convert string to float: '--stdin=9013'"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python\n",
    "\"\"\"Filter tabular BLAST output\"\"\"\n",
    "\n",
    "import sys\n",
    "\n",
    "infile = sys.argv[1]\n",
    "MIN_BITSCORE = float(sys.argv[2])\n",
    "MAX_EVALUE = float(sys.argv[3])\n",
    "\n",
    "try:\n",
    "    N_HITS = int(sys.argv[4])\n",
    "except IndexError:\n",
    "    N_HITS = 3\n",
    "\n",
    "\n",
    "def filter_hit(bitscore, evalue):\n",
    "    \"\"\"Compares hit bitscore to min. bitscore, and hit E-value to max. E-value,\n",
    "    to decide if hit is accepted or rejected. Returns True or False.\"\"\"\n",
    "    return False\n",
    "\n",
    "\n",
    "previous = None\n",
    "with open(infile) as fin:\n",
    "    for line in fin:\n",
    "        # Default tabular BLAST output has 12 fields\n",
    "        qseqid, sseqid, pident, length, mismatch, gapopen, qstart, qend, sstart, send, evalue, bitscore = line.strip().split('\\t')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.6 (conda)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "f139eb95dc7458f532b463c4b0877e2c71664b376e1cbbde639cfe15fd546385"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
