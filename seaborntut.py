import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Toyota.csv')
print(data.shape)
sns.set(style = 'darkgrid')
#sns.regplot(x=data['Age'],y=data['Price'])
# to remove regression line, to change marker:
#sns.regplot(x=data['Age'],y=data['Price'],fit_reg=False,marker='*')

# scatter plot of price vs age by fuel type 
#sns.lmplot(x='Age',y='Price',data=data,fit_reg=False,hue='FuelType',legend='True',palette='Set1')
#sns.displot(data['Age'])
#sns.countplot(x='FuelType',data=data)

# --> grouped bar plots
#sns.countplot(x='FuelType',data=data,hue = 'Automatic',legend=True)

# --> whisker and box plot
colors = ['green','blue','orange']
sns.boxplot(x=data["FuelType"],y=data['Price'],palette=colors)

plt.show()