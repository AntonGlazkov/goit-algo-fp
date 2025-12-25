items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True,
    )

    chosen = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return chosen, total_cost, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if cost <= b:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - cost] + calories)

    chosen = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = names[i - 1]
            chosen.append(name)
            b -= items[name]["cost"]

    total_cost = sum(items[name]["cost"] for name in chosen)
    total_calories = sum(items[name]["calories"] for name in chosen)

    return chosen, total_cost, total_calories


def main():
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy:", greedy_result)
    print("DP:", dp_result)


if __name__ == "__main__":
    main()
