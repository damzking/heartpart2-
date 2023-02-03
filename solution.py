# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
# load data
heart = pd.read_csv('heart_disease.csv')
print(heart.head())

thalach_hd = heart.thalach[heart.heart_disease=='presence']
thalach_no_hd = heart.thalach[heart.heart_disease=='absence']
diff_mean = np.mean(thalach_hd)-np.mean(thalach_no_hd)
print(diff_mean)
tstat, pval = ttest_ind(thalach_hd, thalach_no_hd)
print(pval)
age_hd = heart.age[heart.heart_disease=='presence']
age_no_hd = heart.age[heart.heart_disease=='absence']


 
# second box plot:



sns.boxplot(x=heart.heart_disease, y=heart.trestbps)
plt.show()


thalach_typical = heart.thalach[heart.cp== 'typical angina']
thalach_atypical = heart.thalach[heart.cp== 'atypical angina']
thalach_nonanginalpain = heart.thalach[heart.cp== 'non-anginal pain']
thalach_asymptomatic = heart.thalach[heart.cp== 'asymptomatic']

Fstat,pval = f_oneway(thalach_typical,thalach_nonanginalpain,thalach_atypical,thalach_asymptomatic)
print(pval)

table = pd.crosstab(heart.cp,heart.heart_disease)

print(table)

chi2,pval,dof,exp = chi2_contingency(table)
print(pval)