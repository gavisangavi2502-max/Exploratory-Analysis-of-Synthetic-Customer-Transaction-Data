# Exploratory Analysis of Synthetic Customer Transaction Data

Contents:
- script.py : Reproducible script to generate dataset, compute segmented stats and save visualizations.
- data.csv : Generated synthetic dataset (500 records).
- stats_output.txt : Tab-separated mean/median/std by CustomerSegment.
- results.txt : Human-readable results table.
- summary.txt : 250-word interpretative summary.
- histogram.png, bar_chart.png : Visualizations.

Run instructions:
1. Ensure Python 3.x with pandas, numpy, matplotlib installed.
2. Run: `python script.py`
3. Files will be written to the current working directory.

Notes:
- The PurchaseAmount distribution uses a Gamma distribution to better mimic right-skewed transaction amounts.
- The script uses a fixed random seed (42) for reproducibility.
