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

#%%
#PC Portable
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

print(sns.get_dataset_names())

tips = sns.load_dataset('tips')
titanic = sns.load_dataset('titanic')
diamonds = sns.load_dataset('diamonds')

#%%
sns.scatterplot(x='total_bill', y='tip', data=tips, hue="day", size="size", palette="YlGnBu")
# %%
sns.histplot(tips['total_bill'], kde=True, bins=30)
# %%
sns.barplot(x="sex",y="tip",data=tips,hue="sex")
# %%
sns.boxplot(x="day",y="total_bill",data=tips,hue="sex",palette="YlGnBu")
# %%
sns.stripplot(x="day",y="tip",data=tips,hue="sex", dodge=True, palette="YlGnBu")
# %%
sns.jointplot(x="total_bill",y="tip",data=tips, kind="reg")
# %%
sns.jointplot(x="total_bill",y="tip",data=tips, kind="kde",fill=True,cmap="YlGnBu")
# %%
sns.jointplot(x="total_bill",y="tip",data=tips, kind="hex",cmap="YlGnBu")
# %%
sns.pairplot(titanic.select_dtypes(["number"]),hue="pclass")
# %%
