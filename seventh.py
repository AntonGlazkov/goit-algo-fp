import random

N = 1_000_00  

analytic_counts = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
analytic_probs = {s: analytic_counts[s] / 36 for s in range(2, 13)}

counts = [0] * 13
for _ in range(N):
    s = random.randint(1, 6) + random.randint(1, 6)
    counts[s] += 1

mc_probs = {s: counts[s] / N for s in range(2, 13)}

# Таблиця порівняння 
header = f"{'Сума':>4} | {'MC ймов.':>10} | {'Аналіт.':>10} | {'Різниця':>10}"
print(header)
print("-" * len(header))

rows = []
max_abs_diff = 0.0

for s in range(2, 13):
    diff = mc_probs[s] - analytic_probs[s]
    abs_diff = abs(diff)
    if abs_diff > max_abs_diff:
        max_abs_diff = abs_diff

    row = (
        f"{s:>4} | "
        f"{mc_probs[s]*100:>9.4f}% | "
        f"{analytic_probs[s]*100:>9.4f}% | "
        f"{diff*100:>+9.4f}%"
    )
    print(row)
    rows.append(row)