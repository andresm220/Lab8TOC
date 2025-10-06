#!/usr/bin/env python3
"""
Exercise 4 — Linear Search best/avg/worst demonstration.
We count comparisons in three situations and also do a simple timing profile.
"""

import random
import time
import csv
import matplotlib.pyplot as plt


def linear_search(arr, target):
    """Returns (index_or_-1, comparisons)."""
    comps = 0
    for i, x in enumerate(arr):
        comps += 1
        if x == target:
            return i, comps
    return -1, comps


def demo_counts(n: int):
    arr = list(range(n))
    # Best case: target is first
    _, best = linear_search(arr, 0)
    # Worst case: target absent
    _, worst = linear_search(arr, n)  # not in array
    # Average case: sample random positions and average
    TRIALS = min(200, max(10, n))
    total = 0
    for _ in range(TRIALS):
        t = random.randint(0, n)  # sometimes absent (n), sometimes present
        _, c = linear_search(arr, t)
        total += c
    avg = total / TRIALS
    return best, avg, worst


def profile_timing(candidate_ns):
    results = []
    for n in candidate_ns:
        arr = list(range(n))
        start = time.perf_counter()
        linear_search(arr, n)  # worst-case (absent)
        elapsed = time.perf_counter() - start
        results.append((n, elapsed))
        print(f"[OK] n={n} worst-case time={elapsed:.6f}s")
    return results


def save_csv_plot(results, csv_path="ex4_results.csv", png_path="ex4_plot.png"):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n", "worst_case_seconds"])
        for n, sec in results:
            w.writerow([n, f"{sec:.6f}"])

    xs = [n for n, _ in results]
    ys = [sec for _, sec in results]
    plt.figure()
    plt.plot(xs, ys, marker="o")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (s) — peor caso (ausente)")
    plt.title("Ejercicio 4 — Búsqueda Lineal")
    plt.grid(True)
    plt.savefig(png_path, dpi=150, bbox_inches="tight")
    print(f"[SAVE] Plot -> {png_path}")


def main():
    # Comparaciones representativas
    for n in [10, 100, 1000]:
        best, avg, worst = demo_counts(n)
        print(f"n={n} -> comps: best={best}, avg≈{avg:.2f}, worst={worst}")

    # Timing (peor caso)
    candidate_ns = [1, 10, 100, 1000, 10_000, 100_000, 1_000_000]
    results = profile_timing(candidate_ns)
    save_csv_plot(results)


if __name__ == "__main__":
    main()
