# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:44:32 2026
@author: ligna
"""
from math import lcm

# ==========================================================
# FINAL ASSIGNMENT - NON-PREEMPTIVE SCHEDULER
# Method: Branch and Bound
# C1 = 3
# Goals:
#   1) Every job must meet its deadline
#   2) Find the ordering that minimizes total waiting time
# ==========================================================

tasks = [
    {"name": "T1", "C": 3, "T": 10},
    {"name": "T2", "C": 3, "T": 10},
    {"name": "T3", "C": 2, "T": 20},
    {"name": "T4", "C": 2, "T": 20},
    {"name": "T5", "C": 2, "T": 40},
    {"name": "T6", "C": 2, "T": 40},
    {"name": "T7", "C": 3, "T": 80},
]

# ==========================================================
# Compute the hyperperiod (LCM of all periods)
# ==========================================================
hyper = 1
for t in tasks:
    hyper = lcm(hyper, t["T"])
print("Hyperperiod =", hyper)

# ==========================================================
# Build the full job list for one hyperperiod
# For task i: job k is released at (k-1)*T and due at k*T
# ==========================================================
jobs = []
for task in tasks:
    nb = hyper // task["T"]
    for i in range(nb):
        r = i * task["T"]
        d = r + task["T"]
        jobs.append({
            "id":       f"{task['name']}_{i+1}",
            "task":     task["name"],
            "C":        task["C"],
            "release":  r,
            "deadline": d
        })

# ==========================================================
# Branch and Bound
# ==========================================================
best_wait  = float("inf")
best_sched = None

def lower_bound_wait(time, remaining):
    """
    Computes an optimistic lower bound on the remaining waiting time.
    We assume each unscheduled job starts as soon as it is released,
    with no gaps between executions (best-case scenario).
    """
    lb = 0
    t  = time
    future = sorted(remaining, key=lambda x: x["release"])
    for j in future:
        start = max(t, j["release"])
        lb += start - j["release"]
        t   = start + j["C"]
    return lb

def branch(time, remaining, schedule, total_wait):
    global best_wait, best_sched

    # All jobs scheduled: check if this solution is the best so far
    if not remaining:
        if total_wait < best_wait:
            best_wait  = total_wait
            best_sched = schedule[:]
        return

    # Cut this branch if even the optimistic bound can't beat the current best
    if total_wait + lower_bound_wait(time, remaining) >= best_wait:
        return

    # Identify jobs that are already available at current time
    ready = [j for j in remaining if j["release"] <= time]

    # No job ready yet: skip idle time and jump to the next release
    if not ready:
        next_release = min(j["release"] for j in remaining)
        branch(next_release, remaining, schedule, total_wait)
        return

    # Try jobs in EDF order to find good solutions early (better pruning)
    ready.sort(key=lambda x: x["deadline"])

    for job in ready:
        start  = time
        finish = start + job["C"]

        # Skip this job if it would miss its hard deadline
        if finish > job["deadline"]:
            continue

        wait = start - job["release"]

        new_sched = schedule + [{
            "Job":      job["id"],
            "Start":    start,
            "Finish":   finish,
            "Deadline": job["deadline"],
            "Waiting":  wait,
            "Response": finish - job["release"]
        }]

        # Remove selected job from the remaining pool
        idx           = remaining.index(job)
        new_remaining = remaining[:idx] + remaining[idx+1:]

        branch(finish, new_remaining, new_sched, total_wait + wait)

# ==========================================================
# Launch the search
# ==========================================================
branch(0, jobs, [], 0)

# ==========================================================
# Display results
# ==========================================================
print("\n===== OPTIMAL RESULT =====")
if best_sched is None:
    print("Task set NOT schedulable")
else:
    print("Schedulable = YES")
    print("Minimum Total Waiting Time =", best_wait)
    print()
    for row in best_sched:
        print(row)
