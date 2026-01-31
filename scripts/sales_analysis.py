import pandas as pd

# Load datasets
customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")

# Merge data
orders_items = orders.merge(order_items, on="order_id")
full_data = orders_items.merge(customers, on="customer_id")
full_data = full_data.merge(products, on="product_id")

# Calculate revenue
full_data["revenue"] = full_data["price"] * full_data["quantity"]

# Total revenue
print("Total Revenue:", full_data["revenue"].sum())

# Revenue by customer
print("\nRevenue by Customer:")
print(
    full_data.groupby("customer_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Top selling products
print("\nTop Selling Products:")
print(
    full_data.groupby("product_name")["quantity"]
    .sum()
    .sort_values(ascending=False)
)
