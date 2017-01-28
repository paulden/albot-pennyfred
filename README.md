# Albot Pennyfred

## Introduction

Albot Pennyfred (or Alfred Pennyworth, depending of your inspiration) is a Twitter bot built on a Django API, ready to help you whenever you need information from your favorite Twitter butler.

## Languages and resources

This project is developed using Python 3.5 with Django 1.9.9. To build the API, the Django Rest Framework was used.

This very API calls other API to gather information and deliver it on Twitter. These API are described later on.

The bot in itself is using Twitter Streaming API to interact with users referring to the account.
The streaming API is consumed using Tweepy which makes it easy to stream incoming tweets.

## Run it locally

Should you have Alfred running locally on your machine, here is the way to set it up:

- You should have Python 3 installed on your machine. If need be, install it using a command line

```bash
sudo apt-get install python3
```

- You also need to have Django, the Django Rest Framework and Tweepy. You may install it using a command line.
You may have to use a `sudo` and/or make sure you have Python 3 files installed using `pip3` instead of `pip`

```bash
pip install django
pip install djangorestframework
pip install tweepy
```

- You can know run Albot Pennyfred locally using these commands.
You may have to use `python3` instead of `python` if your machine has Python 2 as default

```bash
cd albotpennyfred
python manage.py runserver
```

- You can know access Albot API with requests such as http://127.0.0.1:8000/weather/brussels (in your browser or a terminal)

## Features

### Read your tweets

Whenever a Twitter user refers to Alfred, the tweet will be read and Alfred will react properly. He may acknowledge other users interactions.

### Help you

As a butler, Alfred will try to help you in these simple matters:

#### Tell you what's the weather

#### Remind you of your tasks

#### Help you when you plan to move

## Useful links

## Contact
