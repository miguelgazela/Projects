#!/usr/bin/env python
import json

"""
Class note builder for college
"""

def main():
    with open('classes.json') as fin:
        data = json.load(fin)

    print data['name']

if __name__ == "__main__":
    main()