import os
import pandas as pd
import subprocess

def sort_file(dir,filename):
    df = pd.read_csv(dir+'/'+filename,index_col='row_id',dtype={'row_id':int})
    df.sort_index(inplace=True)
    df.to_csv(dir+'/sorted_'+filename)


for filename in os.listdir("models"):
    if not filename.startswith("sorted_") and os.path.isfile('models/sorted_'+filename):
        print filename,"already sorted"
    elif not filename.startswith("sorted_") and filename.endswith('.csv'):
        print "sorting",filename
        sort_file("models",filename)
        

