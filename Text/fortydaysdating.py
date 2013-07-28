from datetime import datetime, date
import urllib
import re
import webbrowser
import sched
import time

sec_between_checks = 60

days = [("2013-07-26", "day-nineteen"),
    ("2013-07-27", "day-twenty"), ("2013-07-28", "day-twentyone"),
    ("2013-07-29", "day-twentytwo"), ("2013-07-30", "day-twentythree"),
    ("2013-07-31", "day-twentyfour"), ("2013-08-01", "day-twentyfive"),
    ("2013-08-02", "day-twentysix"), ("2013-08-03", "day-twentyseven"),
    ("2013-08-04", "day-twentyeight"), ("2013-08-05", "day-twentynine"),
    ("2013-08-06", "day-thirty"), ("2013-08-07", "day-thirtyone"),
    ("2013-08-08", "day-thirtytwo"), ("2013-08-09", "day-thirtythree"),
    ("2013-08-10", "day-thirtyfour"), ("2013-08-11", "day-thirtyfive"),
    ("2013-08-12", "day-thirtysix"), ("2013-08-13", "day-thirtyseven"),
    ("2013-08-14", "day-thirtyeight"), ("2013-08-15", "day-thirtynine"),
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
