#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on July 1 2021 @ HongKong
Author: Changlong Li
Email: clli@cs.ecnu.edu.cn
"""

"""
Based on this script, you can obtain the memory information of mobile devices, and output the detected information to
the directory ./dataset/
"""

import os
import time

import re

def get_swap_partition_used():
    f = os.popen('adb shell "cat /proc/swaps"')
    output = f.read()
    #print(output)
    Used = re.split(r"[ ]+", output)[1].split('\t')[2]
    #print(Used)
    file_handle = open('dataset/swapUsed.txt', mode='a+')
    file_handle.write(Used + '\n')
    return Used

def get_mem_available():
    f = os.popen('adb shell "cat /proc/meminfo"')
    output = f.read()
    #print(output)
    MemAvailable = output.split('\n')[2].split()[1]
    #print(MemAvailable)
    file_handle = open('dataset/memAvailable.txt', mode='a+')
    file_handle.write(MemAvailable + '\n')
    return MemAvailable

def get_pswapin():
    f = os.popen('adb shell "cat /proc/vmstat | grep "pswpin""')
    output = f.read()
    #print(output)
    Pswpin = output.split()[1]
    #print(Pswpin)
    file_handle = open('dataset/pSwpin.txt', mode='a+')
    file_handle.write(Pswpin + '\n')
    return Pswpin

def get_pswapout():
    f = os.popen('adb shell "cat /proc/vmstat | grep "pswpout""')
    output = f.read()
    #print(output)
    Pswpout = output.split()[1]
    #print(Pswpout)
    file_handle = open('dataset/pSwpout.txt', mode='a+')
    file_handle.write(Pswpout + '\n')
    return Pswpout

def get_active_anon():
    f = os.popen('adb shell "cat /proc/meminfo"')
    output = f.read()
    # print(output)
    ActiveAnon = output.split('\n')[8].split()[1]
    #print(ActiveAnon)
    file_handle = open('dataset/activeAnon.txt', mode='a+')
    file_handle.write(ActiveAnon + '\n')
    return ActiveAnon

def get_inactive_anon():
    f = os.popen('adb shell "cat /proc/meminfo"')
    output = f.read()
    # print(output)
    InActiveAnon = output.split('\n')[9].split()[1]
    #print(InActiveAnon)
    file_handle = open('dataset/InActiveAnon.txt', mode='a+')
    file_handle.write(InActiveAnon + '\n')
    return InActiveAnon

def get_active_file():
    f = os.popen('adb shell "cat /proc/meminfo"')
    output = f.read()
    # print(output)
    ActiveFile = output.split('\n')[10].split()[1]
    #print(ActiveFile)
    file_handle = open('dataset/ActiveFile.txt', mode='a+')
    file_handle.write(ActiveFile + '\n')
    return ActiveFile

def get_inactive_file():
    f = os.popen('adb shell "cat /proc/meminfo"')
    output = f.read()
    # print(output)
    InActiveFile = output.split('\n')[11].split()[1]
    #print(InActiveFile)
    file_handle = open('dataset/InactiveFile.txt', mode='a+')
    file_handle.write(InActiveFile + '\n')
    return InActiveFile

if __name__ == '__main__':
    #get_swap_partition_used()
    #get_mem_available()
    #get_pswapin()
    #get_pswapout()
    #get_active_anon()
    #get_inactive_file()

    swapUsed = []
    memAvailable = []
    pSwpout = []
    pSwpin = []
    activeAnon = []
    inactiveAnon = []
    activeFile = []
    inactiveFile = []

    while True:
        swapUsed.append(get_swap_partition_used())
        memAvailable.append(get_mem_available())
        pSwpout.append(get_pswapout())
        pSwpin.append(get_pswapin())
        activeAnon.append(get_active_anon())
        inactiveAnon.append(get_inactive_anon())
        activeFile.append(get_active_file())
        inactiveFile.append(get_inactive_file())
        time.sleep(3)
