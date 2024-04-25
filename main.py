#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
#%%
# Load the data
loan = pd.read_csv("./Data/Loan_Default.csv")
print(loan.columns)
#print(loan.head())
print(loan.describe())
#%%
#print(loan["Status"].value_counts())
# Drop the missing values
#loan = loan.dropna()
#print(loan.isnull().sum())
# %%
sns.countplot(x="Gender", data=loan, hue="Status",palette="YlGnBu")
# %%
g=sns.FacetGrid(loan, col="age",palette="YlGnBu")
g.map(sns.histplot, x="loan_amount", data=loan, alpha=.7, bins=30)
#%%
g=sns.FacetGrid(loan, col="Status",palette="YlGnBu")
g.map(sns.histplot, x="income", data=loan, alpha=.7, bins=30)
#%%
sns.boxplot(x="Status", y="income", data=loan,palette="YlGnBu")