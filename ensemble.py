from collections import Counter,defaultdict
import numpy as np
import os
import pandas as pd
import time

start_time=time.time()

def time_passed():
    return time.time() - start_time

scores={}

num_row_ids=8607230

def update_tally(preds,preds_per_row_id,weight):
    for i in range(len(preds)):
        if preds[i] in preds_per_row_id:
            curr = preds_per_row_id[preds[i]]
        else:
            curr = 0.0
        curr += weight/(i+1.0)
        preds_per_row_id[preds[i]] = curr

weighted_list = {}

def score(dir,filename,weight):
    if not os.path.isfile(dir+'/sorted_'+filename):
        print dir+'/'+filename+" has not been sorted.  Run python sort_all_csv.py"
        exit()
    weighted_list[dir+'/sorted_'+filename]=weight
    print("%s has weight %d" % (filename,weight))
    
def get_predictions(preds_per_row_id,num=3):
    best = Counter(preds_per_row_id).most_common(num)
    return ' '.join([x for x,_ in best])

files={}

def close_all_files(files):
    for filename,_ in weighted_list.items():
        files[filename].close()
    

def generate_predictions():
    out = []
    for filename,_ in weighted_list.items():
        files[filename] = open(filename,"r")
        files[filename].readline()  # skip first line
    for row_id in range(num_row_ids):
        if row_id > 0 and row_id % 100000 == 0:
            print "Completed",row_id,"rows in",time_passed()
        preds_per_row_id = {}
        for filename,weight in weighted_list.items():
           line = files[filename].readline().strip()
           line_parts = line.split(",")
           if line_parts[0] != str(row_id):
               print "Unexpected rowid found in " + filename + " where expected row_id=" + str(row_id) + ", found row_id: " + line_parts[0]
               close_all_files(files)
               exit()
           preds = line_parts[1].split(" ")
           update_tally(preds,preds_per_row_id,weight)
        out.append(get_predictions(preds_per_row_id))
    close_all_files(files)
    df = pd.DataFrame()
    df['place_id'] = pd.Series(out)
    df.index.rename('row_id',inplace=True)
    df.to_csv("ensembled_submission.csv")

score("models","tom_model.csv",46)
score("models","markus_best_model.csv",44)
score("models","markus_quick_model.csv",14)
score("models","qingchen_alternative_model.csv",7)
score("models","xgb_feature_set1.csv",10)
score("models","random_forest_entropy_feature_set2.csv",3)
score("models","xgb_feature_set2.csv",12)
        
generate_predictions()

print("Time elapsed:  %s"  % time_passed())
