#!/bin/sh

FILEPATH="../ex03/hh_positions.csv"
awk ' BEGIN { FS = "\",\"|T" }
    {
        if (NR == 1)
            START = $0
        else
        {
            if (!($2 in files))
            {
                file = $2".csv"
                files[$2]
                print START > file
            }
            print >> file
        }
    }' ${FILEPATH}
