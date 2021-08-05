#!/bin/python
""" Python code for Proof Of Concept"""

print("Hello World")

NUM1 = " "
NUM2 = 2
SUM = NUM1 + NUM2
print(SUM)

# nslookup.py
import subprocess

domain = input("Enter the Domain: ")
output = subprocess.check_output(f"nslookup {domain}", shell=True, encoding="UTF-8")
print(output)
