import pandas as pd
# import matplotlib.pyplot as plt
laptop_data = pd.read_csv('laptop_data.csv')
#laptop_data.to_csv('laptop_data.csv', index=False)
print(laptop_data['Brand'].unique())
print(laptop_data.loc[laptop_data['Brand']=='APPLE'])
print(laptop_data.loc[laptop_data['Brand']=='ACER'])
print(laptop_data.loc[laptop_data['Brand']=='DELL'])
print(laptop_data.loc[laptop_data['Brand']=='LENOVO'])
print(laptop_data.loc[laptop_data['Brand']=='LG'])
print(laptop_data.loc[laptop_data['Brand']=='MICROSOFT'])



# #TODO - make separate tables for each brand
# #TODO - make histograms for each brand
