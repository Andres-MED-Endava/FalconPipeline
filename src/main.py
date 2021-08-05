#!/bin/python

import subprocess

""" Python code for Proof Of Concept"""

print("Hello World")

NUM1 = 1
NUM2 = 2
SUM = NUM1 + NUM2
print(SUM)

domain = input("Enter the Domain: ")
output = subprocess.check_output(f"nslookup {domain}", shell=True, encoding="UTF-8")
print(output)
