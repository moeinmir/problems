#!/usr/bin/python3
import sys
if sys.argv[3]=="+":
    print(float(sys.argv[1])+float(sys.argv[2]))
if sys.argv[3]=="-":
    print(sys.argv[1]-sys.argv[2])
if sys.argv[3]=="*":
    print(sys.argv[1]*sys.argv[2])
if sys.argv[3]=="/":
    print(sys.argv[1]/sys.argv[2])

