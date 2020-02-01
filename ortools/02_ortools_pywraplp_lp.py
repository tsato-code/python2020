#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 20:21:17 2019

@author: tsato

【説明】
線形計画問題を解くモジュール ortools.linear_solver のサンプルプログラム。

【使い方】
$ cd ./
$ python 04_ortools_pywraplp_lp.py

【参考】
- Module pywraplp, http://google.github.io/or-tools/python/ortools/linear_solver/pywraplp.html
"""

from ortools.linear_solver import pywraplp
import ortools


def solve_LP():
    # min 50 x1 + 65 x2
    # s.t.
    # 3 x1 + 2 x2 >= 9
    # 1/15 * x1 + 2/15 * x2 >= 1/3 
    # 1/6  * x1 >= 1/3
    # x1 - 3 x2 <= 0
    # 2 x2 - x2 >= 0
    # x1 >= 0
    # x2 >= 0
    # 問題の定義
    solver = pywraplp.Solver("toy", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    # 求解ステータス出力
    solver.EnableOutput()
    # 決定変数の定義
    x = {}
    x[1] = solver.NumVar(-solver.infinity(), solver.infinity(), "x[1]")
    x[2] = solver.NumVar(0, solver.infinity(), "x[2]")
    x[3] = 30
    x[4] = 100
    # 目的関数と制約条件の設定
    obj = 50*x[1]+65*x[2]+x[3]+x[4]
    solver.Minimize(obj)
    c = {}
    c[1] = solver.Add(3*x[1]+2*x[2] >= 9, "c-1")
    c[2] = solver.Add(1/15*x[1]+2/15*x[2] >= 1/3, "c-2")
    c[3] = solver.Add(1/6*x[1] >= 1/3, "c-3")
    c[4] = solver.Add(x[1]-3*x[2] <= 0, "c-4")
    c[5] = solver.Add(2*x[2]-x[2] >= 0, "c-5")
    # 上下限の設定
    x[1].SetBounds(0, 100)
    # 変数の個数と制約式の個数
    print("  |--> # of variables {}".format(solver.NumVariables()))
    print("  |--> # of constraints {}".format(solver.NumConstraints()))
    print("  |--> const. {}".format([(c[i].name(), c[i].index()) for i in c]))
    # アルゴリズムの設定
    p1 = pywraplp.MPSolverParameters()
    p1.SetIntegerParam(p1.LP_ALGORITHM, p1.BARRIER)
    print("  |--> algorithm {}".format(
            p1.GetIntegerParam(p1.LP_ALGORITHM)))
    # 前処理設定
    p1.SetIntegerParam(p1.PRESOLVE, p1.PRESOLVE_ON)
    print("  |--> presolve {}".format(
            p1.GetIntegerParam(p1.PRESOLVE)))
    # 解の再利用設定
    p1.SetIntegerParam(p1.INCREMENTALITY, p1.INCREMENTALITY_ON)
    print("  |--> incrementality {}".format(
            p1.GetIntegerParam(p1.INCREMENTALITY)))
    # 求解
    res = solver.Solve()
    # モデル出力 (lp format)
    print("  |--> export lpfile\n{}".format(solver.ExportModelAsLpFormat(True)))
    resdict = {0:"OPTIMAL", 1:"FEASIBLE", 2:"INFEASIBLE", 3:"UNBOUNDED",
               4:"ABNORMAL", 5:"MODELINVALID", 6:"NOT_SOLVED"}
    print("  |--> status {}".format(resdict[res]))
    l = [x[1].solution_value(), x[2].solution_value()]
    # 最適値の出力
    print("  |--> optimal value {}".format(solver.Objective().Value()))
    # 解の出力
    print("  |->> solution {}".format(l))
    # 基底解の出力
    print("  |--> basis status {}".format([(c[i].name(), c[i].basis_status()) for i in c]))
    # d = [x[1].DualValue(), x[2].DualValue()]
    # print("  |--> dual value {}".format(d))
    return l


if __name__=="__main__":
    print("  |--> or-tools version {}".format(ortools.__version__))
    l = solve_LP()
        