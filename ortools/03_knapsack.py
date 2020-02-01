#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 23:04:51 2020

@author: tsato

[説明]
MIP の求解を時間で打ち切ったときの暫定解を出力するプログラム。

[使い方]
パラメータを適当にいじってステータスを FEASIBLE にする。
以下は手元の Macbook Air でたまに FEASIBLE となるパターン。
$ python 03_knapsack.py
"""

from ortools.linear_solver import pywraplp
import random


n_items = 30000
capacity = 10000
max_weight = 20
max_gain = 20
time_limit = 3
n_threads = 1


random.seed(99)


def knapsack_solverlem(weights, gains):
    solver = pywraplp.Solver("knapsack_solverlem", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    solver.SetNumThreads(n_threads)
    solver.set_time_limit(time_limit*1000*n_threads)
    # solver.EnableOutput()
    x = {}
    for i in range(n_items):
        x[i] = solver.BoolVar("x[{}]".format(i))
    obj = solver.Sum( gains[i] * x[i] for i in range(n_items) )
    solver.Maximize(obj)
    total_weights = solver.Sum( weights[i] * x[i] for i in range(n_items) )
    solver.Add( total_weights <= capacity )
    res = solver.Solve()
    status = ["* OPTIMAL *", "FEASIBLE", "INFEASIBLE", "UNBOUNDED", "ABNORMAL", "MODELINVALID", "NOT_SOLVED"]
    print("  |--> status: {}".format(status[res]))
    if res==0:
        print("  |--> optimal value {}".format(solver.Objective().Value()))
        solution = [x[i].solution_value() for i in range(n_items)]
        print("  |--> optimal solution: {}".format(solution[:3]))
    elif res==1:
        print("  |--> provisional value {}".format(solver.Objective().Value()))
        solution = [x[i].solution_value() for i in range(n_items)]
        print("  |--> feasible solution: {}".format(solution[:3]))
    else:
        solution = []
    return solution


if __name__=="__main__":
    weights = [random.randint(1, max_weight) for _ in range(n_items)]
    gains = [random.randint(1, max_gain) for _ in range(n_items)]
    print("  |--> weights: {}".format(weights[:3]))
    print("  |--> gains: {}".format(gains[:3]))
    solution = knapsack_solverlem(weights, gains)


"""
  |--> weights: [13, 13, 7]
  |--> gains: [9, 10, 1]
  |--> status: FEASIBLE
  |--> provisional value 57041.0
  |--> feasible solution: [0.0, 0.0, 0.0]
"""