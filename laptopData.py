import pandas as pd
# import matplotlib.pyplot as plt
laptop_data = pd.read_csv('laptop_data.csv')
#laptop_data.to_csv('laptop_data.csv', index=False)
apple_data = laptop_data.loc[laptop_data['Brand'] == 'APPLE']

print(apple_data.at[0, 'Price'])
print(apple_data)


# #TODO - make separate tables for each brand
# #TODO - make histograms for each brand
