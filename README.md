# Constraint Satisfaction Problem (CSP) Solver

A modular Python-based solver for **Constraint Satisfaction Problems (CSPs)**, designed with clean abstractions for variables, domains, and constraints.  
The project formulates CSP solving as a **search problem**, enabling systematic exploration with early pruning via consistency checking.

---

## Overview

This project implements a general-purpose CSP framework that supports:
- Flexible variable and domain definitions
- Custom constraint modeling
- Search-based solution strategies
- Early pruning of inconsistent partial assignments

The solver demonstrates how classical AI problems such as CSPs can be reduced to search problems and efficiently solved using depth-first search.

---

## Key Features

- **Modular CSP Representation**
  - Abstract `Variable`, `Constraint`, and `CSP` classes
  - Support for relational, difference, ordering, and parity constraints

- **Search-Based Solver**
  - Reduction of CSPs to a generic search problem
  - Depth-first search over partial assignments
  - Consistency checking to prune invalid branches early

- **Performance Insight**
  - Tracks the number of failing branches during search
  - Enables basic analysis of search efficiency

- **Extensibility**
  - Easily adaptable to new CSP formulations
  - Reusable search and constraint abstractions

---

## How to Run

From the project root directory:

```bash
python csp_search.py
