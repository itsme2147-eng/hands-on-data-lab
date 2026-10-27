"""Generate three related, intentionally messy retail tables (synthetic data).

customers.csv, products.csv, orders.csv  - linked by customer_id / product_id,
which lets the lab practise merging as well as cleaning.
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SEED = 7


def generate(seed: int = SEED):
    rng = np.random.default_rng(seed)

    # ---------------- customers ----------------
    n_c = 400
    customers = pd.DataFrame({
        "customer_id": [f"CU{i:04d}" for i in range(1, n_c + 1)],
        "city": rng.choice(["Pune", "Mumbai", "Bengaluru", "Delhi", "Chennai", "Hyderabad"], n_c),
        "segment": rng.choice(["Consumer", "Corporate", "Home Office"], n_c, p=[.55, .3, .15]),
        "age": rng.normal(35, 10, n_c).round().clip(18, 75),
        "signup_date": (pd.Timestamp("2022-01-01") + pd.to_timedelta(rng.integers(0, 1000, n_c), unit="D")).strftime("%Y-%m-%d"),
    })
    customers.loc[rng.choice(n_c, 25, replace=False), "age"] = np.nan
    customers.loc[rng.choice(n_c, 3, replace=False), "age"] = -1          # invalid
    i = rng.choice(n_c, 20, replace=False); customers.loc[i, "city"] = customers.loc[i, "city"].str.upper()
    i = rng.choice(n_c, 15, replace=False); customers.loc[i, "city"] = " " + customers.loc[i, "city"] + " "
    customers.loc[rng.choice(n_c, 10, replace=False), "segment"] = None

    # ---------------- products ----------------
    cats = {"Electronics": (2500, 45000), "Furniture": (1500, 25000), "Office Supplies": (50, 1200),
            "Clothing": (400, 4000), "Books": (150, 900)}
    rows = []
    for cat, (lo, hi) in cats.items():
        for k in range(1, 9):
            price = round(float(rng.uniform(lo, hi)), 0)
            rows.append((f"P{len(rows) + 1:03d}", cat, f"{cat.split()[0]} item {k}", price, round(price * rng.uniform(.55, .85), 0)))
    products = pd.DataFrame(rows, columns=["product_id", "category", "product_name", "unit_price", "unit_cost"])
    products["unit_price"] = products["unit_price"].astype(object)
    for j in rng.choice(len(products), 5, replace=False):
        products.at[j, "unit_price"] = f"Rs {products.at[j, 'unit_price']:,.0f}"   # wrong dtype (text)

    # ---------------- orders ----------------
    n_o = 5000
    dates = pd.Timestamp("2024-01-01") + pd.to_timedelta(rng.integers(0, 730, n_o), unit="D")
    # seasonality: keep more orders in Oct-Dec by re-sampling some dates
    boost = rng.random(n_o) < .18
    dates = pd.Series(dates)
    dates[boost] = pd.to_datetime(rng.choice(["2024", "2025"], boost.sum())) + pd.to_timedelta(rng.integers(273, 365, boost.sum()), unit="D")
    orders = pd.DataFrame({
        "order_id": [f"ORD{i:05d}" for i in range(1, n_o + 1)],
        "order_date": dates.dt.strftime("%Y-%m-%d"),
        "customer_id": rng.choice(customers["customer_id"], n_o),
        "product_id": rng.choice(products["product_id"], n_o),
        "quantity": rng.integers(1, 6, n_o).astype(float),
        "discount": rng.choice([0, 0, 0, .05, .10, .15, .20], n_o),
        "payment_method": rng.choice(["Credit Card", "UPI", "Debit Card", "Cash on Delivery"], n_o, p=[.3, .4, .2, .1]),
        "status": rng.choice(["Delivered", "Returned", "Cancelled"], n_o, p=[.88, .08, .04]),
    })
    orders.loc[rng.choice(n_o, 80, replace=False), "quantity"] = np.nan
    orders.loc[rng.choice(n_o, 6, replace=False), "quantity"] = -2            # invalid
    i = rng.choice(n_o, 150, replace=False)
    orders["discount"] = orders["discount"].astype(object)
    orders.loc[i, "discount"] = [f"{int(float(d) * 100)}%" for d in orders.loc[i, "discount"]]   # '10%' strings
    i = rng.choice(n_o, 120, replace=False); orders.loc[i, "order_date"] = pd.to_datetime(orders.loc[i, "order_date"]).dt.strftime("%d/%m/%Y")
    i = rng.choice(n_o, 100, replace=False); orders.loc[i, "payment_method"] = orders.loc[i, "payment_method"].str.lower()
    orders.loc[rng.choice(n_o, 40, replace=False), "payment_method"] = None
    orders = pd.concat([orders, orders.sample(60, random_state=seed)], ignore_index=True)           # duplicates
    return customers, products, orders


if __name__ == "__main__":
    for name, df in zip(["customers", "products", "orders"], generate()):
        df.to_csv(ROOT / "data" / f"{name}.csv", index=False)
        print(name, df.shape)
