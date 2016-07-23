import os
import pandas as pd

def sort_file(filename):
    df = pd.read_csv(filename,index_col='row_id',dtype={'row_id':int})
    df.sort_index(inplace=True)
    df.to_csv('sorted_'+filename)


for filename in os.listdir(os.getcwd()):
    if not filename.startswith("sorted_") and os.path.isfile('sorted_'+filename):
        print filename,"already sorted"
    elif not filename.startswith("sorted_") and filename.endswith('.csv'):
        print "sorting",filename
        sort_file(filename)
        

