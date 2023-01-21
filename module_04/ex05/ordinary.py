#!/usr/bin/env python3


import sys
import os
import psutil


def ordinary(file_name: str):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return lines


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError("Wrong counts of argument.")
        data = ordinary(sys.argv[1])
        for line in data:
            pass
        process = psutil.Process(os.getpid())
        memory_info = process.memory_info()
        # print(f"\033[32mPeak Memory Usage = {memory_info.rss / (10**9):0.3f} GB")
        print(f"\033[32mPeak Memory Usage = {memory_info.rss / (2**30):0.3f} GB")
        cpu_times = process.cpu_times()
        print(f"\033[32mUser Mode Time + System Mode Time = {cpu_times.user + cpu_times.system:0.2f}s")
    except ValueError as err:
        print("\033[31mError:", err)
    except FileNotFoundError as err:
        print("\033[31mError:", err)
