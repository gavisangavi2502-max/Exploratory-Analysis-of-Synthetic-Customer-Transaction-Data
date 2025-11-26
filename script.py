import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

np.random.seed(42)
n = 500
start_date = datetime(2024,1,1)

data = pd.DataFrame({
    "TransactionID": range(1, n+1),
    "CustomerSegment": np.random.choice(['A','B','C'], n),
    "PurchaseAmount": np.round(np.random.gamma(shape=5, scale=40, size=n), 2),
    "TransactionDate": [start_date + timedelta(days=int(x)) for x in np.random.randint(0,365,n)]
})

print(data.info())
print(data.head())

stats = data.groupby("CustomerSegment")["PurchaseAmount"].agg(["mean","median","std"])
print(stats)

plt.hist(data["PurchaseAmount"])
plt.title("Histogram of Purchase Amount")
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")
plt.savefig("hist.png")
plt.clf()

stats.plot(kind="bar")
plt.title("Purchase Amount Stats by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Values")
plt.savefig("bar.png")
plt.clf()
