# Task 3 — Analysis with Pandas & NumPy



import pandas as pd

import numpy as np



# -----------------------------

# 1. Load and Explore Data

# -----------------------------

df = pd.read_csv("data/trends_clean.csv")



print("Loaded data:", df.shape)



print("\nFirst 5 rows:")

print(df.head())



# Average values using Pandas

avg_score = df["score"].mean()

avg_comments = df["num_comments"].mean()



print("\nAverage score:", int(avg_score))

print("Average comments:", int(avg_comments))





# -----------------------------

# 2. NumPy Analysis

# -----------------------------

scores = df["score"].values



print("\n--- NumPy Stats ---")

print("Mean score:", int(np.mean(scores)))

print("Median score:", int(np.median(scores)))

print("Std deviation:", int(np.std(scores)))

print("Max score:", int(np.max(scores)))

print("Min score:", int(np.min(scores)))





# Category with most stories

category_counts = df["category"].value_counts()

top_category = category_counts.idxmax()

top_count = category_counts.max()



print(f"\nMost stories in: {top_category} ({top_count} stories)")





# Most commented story

max_comments_row = df.loc[df["num_comments"].idxmax()]



print(

  f'\nMost commented story: "{max_comments_row["title"]}" - {max_comments_row["num_comments"]} comments'

)





# -----------------------------

# 3. Add New Columns

# -----------------------------



# Engagement column

df["engagement"] = df["num_comments"] / (df["score"] + 1)



# is_popular column

df["is_popular"] = df["score"] > avg_score





# -----------------------------

# 4. Save Result

# -----------------------------

df.to_csv("data/trends_analysed.csv", index=False)



print("\nSaved to data/trends_analysed.csv")