#!/usr/bin/env python
import json
import os
import sys
from datetime import datetime
from datetime import timedelta


def read_config_file():
    try:
        with open('config.json') as config_file:
            return json.load(config_file)
    except IOError:
        return None;


def process_class(class_):
    create_notes('praticas', class_['schedule']['practical'])
    create_notes('teoricas', class_['schedule']['theoretical'])


def create_notes(folder, classes):
    if len(classes) > 0:
        os.mkdir(folder)
        os.chdir(os.path.join(os.getcwd(), folder))

        for p in classes:
            start = datetime.strptime(p['start_date'], "%d/%m/%Y")
            end = datetime.strptime(p['end_date'], "%d/%m/%Y")
            num_class = 1

            while True:
                with open('aula_{0}.md'.format(num_class), 'w') as fout:
                    fout.write("# {0}\n## Aula {1}".format(
                        start.strftime("%d/%m/%Y"),
                        num_class))

                num_class += 1 
                start = start + timedelta(days=7)

                if end < start:
                    break


def main():
    data = read_config_file()
    if not data:
        print "Config file is missing."
        return

    path = data['path']

    # create the semester folder
    if not os.path.exists(path):
        os.mkdir(path)

    # create a folder for each class
    for s_class in data['classes']:
        if not os.path.exists(os.path.join(path, s_class['akronim'])):
            os.mkdir(os.path.join(path, s_class['akronim']))
            os.chdir(os.path.join(path, s_class['akronim']))
            process_class(s_class)
        else:
            print "Folder '{0}' already exists at {1}".format(
                s_class['akronim'], path)



if __name__ == "__main__":
    sys.exit(main())