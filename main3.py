import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')
print(df.info())

print_rows = df.head()
print(print_rows)

first_row = df.head()
print(first_row)

subset = df[['Country', 'Average IQ']]
print(subset)

filtered_df = subset[subset['Average IQ'] > 100]
print(filtered_df)