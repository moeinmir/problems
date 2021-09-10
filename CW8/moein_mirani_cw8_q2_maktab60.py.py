#!/usr/bin/python3
import argparse
parser=argparse.ArgumentParser(description="variables for cal")
parser.add_argument("num1",help="help1",type=float)
parser.add_argument("num2",help="help1",type=float)
#below line does nor make scence ignore it
parser.add_argument("-o","--operation",action="store_true",help="help",required=True)
group=parser.add_mutually_exclusive_group()
group.add_argument("--add",action="store_true")
group.add_argument("--sub",action="store_true")
group.add_argument("--mul",action="store_true")
group.add_argument("--dev",action="store_true")
args=parser.parse_args()
if args.operation:
    if args.add:
        print(int(args.num1)+int(args.num2))
if args.operation:
    if args.sub:
        print(int(args.num1)-int(args.num2))
if args.operation:
    if args.mul:
        print(int(args.num1)*int(args.num2))
if args.operation:
    if args.dev:
        print(int(args.num1)/int(args.num2))
