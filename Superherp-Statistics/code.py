# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)

gender_count=data['Gender'].value_counts()
plt.bar(gender_count.index,gender_count)


#path of the data file- path



#Code starts here 




# --------------
#Code starts here


alignment=data['Alignment'].value_counts()
plt.pie(alignment)
plt.xlabel('Character Alignment')


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]
sc_covariance=sc_df.cov().iloc[0,1]
sc_strength=data['Strength'].std()
sc_combat=data['Combat'].std()

sc_pearson=sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)


ic_df=data[['Intelligence','Combat']]
ic_covariance=ic_df.cov().iloc[0,1]
ic_intelligence=data['Intelligence'].std()
ic_combat=data['Combat'].std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


# --------------
#Code starts here

total_high=data['Total'].quantile(q=0.99)
#print(data.columns)

super_best=data[data['Total']>total_high]
#print(super_best)

super_best_names=super_best.Name.tolist()
print(super_best_names)


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(20,10))
data['Intelligence'].plot(kind='box',stacked=False,ax=ax_1)
data['Speed'].plot(kind='box',stacked=False,ax=ax_2)
data['Power'].plot(kind='box',stacked=False,ax=ax_3)


