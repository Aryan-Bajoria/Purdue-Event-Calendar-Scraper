## Purdue Events Calendar Scraper

A Python script that scrapes the Purdue event calendar API and creates a .csv file on your desktop with events titles, timings and links relevant to you. Runs automatically on a cron job every week.

## The Problem

While there are many events on campus including career fairs and seminars, it is hard to find relevant ones in time and keep track of event details through the official Purdue event calendar, leading to many missed opportunities. Additionally, the official event calendar is slow and cluttered, making it hard to locate important events at first glance. Furthermore, looking through the calendar regularly is repetitive and cumbersome.

## How It Works

The project fetches events for the next week from the Purdue events calendar API and parses it into json. It then reads user-defined topics from a config.json file and finds relevant matches from the scraped data. It then stores the matches into events.csv in the output directory defined by the user in config.json.

![System diagram](docs/System%20Diagram.png)

## Tech Stack

- **Language:** Python
- **Libraries:** requests, json, os, pathlib
- **External tools:** cron, Purdue Brand Studio API

## Setup

### Prerequisites
* Python 3.8+ (`python3 --version`)
* Git (`git --version`)
* MacOS, Linux, or WSL (for cron scheduling)

---

### 1. Clone the repository

```bash
git clone https://github.com/Aryan-Bajoria/Purdue-Event-Calendar-Scraper
cd Purdue-Event-Calendar-Scraper
```
### 2. Set up a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Preferences

Add relevant, excluded keywords, and output directory in config.json

### 5. Run the test Suite

```bash
python3 -m unittest discover -s tests
```

### 6. Automate weekly cron runs

```bash
chmod +x scripts/setup_cron.sh
./scripts/setup_cron.sh
```

## Usage

Run the script manually

```bash
python3 -m src.scraper
```

## Roadmap

- [ ] Set up an event attendance tracking system.
- [ ] Set up notes for attended events.
- [ ] Link to Google calendar


## Author

Created by [Aryan Bajoria](https://github.com/Aryan-Bajoria/)
