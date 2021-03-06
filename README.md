# Python Bytes Podcast - Telegram Bot

[![Build Status](https://travis-ci.org/AbhishekPednekar84/python-bytes-bot.svg?branch=master)](https://travis-ci.org/AbhishekPednekar84/python-bytes-bot)

This repository contains the Python (v3.7) code for the [Python Bytes Podcast Telegram bot](https://t.me/@PythonBytesBot).

## Using the bot

1. Search for the bot in Telegram using either **Python Bytes Podcast** or **@PythonBytesBot**
2. Click **START** to begin conversing with the bot
3. To search for podcast episodes, send any search text (for example, `treebeard`)
4. To search with multiple words, separate them with a `-` (for example, `sanic-django`)

## Commands
1. `/start` - To start interacting with the bot and get a welcome message
2. Any search text

## Creating a local setup

1. Clone the current repository - `git clone https://github.com/AbhishekPednekar84/python-bytes-bot`
2. Create a virtual environment - `python -m venv venv`
3. Activate the virtual environment - `venv\Scripts\activate.bat` (Windows), `source venv/bin/activate` (OSx / Linux)
4. Install the project dependencies - `pip install -r requirements.txt`
5. Create a `.env` file and add an environment variable called `TELEGRAM_TOKEN` (refer to `.env.example`)
6. Run the code - `python bot/server.py` or `python3 bot/bot_server.py`
7. To run the tests - `pytest`

---

<p align="center"><img src="https://github.com/AbhishekPednekar84/python-bytes-bot/blob/master/images/bot1.jpg" alt="Bot1"></p>

---

<p align="center"><img src="https://github.com/AbhishekPednekar84/python-bytes-bot/blob/master/images/bot2.jpg" alt="Bot2"></p>
