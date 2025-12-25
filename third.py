import heapq

def dijkstra(graph, start):
    distances = {v: float("inf") for v in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_dist, current_v = heapq.heappop(heap)

        if current_dist > distances[current_v]:
            continue

        for neighbor, weight in graph[current_v]:
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances


def main():
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2), ("F", 6)],
        "E": [("C", 10), ("D", 2), ("F", 3)],
        "F": [("D", 6), ("E", 3)],
    }

    start = "A"
    distances = dijkstra(graph, start)

    print(f"Початкова вершина: {start}")
    for v in sorted(distances):
        print(f"Найкоротша відстань до {v}: {distances[v]}")


if __name__ == "__main__":
    main()
