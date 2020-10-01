#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:52:27 2020

@author: kduarte
"""

import pandas as pd
import numpy as np

fileID = open('../whichFiles.txt','r');
dirinfo = fileID.read().split('\n')

df = pd.read_csv('../List_New_Latest_Exam_1411_12_03_2019_entire.csv')

df_new = df[['Subject','Age','Group','Sex']]
df_new = df_new.drop_duplicates()   


df_new = df_new[df_new['Subject'].str.contains('|'.join(dirinfo))]

print(df_new['Group'].value_counts())

df_cn    = df_new[df_new['Group']=='CN'  ]
df_emci  = df_new[df_new['Group']=='EMCI']
df_mci   = df_new[df_new['Group']=='MCI' ]
df_lmci  = df_new[df_new['Group']=='LMCI']
df_ad    = df_new[df_new['Group']=='AD'  ]


df_cn    = df_cn.sample  (n=100,random_state=5071993)
df_emci  = df_emci.sample(n=100,random_state=5071993)
df_mci   = df_mci.sample (n=100,random_state=5071993)
df_lmci  = df_lmci.sample(n=100,random_state=5071993)
df_ad    = df_ad.sample  (n=100,random_state=5071993)

df_final = pd.concat([df_cn,df_emci,df_mci,df_lmci,df_ad])
vec_subjects = df_final['Subject']
vec_subjects.to_csv('../final_test_100_patients_per_class.txt',sep='\n',index=False)