#!/bin/sh

awk 'NR == 1 || FNR > 1' *.csv > merge_date.csv

# diff merge_date.csv ../ex03/hh_positions.csv
