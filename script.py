import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Reproducible synthetic data generation
np.random.seed(42)
n = 500
start_date = datetime(2024,1,1)
dates = [start_date + timedelta(days=int(x)) for x in np.random.randint(0,365,n)]
data = pd.DataFrame({
    "TransactionID": range(1, n+1),
    "CustomerSegment": np.random.choice(['A','B','C'], n),
    "PurchaseAmount": np.round(np.random.gamma(shape=5, scale=40, size=n), 2),
    "TransactionDate": pd.to_datetime(dates)
})

# Inspect
print(data.info())
print(data.head())

# Compute segmented descriptive statistics
stats = data.groupby("CustomerSegment")["PurchaseAmount"].agg(["mean","median","std"]).round(2)
print("Segmented stats (mean, median, std):")
print(stats)

# Save outputs to working directory
data.to_csv("data.csv", index=False)
stats.to_csv("stats_output.txt", sep="\t")
with open("results.txt","w") as f:
    f.write("Segment\tMean\tMedian\tStd\n")
    for seg, row in stats.iterrows():
        f.write(f"{seg}\t{row['mean']}\t{row['median']}\t{row['std']}\n")

# Visualizations
plt.hist(data["PurchaseAmount"])
plt.title("Histogram of Purchase Amount")
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.clf()

stats.plot(kind="bar")
plt.title("Purchase Amount Stats by Segment (Mean, Median, Std)")
plt.xlabel("Customer Segment")
plt.ylabel("Value")
plt.savefig("bar_chart.png")
plt.clf()
