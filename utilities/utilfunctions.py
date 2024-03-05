from datetime import datetime, timedelta
import shutil
import sys


def start_time_for_timesheet():
    formatted_date = "%d/%m/%y %H:%M:%S"
    # d = datetime.today(formatted_date)
    d = datetime.now() + timedelta(days=-1, hours=-5, minutes=3)
    # v = str(d.strftime("%d/%m/%y %H:%M:%S %p"))
    v = str(d.strftime("%d/%m/%Y %H:%M %p"))
    splitted_date = v.split(" ")
    return splitted_date


def end_time_for_timesheet():
    formatted_date = "%d/%m/%y %H:%M:%S"
    # d = datetime.today(formatted_date)
    d = datetime.now() + timedelta(days=-1, hours=-5, minutes=5)
    # v = str(d.strftime("%d/%m/%y %H:%M:%S %p"))
    v = str(d.strftime("%d/%m/%Y %H:%M %p"))
    splitted_date = v.split(" ")
    return splitted_date


def start_time_for_absence():
    formatted_date = "%d/%m/%y %H:%M:%S"
    # d = datetime.today(formatted_date)
    d = datetime.now() + timedelta(days=-1, hours=-4, minutes=3)
    # v = str(d.strftime("%d/%m/%y %H:%M:%S %p"))
    v = str(d.strftime("%d/%m/%Y %H:%M %p"))
    splitted_date = v.split(" ")
    return splitted_date


def end_time_for_absence():
    formatted_date = "%d/%m/%y %H:%M:%S"
    # d = datetime.today(formatted_date)
    d = datetime.now() + timedelta(days=-1, hours=-4, minutes=5)
    # v = str(d.strftime("%d/%m/%y %H:%M:%S %p"))
    v = str(d.strftime("%d/%m/%Y %H:%M %p"))
    splitted_date = v.split(" ")
    return splitted_date


def create_zip_file():
    shutil.make_archive(sys.path[0] + '\\Zipped file', 'zip', sys.path[0] + '\\Reports')
