import pandas as pd
import glob
import os

# get all csv files from the data folder
files = glob.glob("data/*.csv")

dfs = []

for file in files:
    df = pd.read_csv(file)

    # keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # clean price column in case it has $ signs
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)

    # make sales column
    df["sales"] = df["quantity"] * df["price"]

    # keep only required columns
    df = df[["sales", "date", "region"]]

    dfs.append(df)

# combine all files
final_df = pd.concat(dfs, ignore_index=True)

# save output
final_df.to_csv("formatted_output.csv", index=False)

print("Done! formatted_output.csv created.")