#!/bin/bash
                                                                                
for i in {1..10}; do
  echo $i
  date > out$i
done

print "Done"

