#1 Import a library that allows to read data from a csv file
import pandas as pd

#2 Import the dataset
df = pd.read_csv("chipotle.csv")

#3 Look at the 10 first rows in the dataset
print(df.head(10))

#4 What is the shape of the dataset ?
print(df.shape)

#5 Display all the columns of our dataset
print(df.columns)

#6 How many items were ordered from Chipotle in total?
total_items_ordered = df["quantity"].sum()
print(total_items_ordered)

#7 What is the most ordered item? (.groupby() + .sort_value())
most_ordered_item = df.groupby("item_name")["quantity"].sum().sort_values(ascending=False)
print(most_ordered_item)

#8 How much revenue has Chipotle made?
df["item_price"] = df["item_price"].str.replace("$", "").astype("float")
revenu_total = (df["quantity"]*df["item_price"]).sum()
print(revenu_total)

#9 What is the average revenue per order?
avg_revenu_by_order = revenu_total / len(df["order_id"].unique())
print(avg_revenu_by_order)