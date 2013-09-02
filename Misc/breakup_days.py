from datetime import datetime, date


def main():
    fateful_day = date(2013, 06, 26)
    delta = date.today() - fateful_day

    print "%s days have passed since we broke up." % delta.days
if __name__ == "__main__":
    main()