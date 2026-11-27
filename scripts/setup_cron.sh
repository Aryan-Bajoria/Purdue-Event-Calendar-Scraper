#!/bin/bash

#Find the absolute path of the scripts file
SCRIPT="$(cd "$(dirname "$0")/../scripts" && pwd)/scraper.py"
CRON_JOB="0 9 * * 1 /usr/bin/python3 \"$SCRIPT\""

(crontab -l 2>/dev/null | grep -F "$SCRIPT") &&  {
    echo "Cron job already exists."
    exit 0
}

(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "Cron job set up for every week for 9:00 a.m. every Monday"