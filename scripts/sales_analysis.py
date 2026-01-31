import pandas as pd

# -----------------------------
# Load datasets
# -----------------------------
customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")

# -----------------------------
# Merge datasets
# -----------------------------
orders_items = orders.merge(order_items, on="order_id", how="inner")
orders_items_customers = orders_items.merge(customers, on="customer_id", how="inner")
full_data = orders_items_customers.merge(products, on="product_id", how="inner")

# -----------------------------
# Revenue calculation
# -----------------------------
full_data["revenue"] = full_data["price"] * full_data["quantity"]

# -----------------------------
# Total revenue
# -----------------------------
total_revenue = full_data["revenue"].sum()
print("Total Revenue:", total_revenue)

# -----------------------------
# Revenue by customer
# -----------------------------
revenue_by_customer = (
    full_data.groupby("customer_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Customer:")
print(revenue_by_customer)

# -----------------------------
# Top selling products
# -----------------------------
top_products = (
    full_data.groupby("product_name")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Selling Products:")
print(top_products)

# -----------------------------
# Save outputs to files
# -----------------------------
full_data.to_csv("outputs/full_sales_data.csv", index=False)
revenue_by_customer.to_csv("outputs/revenue_by_customer.csv")
top_products.to_csv("outputs/top_products.csv")

print("\nAnalysis completed successfully.")
print("Output files saved in the 'outputs' folder.")

