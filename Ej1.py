
"""
Exercise 1 — O(n^2 log n)
Implements the triple-nested loops and profiles runtime for various n.
Also saves a CSV and a PNG plot. Uses an iteration cap to avoid very long runs in Python.
"""

import time
import math
import csv
from typing import List, Tuple
import matplotlib.pyplot as plt


def function_ex1(n: int) -> int:
    """
    Python equivalent of:
    for (i = n/2; i <= n; i++)
      for (j = 1; j + n/2 <= n; j++)
        for (k = 1; k <= n; k *= 2)
          counter++
    Returns the counter so we can sanity-check work done.
    """
    counter = 0
    for i in range(n // 2, n + 1):
        limit = n - (n // 2)
        for j in range(1, limit + 1):
            k = 1
            while k <= n:
                counter += 1
                k *= 2
    return counter


def profile_function(
    candidate_ns: List[int],
    max_iterations: int = 50_000_00,  # ~50 millones (cap suave)
    per_n_repeats: int = 1,
) -> List[Tuple[int, float, int, bool]]:
    """
    Runs function_ex1 for each n in candidate_ns.
    Skips n if a quick iteration estimate exceeds max_iterations.
    Returns a list of tuples: (n, seconds, counter, skipped)
    """
    results = []

    for n in candidate_ns:
        i_count = (n - n // 2) + 1
        j_count = (n - n // 2)
        k_count = math.floor(math.log2(n)) + 1 if n > 0 else 1

        est = i_count * j_count * k_count
        if est > max_iterations:
            results.append((n, 0.0, 0, True))
            print(f"[SKIP] n={n} estimated iterations={est:,} > cap={max_iterations:,}")
            continue

        start = time.perf_counter()
        counter = 0
        for _ in range(per_n_repeats):
            counter = function_ex1(n)
        elapsed = time.perf_counter() - start
        results.append((n, elapsed, counter, False))
        print(f"[OK]   n={n} time={elapsed:.6f}s counter={counter:,}")
    return results


def save_csv_plot(results, csv_path="ex1_results.csv", png_path="ex1_plot.png"):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n", "seconds", "counter", "skipped"])
        for n, sec, cnt, skipped in results:
            w.writerow([n, f"{sec:.6f}", cnt, int(skipped)])

    xs = [n for (n, s, c, skip) in results if not skip]
    ys = [s for (n, s, c, skip) in results if not skip]

    if xs and ys:
        plt.figure()
        plt.plot(xs, ys, marker="o")
        plt.xlabel("Tamaño de entrada (n)")
        plt.ylabel("Tiempo de ejecución (s)")
        plt.title("Ejercicio 1 — O(n^2 log n)")
        plt.grid(True)
        plt.savefig(png_path, dpi=150, bbox_inches="tight")
        print(f"[SAVE] Plot -> {png_path}")
    else:
        print("[WARN] No points to plot (all skipped?).")


def main():
    candidate_ns = [1, 10, 100, 1000, 10_000, 100_000, 1_000_000]
    results = profile_function(candidate_ns)
    save_csv_plot(results)


if __name__ == "__main__":
    main()
