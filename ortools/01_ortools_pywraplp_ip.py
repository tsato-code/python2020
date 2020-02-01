#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:03:14 2019

@author: tsato

【説明】
整数線形計画問題を解くモジュール ortools.linear_solver のサンプルプログラム。

【使い方】
$ cd ./
$ python 02_ortools_pywraplp.py

【参考】
- Module pywraplp, http://google.github.io/or-tools/python/ortools/linear_solver/pywraplp.html
"""
from ortools.linear_solver import pywraplp


def solve_IP():
    # min -2 x1 + x2
    # s.t.
    #   -2x1 - 3x2 >= -6
    #  x1 - 2x2 >= -2
    #  x1 >= 0, x2 >= 0
    #  x1, x2 in Z
    # 問題の定義
    prob = pywraplp.Solver("toy", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    # prob.EnableOutput()
    
    prob.AT_UPPER_BOUND = 100 
    prob.AT_LOWER_BOUND = 0
    # prob.SetBounds(-100, 100)
    # 変数の定義
    x = {}
    infinity = prob.infinity()
    x[1] = prob.IntVar(0, infinity, "x[1]")
    x[2] = prob.IntVar(0, infinity, "x[2]")
    # 目的関数
    obj = -2 * x[1] + x[2]
    x[1].SetBounds(-100, 100)
    print(obj)
    prob.Minimize(obj)
    # 制約条件
    prob.Add( -2*x[1]-3*x[2 ]>= -6 )
    prob.Add( x[1]-2*x[2] >= -2 )
    # 求解
    prob.SetHint([x[1]], [-5])
    res = prob.Solve()
    print(prob.AT_UPPER_BOUND)
    print(prob.ComputeConstraintActivities())
    print(prob.WallTime())
    # ステータス
    resdict = {0:"OPTIMAL", 1:"FEASIBLE", 2:"INFEASIBLE", 3:"UNBOUNDED",
               4:"ABNORMAL", 5:"MODELINVALID", 6:"NOT_SOLVED"}
    print("MIP solver result: {}".format(resdict[res]))
    l = [x[1].solution_value(), x[2].solution_value()]
    print(prob.variables())
    return l


if __name__=="__main__":
    l = solve_IP()
    print(l)