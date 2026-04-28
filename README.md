# In422 – Real-Time Task Scheduling

**Real-Time Information Systems** | IPSA Toulouse | Promotion 2027 – Aero 4  
**Author:** Simon Lignac  
**Instructor:** Jasdeep Singh | Academic Year 2025–2026

---

## Overview

This project analyses and schedules a set of **7 periodic real-time tasks** on a single processor. It covers:

1. **WCET measurement** of task τ₁ (product of two 512-bit integers) via statistical sampling
2. **Schedulability analysis** using the Liu & Layland utilisation bound and response time analysis
3. **Optimal non-preemptive schedule** minimising total waiting time over one hyperperiod
4. **Relaxed schedule** where τ₅ is allowed to miss its deadline

---

## Repository Structure

```
├── chronometer/            # C timing utility for τ₁ measurement
├── generate_number/        # C++ 512-bit integer generator
├── scheduling.py           # Branch-and-Bound optimal scheduler
├── scheduling_relax_t5.py  # Modified scheduler (τ₅ soft deadline)
└── README.md
```

---

## Task Set

| Task | C (ms)  | T (ms) | D (ms) |
|------|---------|--------|--------|
| τ₁   | 0.084   | 10     | 10     |
| τ₂   | 3       | 10     | 10     |
| τ₃   | 2       | 20     | 20     |
| τ₄   | 2       | 20     | 20     |
| τ₅   | 2       | 40     | 40     |
| τ₆   | 2       | 40     | 40     |
| τ₇   | 3       | 80     | 80     |

**Hyperperiod:** H = 80 ms | **Total jobs:** 29 | **Utilisation:** U ≈ 0.646

---

## Results Summary

| Metric | Value |
|--------|-------|
| WCET C₁ (measured) | 84 µs |
| Total waiting time W | 82.184 ms |
| Total busy time B | 51.184 ms |
| Total idle time I | 28.816 ms |
| Missed deadlines | 0 |

Relaxing τ₅'s deadline yields W' = 82.184 ms — no improvement, as the optimal schedule already respects all deadlines.

---

## How to Run

```bash
# Optimal non-preemptive scheduler
python scheduling.py

# Modified scheduler (τ₅ soft deadline)
python scheduling_relax_t5.py
```


