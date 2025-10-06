#!/usr/bin/env python3
"""
Exercise 2 — O(n)
Implements the nested loop with a break in the inner loop and profiles runtime.
Saves CSV and PNG plot.
"""

import time
import csv
from typing import List, Tuple
import matplotlib.pyplot as plt


def function_ex2(n: int) -> int:
    """
    Equivalent:
    if (n <= 1) return;
    for (i = 1; i <= n; i++) {
      for (j = 1; j <= n; j++) { printf(...); break; }
    }
    Returns the number of prints (simulated with a counter).
    """
    if n <= 1:
        return 0
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count += 1
            break
    return count


def profile_function(candidate_ns: List[int]) -> List[Tuple[int, float, int]]:
    results = []
    for n in candidate_ns:
        start = time.perf_counter()
        cnt = function_ex2(n)
        elapsed = time.perf_counter() - start
        results.append((n, elapsed, cnt))
        print(f"[OK] n={n} time={elapsed:.6f}s prints={cnt}")
    return results


def save_csv_plot(results, csv_path="ex2_results.csv", png_path="ex2_plot.png"):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n", "seconds", "count"])
        for n, sec, cnt in results:
            w.writerow([n, f"{sec:.6f}", cnt])

    xs = [n for n, _, _ in results]
    ys = [sec for _, sec, _ in results]

    plt.figure()
    plt.plot(xs, ys, marker="o")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Ejercicio 2 — O(n)")
    plt.grid(True)
    plt.savefig(png_path, dpi=150, bbox_inches="tight")
    print(f"[SAVE] Plot -> {png_path}")


def main():
    candidate_ns = [1, 10, 100, 1000, 10_000, 100_000, 1_000_000]
    results = profile_function(candidate_ns)
    save_csv_plot(results)


if __name__ == "__main__":
    main()
