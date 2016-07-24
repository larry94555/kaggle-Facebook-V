# kaggle-Facebook-V
Scripts for Kaggle Facebook V Challenge

This repository includes the scripts needed to ensemble the winning csv file from Tom Van de Wiele, the cvs fies from Markus Kleigl, and others into a score of 0.62865.

Instructions:

1.  clone this repository.
2.  Run `python uncompress_all_models.py` to generate a directory models of uncompressed csv files.
3.  Run `python sort_all_csv.py` to created sorted files which are needed by the ensemble script.
4.  Run `python ensemble.py` to generate the submission file which will be called `ensembled_submission.csv`

When you submit this file, the reported result will be 0.62865.  The weights used are:

[tom's model][ttvand]:  46  

[markus's best model][markus]:  44

[markus's quick model][markus] (the first model "Version 1"):  14

[Qingchen's alternative model][qingchen] (using week number): 7

[xgb feature set 1][larry]:  10

[random forest entropy feature set 2][larry]:  3

[xgb feature set 2][larry]:  12 

[ttvand]:https://github.com/ttvand/Facebook-V
[markus]:https://github.com/mkliegl/kaggle-Facebook-V
[qingcheck]:https://www.kaggle.com/c/facebook-v-predicting-check-ins/forums/t/22123/6th-place-kernel-density-estimation/126440#post126440
[larry]:https://www.kaggle.com/c/facebook-v-predicting-check-ins/forums/t/22086/solution-sharing-i-got-to-23-with-xgb-rf-knn/126278#post126278
