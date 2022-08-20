import os
import sys

for k, v in os.__dict__.items():
    print(k, '\t\t', v)