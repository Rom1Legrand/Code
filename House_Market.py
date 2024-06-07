#1 Import a library
import pandas as pd

#2 import dataset + creat df
df_house_price = pd.read_csv("house_price.csv")
df_nb_chambres = pd.read_csv("nombre_de_chambres.csv")
df_nb_sdb = pd.read_csv("nombre_de_sdb.csv")
df_superficie = pd.read_csv("superficie.csv")

print(df_house_price.head())
print (df_nb_chambres.head())
print (df_nb_sdb.head())
print (df_superficie.head())


#3 Give a column name to the three datasets that don't have a header in the source file
df_nb_chambres.columns = ["id", "chambres"]
df_nb_sdb.columns = ["id", "sdb"]
df_superficie.columns = ["id", "surface"]

#4 Make an inner join of these four datasets into a single dataframe
df_temp = df_house_price.merge(df_nb_sdb, on="id", how="inner")
df_temp = df_temp.merge(df_nb_chambres, on="id", how="inner")
df_final = df_temp.merge(df_superficie, on="id", how="inner")
print(df_final)

#5 What is the average surface area of the houses in our dataset?
print(df_final["surface"].mean())

#6 What is the median and average number of rooms?
print("The average number of room is {}, and the median number is {}".format(df_final["chambres"].median(), df_final["chambres"].mean()))

#7 What is the average cost of a house?
print(df_final["house_price"].mean())

#8 What is the average cost of a house, depending on the number of rooms it has? print(df_final.groupby(["chambres","house_price"].mean())
print(df_final.groupby("chambres")["house_price"].mean())

#9 The average cost per room doesn't tell us much. Let's try to categorize by size.
# "very large" = "a house larger than 25,000 sqrt_feet"
# "large" = "a house between 20,000 and 25,000 sqrt_feet"
#"medium" = "a house between 15,000 and 20,000 sqrt_feet"
#"small"= "a house between 10,000 and 15,000 sqrt_feet"
# "very small"  = a house less than 10,000 sqrt_feet"

df_final["taille"]= df_final["surface"].apply(lambda x : "very_large" if x > 25000 
                                   else "large" if (x > 20000) and (x <= 25000) 
                                   else "medium" if (x > 15000) and (x <= 20000) 
                                   else "small" if (x > 10000) and  (x <= 15000) 
                                   else "very_small")
print(df_final)

#10 What is the average cost of a house depending on its size category?
print(df_final.groupby("taille")["house_price"].mean())

#11 Apply the code below to view your result. What can you conclude?
import plotly.express as px
fig = px.scatter(df_final, x = "surface", y = "house_price", trendline = "ols")
fig.show()




