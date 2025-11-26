import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Generate dataset
np.random.seed(42)
n = 500
data = pd.DataFrame({
    "TransactionID": range(1, n+1),
    "CustomerSegment": np.random.choice(['A','B','C'], n),
    "PurchaseAmount": np.random.normal(200, 50, n).round(2),
    "TransactionDate": [
        (datetime.now() - timedelta(days=np.random.randint(0, 365))).strftime("%Y-%m-%d")
        for _ in range(n)
    ]
})

# Display first rows
print(data.head())

# Descriptive stats
stats = data.groupby("CustomerSegment")["PurchaseAmount"].describe()
print(stats)

# Visualizations
plt.hist(data["PurchaseAmount"])
plt.title("Distribution of Purchase Amounts")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show()

avg = data.groupby("CustomerSegment")["PurchaseAmount"].mean()
avg.plot(kind='bar')
plt.title("Average Purchase Amount by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Average Amount")
plt.show()
