from datetime import datetime, date
import urllib
import re
import webbrowser
import sched
import time

sec_between_checks = 60

days = [("2013-07-26", "day-nineteen"),
    ("2013-07-27", "day-twenty"), ("2013-07-28", "day-twenty-one"),
    ("2013-07-29", "day-twenty-two"), ("2013-07-30", "day-twenty-three"),
    ("2013-07-31", "day-twenty-four"), ("2013-08-01", "day-twenty-five"),
    ("2013-08-02", "day-twenty-six"), ("2013-08-03", "day-twenty-seven"),
    ("2013-08-04", "day-twenty-eight"), ("2013-08-05", "day-twenty-nine"),
    ("2013-08-06", "day-thirty"), ("2013-08-07", "day-thirty-one"),
    ("2013-08-08", "day-thirty-two"), ("2013-08-09", "day-thirty-three"),
    ("2013-08-10", "day-thirty-four"), ("2013-08-11", "day-thirty-five"),
    ("2013-08-12", "day-thirty-six"), ("2013-08-13", "day-thirty-seven"),
    ("2013-08-14", "day-thirty-eight"), ("2013-08-15", "day-thirty-nine"),
    ("2013-08-16", "day-forty")
]


def check_new_post(sc):
    now = datetime.now().time()

    if now.hour >= 14:
        data = urllib.urlopen("http://fortydaysofdating.com/").read()

        # find what post it should search
        today = str(date.today())
        for post_date, post_day in days:
            if post_date == today:
                post = post_day
                break

        match = re.search(r'post-'+post, data)
        if match:
            print_msg("New post available!")
            webbrowser.open_new("http://fortydaysofdating.com/"+post)
        else:
            print_msg("Nothing new so far...")
            sc.enter(sec_between_checks, 1, check_new_post, (sc,))
    else:
        print_msg("It's still early. Waiting a little longer to scrap the site.")
        sc.enter(sec_between_checks*5, 1, check_new_post, (sc,))


def print_msg(msg):
    now = datetime.now().time()
    print "[%.2d:%.2d:%.2d] - %s" % (now.hour, now.minute, now.second, msg)


def main():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(sec_between_checks, 1, check_new_post, (s,))
    s.run()


if __name__ == "__main__":
    main()
