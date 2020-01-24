# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=path
df=pd.read_csv(df)

p_a=df[df['fico'].astype(float)>700].shape[0]/df.shape[0]
print(p_a)

p_b=df[df['purpose']=='debt_consolidation'].shape[0]/df.shape[0]
#p_b=df[df['purpose']=='debt_consolation'].shape[0]/df.shape[0]
print(p_b)
df1=df[df['purpose']=='debt_consolidation']


test=df[df['fico']>700]
#print(len(test[test['purpose']=='debt_consolidation']))
p_a_b=test[test['purpose']=='debt_consolidation'].shape[0]/df[df['fico'].astype(float)>700].shape[0]


result=(df1[df1['fico'].astype(float)>700].shape[0]/df1.shape[0])==p_a
print(result)
# code ends here


# --------------
# code starts here





prob_lp=df[df['paid.back.loan'] =='Yes'].shape[0]/df['paid.back.loan'].shape[0]
print(prob_lp)

prob_cs=df[df['credit.policy'] =='Yes'].shape[0]/df['credit.policy'].shape[0]
print(prob_cs)

new_df=df[df['paid.back.loan'] =='Yes']
print(new_df)

prob_pd_cs=new_df[new_df['credit.policy'] =='Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)


bayes=prob_pd_cs*prob_lp/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
df1=df[df['paid.back.loan'] == 'No']



# code ends here


# --------------
# code starts here

inst_median=df['installment'].median()
print(inst_median)


inst_mean=df['installment'].mean()
print(inst_mean)
df['installment'].hist(normed=True,bins=50)
# code ends here


