# generate_data.py

import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# --- Configuration ---
NUM_RECORDS = 5000
START_DATE = datetime(2021, 1, 1)
END_DATE = datetime(2023, 12, 31)

# --- Master Data ---
products = {
    'Electronics': {
        'Laptop': 1200, 'Smartphone': 800, 'Tablet': 450, 'Headphones': 150, 'Monitor': 300
    },
    'Furniture': {
        'Chair': 250, 'Desk': 400, 'Sofa': 700, 'Bookshelf': 180
    },
    'Office Supplies': {
        'Pens': 5, 'Notebook': 10, 'Stapler': 15, 'Printer Ink': 45
    },
    'Clothing': {
        'T-Shirt': 25, 'Jeans': 75, 'Jacket': 120, 'Shoes': 90
    }
}

regions = ['North', 'South', 'East', 'West']
shipping_types = ['Standard', 'Express', 'Next-Day']
customer_segments = ['Consumer', 'Corporate', 'Home Office']

# --- Data Generation ---
data = []
order_id_counter = 10000

for _ in range(NUM_RECORDS):
    # Order Info
    order_date = fake.date_time_between(start_date=START_DATE, end_date=END_DATE)
    order_id = f"ORD-{order_id_counter}"
    
    # Product Info
    category = random.choice(list(products.keys()))
    product_name = random.choice(list(products[category].keys()))
    base_price = products[category][product_name]
    
    # Sales Info
    quantity = random.randint(1, 5)
    discount = random.choice([0, 0.05, 0.1, 0.15, 0.2])
    
    sales = base_price * quantity
    total_sale = sales * (1 - discount)
    
    # Profit Calculation (assuming a random profit margin between 5% and 30%)
    profit_margin = random.uniform(0.05, 0.30)
    profit = total_sale * profit_margin
    
    # Customer and Location
    customer_name = fake.name()
    segment = random.choice(customer_segments)
    city = fake.city()
    state = fake.state_abbr()
    region = random.choice(regions)
    
    # Shipping
    ship_mode = random.choice(shipping_types)
    ship_date = order_date + timedelta(days=random.randint(1, 10))

    data.append([
        order_id, order_date, ship_date, ship_mode, customer_name, segment,
        city, state, region, category, product_name, total_sale, quantity,
        discount, profit
    ])
    
    order_id_counter += 1

# --- Create DataFrame ---
columns = [
    'OrderID', 'OrderDate', 'ShipDate', 'ShipMode', 'CustomerName', 'Segment',
    'City', 'State', 'Region', 'Category', 'ProductName', 'Sales', 'Quantity',
    'Discount', 'Profit'
]
df = pd.DataFrame(data, columns=columns)

# --- Save to CSV ---
output_path = 'raw_sales_data.csv'
df.to_csv(output_path, index=False)

print(f"Successfully generated {NUM_RECORDS} records and saved to {output_path}")