# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:51:28 2021

@author: Pnach
"""
import glob
import numpy as np
import pandas as pd
import folium
import webbrowser
from folium import plugins


"""
path = "2018-12-25"
all_files = glob.glob(path + "/*.csv")
dfs = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    dfs.append(df)
frame = pd.concat(dfs, axis=0, ignore_index=True)
"""


def question_1():
    path = "2018-12-25/2018-12-25.05.csv"
    df = pd.read_csv(path)
    answer = len(df["vid"].unique())
    print(answer)


def question_2():
    path = "2018-12-25/2018-12-25.05.csv"
    df = pd.read_csv(path)
    answer = df[["speed", "for_hire_light"]
                ][df["speed"] > 0][df["for_hire_light"] == 0].mean()

    print(answer)


def question_3():
    path = "2018-12-25/2018-12-25.05.csv"
    df = pd.read_csv(path)
    answer = df[(df["vid"] == "bwmSJnFxrwrAUjqBcqCWOlj5f9Y")
                & (df["for_hire_light"] == 0)]
    answer = df[["timestamp"]][df["vid"] ==
                               "bwmSJnFxrwrAUjqBcqCWOlj5f9Y"][df["for_hire_light"] == 0]
    print(answer)


def question_4():
    path = "2018-12-25"
    all_files = glob.glob(path + "/*.csv")
    dfs = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        dfs.append(df)
    df = pd.concat(dfs, axis=0, ignore_index=True)
    answer = df[["speed", "for_hire_light"]
                ][df["speed"] > 0][df["for_hire_light"] == 0].mean()
    print(answer)


def question_5():
    path = "2018-12-25"
    all_files = glob.glob(path + "/*.csv")
    dfs = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        dfs.append(df)
    big = pd.concat(dfs, axis=0, ignore_index=True)
    answer = big[(big["for_hire_light"] == 0) &
                 big["speed"] != 0].groupby("vid").max().mean()
    print(answer)


def question_6():
    path = "2018-12-25"
    all_files = glob.glob(path + "/*.csv")
    dfs = []
    taxi_in_hour = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        taxi_in_hour.append(len(df["vid"].unique()))
        dfs.append(df)
    df = pd.concat(dfs, axis=0, ignore_index=True)
    answer = taxi_in_hour.index(max(taxi_in_hour))
    print(answer)


# question_1()
# question_2()
# question_3()
# question_4()
question_5()
# question_6()
