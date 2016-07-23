import os
import pandas as pd
import sys

def sort_file(filename):
    df = pd.read_csv(filename,index_col='row_id',dtype={'row_id':int})
    df.sort_index(inplace=True)
    df.to_csv('sorted_'+filename)


# filename = first parameter
if len(sys.argv) < 2:
    print "Usage: python sort_csv.py <filename>"
    exit()

filename = sys.argv[1] 
if not filename.startswith("sorted_") and os.path.isfile('sorted_'+filename):
    print filename,"already sorted"
elif not filename.startswith("sorted_") and filename.endswith('.csv'):
    print "sorting",filename
    sort_file(filename)
        

