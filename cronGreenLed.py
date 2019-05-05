import sys
import db

if sys.argv[1] == "HIGH":
    # change db value to 1 if on
    # but don't actually turn on the light - let the cron on uptime.py do that after the next check
    # status = GPIO.HIGH
    db.overrideLedActive('green', 1)
else:
    # turn off the green light and update the database - the light won't come back on until the previous
    # condition is met
    # status = GPIO.LOW
    db.overrideLedActive('green', 0)
