


IPSA Toulouse | Promotion 2027 – Aero 4  
**Authors:** Simon Lignac  
**Instructor:** Jasdeep Singh | Academic Year 2025–2026

---

## Overview

This project analyses and schedules a set of **7 periodic real-time tasks** on a single processor. It covers:

1. **WCET measurement** of task τ₁ (product of two 512-bit integers) via statistical sampling
2. **Schedulability analysis** using the Liu & Layland utilisation bound and response time analysis
3. **Optimal non-preemptive EDF schedule** minimising total waiting time over one hyperperiod
4. **Relaxed schedule** where τ₅ is allowed to miss its deadline

---

## Repository Structure

```
├── generate_number/        # WCET measurement code for τ₁
├── chronometer/            # Timing utilities
├── TEST/                   # Test scripts
├── scheduling.py           # Branch-and-Bound optimal scheduler
└── README.md
```

---

## Task Set

| Task | C (ms)  | T (ms) | D (ms) |
|------|---------|--------|--------|
| τ₁   | 0.017   | 10     | 10     |
| τ₂   | 3       | 10     | 10     |
| τ₃   | 2       | 20     | 20     |
| τ₄   | 2       | 20     | 20     |
| τ₅   | 2       | 40     | 40     |
| τ₆   | 2       | 40     | 40     |
| τ₇   | 3       | 80     | 80     |

**Hyperperiod:** H = 80 ms | **Total jobs:** 29 | **Utilisation:** U ≈ 0.639

---

## Results Summary

| Metric | Value |
|--------|-------|
| Total waiting time W | 82.442 ms |
| Total busy time B | 51.136 ms |
| Total idle time I | 21.881 ms |
| Missed deadlines | 0 |

---

## How to Run

```bash
# Optimal non-preemptive EDF scheduler
python scheduling.py

# WCET measurement for τ₁ (requires Python 3.8+)
python generate_number/wcet_tau1.py
```

No external dependencies — standard library only.

---
