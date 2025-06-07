# 🗓️ Meeting Schedule

## Problem Description

Given two lists of **non-overlapping**, **sorted** time intervals `slots1` and `slots2` representing available time slots for two people, and a duration `duration`, your task is to find the **earliest time slot** that works for both people and is of at least the given duration.

Each time slot is represented as a list of two integers `[start, end]` where `start < end`. The time is given in minutes.

Return a list with the start and end time of the meeting slot in the format `[start, start + duration]` if a common slot is found. If there is **no common slot**, return an empty list.

> Both `slots1` and `slots2` are sorted by start time and contain only non-overlapping intervals.

---

## Example

**Input:**

```python
slots1 = [[10, 50], [60, 120], [140, 210]]
slots2 = [[0, 15], [60, 70]]
duration = 8
```

**Output:**
```python
[60, 68]
```
