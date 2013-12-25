#!/usr/bin/env python
import json

def main():
    with open('classes.json') as fin:
        data = json.load(fin)

    print data['name']

if __name__ == "__main__":
    main()