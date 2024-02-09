# Schedule Library imported
import schedule
import time


# Functions setup
def sudo_placement():
    print("Get ready for Sudo Placement at Geeksforgeeks")


def good_luck():
    print("Good Luck for Test")


def work():
    print("Study and work hard")


def bedtime():
    print("It is bed time go rest")


def geeks():
    print("modon says lovely")


# Task scheduling
# After every 10mins geeks() is called.

schedule.every(1).second.do(geeks)
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)