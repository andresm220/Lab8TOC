
"""
Exercise 3 — O(n^2)
Implements the double loop with j += 4 and profiles runtime.
Saves CSV and PNG plot.
"""

import time
import csv
from typing import List, Tuple
import matplotlib.pyplot as plt


def function_ex3(n: int) -> int:
    """
    Equivalent:
    for (i = 1; i <= n/3; i++) {
      for (j = 1; j <= n; j += 4) { printf(...); }
    }
    Returns the number of "prints" (counter).
    """
    count = 0
    for i in range(1, n // 3 + 1):
        j = 1
        while j <= n:
            count += 1
            j += 4
    return count


def profile_function(candidate_ns: List[int]) -> List[Tuple[int, float, int]]:
    results = []
    for n in candidate_ns:
        start = time.perf_counter()
        cnt = function_ex3(n)
        elapsed = time.perf_counter() - start
        results.append((n, elapsed, cnt))
        print(f"[OK] n={n} time={elapsed:.6f}s count={cnt}")
    return results


def save_csv_plot(results, csv_path="ex3_results.csv", png_path="ex3_plot.png"):
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
    plt.title("Ejercicio 3 — O(n^2)")
    plt.grid(True)
    plt.savefig(png_path, dpi=150, bbox_inches="tight")
    print(f"[SAVE] Plot -> {png_path}")


def main():
    candidate_ns = [1, 10, 100, 1000, 10_000]
    results = profile_function(candidate_ns)
    save_csv_plot(results)


if __name__ == "__main__":
    main()
