import pandas as pd

products = ['apples', 'bananas', 'oranges', 'grapes']

sales = [345,456,567,678]

sales_series = pd.Series(sales, index=products)
print(sales_series)


print(sales_series['grapes'])

total_sales = sales_series.sum()
print(total_sales)

data = {'Name:': ['lisa', 'medina', 'medinaa'],
        'Age': [25,80,62],
        'City': ['Prishtine', 'Gillani', 'Peje']
    }

df = pd.DataFrame(data)
print(df)

#df = pd.read_csv('cs.csv')
#df.to_csv('output_database.csv', index = False)

best_selling_product = sales_series.idxmax()
print(f"Best selling product: {best_selling_product}")