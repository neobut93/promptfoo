import json
from collections import defaultdict

# Load results file
path = "results.json"  # update if needed
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

results = data.get("results", {}).get("results", [])

# Aggregate per provider
cost_sum = defaultdict(float)
count_sum = defaultdict(int)

for r in results:
    provider = (r.get("provider") or {}).get("id") or "unknown-provider"
    cost = float(r.get("cost") or 0.0)
    cost_sum[provider] += cost
    count_sum[provider] += 1

# Compute averages and projections
rows = []
for provider in sorted(cost_sum.keys()):
    total_cost = cost_sum[provider]
    runs = count_sum[provider]
    avg = total_cost / runs if runs else 0
    cost_100k = avg * 100_000
    cost_year = cost_100k * 365  # assuming 100k/day
    rows.append((provider, avg, cost_100k, cost_year))

# Dynamic column widths
name_w = max(len("Model Name"), max(len(r[0]) for r in rows))
col1_w = len("Avg cost per 1 iteration")
col2_w = len("Cost per 100000 iterations")
col3_w = len("Cost per 1 year")

# Helper to format with $ tight next to number and consistent width
def fmt_money(value, width):
    s = f"${value:,.6f}" if value < 1 else f"${value:,.2f}"
    return s.rjust(width + 1)  # +1 for the $ already in string

# Print header
header = (
    f"| {'Model Name'.ljust(name_w)} "
    f"| {'Avg cost per 1 iteration'.rjust(col1_w)} "
    f"| {'Cost per 100000 iterations'.rjust(col2_w)} "
    f"| {'Cost per 1 year'.rjust(col3_w)} |"
)
print(header)
print("|" + "-" * (len(header) - 2) + "|")

# Print rows
for provider, avg, c100k, cyear in rows:
    print(
        f"| {provider.ljust(name_w)} "
        f"| {fmt_money(avg, col1_w)} "
        f"| {fmt_money(c100k, col2_w)} "
        f"| {fmt_money(cyear, col3_w)} |"
    )
