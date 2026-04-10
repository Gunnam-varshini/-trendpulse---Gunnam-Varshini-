import pandas as pd



# 1 — Load the JSON file

file_path = "data/trends_20240115.json"



df = pd.read_json(file_path)



print(f"Loaded {len(df)} stories from {file_path}")



# 2 — Clean the Data



# Remove duplicates based on post_id

df = df.drop_duplicates(subset="post_id")

print(f"After removing duplicates: {len(df)}")



# Drop rows with missing important values

df = df.dropna(subset=["post_id", "title", "score"])

print(f"After removing nulls: {len(df)}")



# Convert data types

df["score"] = df["score"].astype(int)

df["num_comments"] = df["num_comments"].astype(int)



# Remove low quality (score < 5)

df = df[df["score"] >= 5]

print(f"After removing low scores: {len(df)}")



# Strip whitespace from title

df["title"] = df["title"].str.strip()



# 3 — Save as CSV

output_path = "data/trends_clean.csv"

df.to_csv(output_path, index=False)



print(f"Saved {len(df)} rows to {output_path}")



# Print summary: stories per category

print("\nStories per category:")

category_counts = df["category"].value_counts()



for category, count in category_counts.items():

  print(f"{category} {count}")