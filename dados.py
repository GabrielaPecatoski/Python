import pandas as pd
import numpy as np
import random
from faker import Faker
import datetime

def generate_sales_data(num_records):
    fake = Faker()
    np.random.seed(0)
    
    product_ids = []
    sale_values = []
    quantities = []
    sale_dates = []
    
    for _ in range(num_records):
        product_ids.append(fake.random_int(min=1000, max=9999))
        sale_values.append(round(random.uniform(10, 1000), 2))
        quantities.append(random.randint(1, 10))
        sale_dates.append(fake.date_time_between(start_date='-1y', end_date='now'))
        
    sales_data = pd.DataFrame({
        'Product_ID': product_ids,
        'Sale_Value': sale_values,
        'Quantity': quantities,
        'Sale_Date': sale_dates
    })
    
    return sales_data

sales_data = generate_sales_data(100)
sales_data.to_csv('sales_data.csv', index=False)
print(sales_data.head())
