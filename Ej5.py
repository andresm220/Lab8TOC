#!/usr/bin/env python3
"""
Exercise 5 — True/False with justifications printed.
(a) True — transitivity of Theta
(b) False — O-transitivity gives f=O(h), not h=Ω(f)
(c) False — program builds all sub-tuples => Θ(n^2), not Θ(n!)
Also includes a tiny generator to empirically count unique slices for (c).
"""

def statement_a():
    print("a) TRUE. If f(n)=Θ(g(n)) and g(n)=Θ(h(n)), then f(n)=Θ(h(n)) by transitivity of Θ.")

def statement_b():
    print("b) FALSE. From f(n)=O(g(n)) and g(n)=O(h(n)), we only infer f(n)=O(h(n)).")
    print("         This does not imply h(n)=Ω(f(n)) in the form stated.")

def count_unique_slices(n: int) -> int:
    # Mirrors the Python A(n) snippet conceptually: adds every slice [i:j] with i<j to a set
    tup = tuple(range(n))
    S = set()
    for i in range(n):
        for j in range(i+1, n):
            S.add(tup[i:j])
    return len(S)

def statement_c():
    print("c) FALSE. The number of slices [i:j] with 0 <= i < j <= n is n*(n-1)/2 = Θ(n^2).")
    # quick sanity checks
    for n in [5, 10, 100]:
        print(f"   n={n} -> unique slices={count_unique_slices(n)} (expected ~n(n-1)/2)")

def main():
    statement_a()
    statement_b()
    statement_c()

if __name__ == "__main__":
    main()
