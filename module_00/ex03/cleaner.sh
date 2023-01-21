#!/bin/sh

awk -F\" '{for (i=2; i<=NF; i+=2) gsub(/,/,"",$i)} 1' OFS="\"" ../ex02/hh_sorted.csv > temp.csv

head -n 1 temp.csv > hh_positions.csv | cat
tail -n +2 temp.csv | \
awk 'BEGIN { FS = OFS = "," }
    {
        STR = ""

        if (index(tolower($3), "junior"))
            STR = STR"Junior/"
        if (index(tolower($3), "middle"))
            STR = STR"Middle/"
        if (index(tolower($3), "senior"))
            STR = STR"Senior"
        if (STR == "")
            STR = "-"

        gsub(/[\/ ]*$/, "", STR)

        $3 = "\""STR"\""
        print
    }' \
>> hh_positions.csv

rm temp.csv
