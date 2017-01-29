# Albot Pennyfred

## Introduction

Albot Pennyfred (or Alfred Pennyworth, depending of your inspiration) is a Twitter bot built on a Django API, ready to help you whenever you need information from your favorite Twitter butler.

This repository hosts the code for Albot.

## Languages and resources

This project is developed using Python 3.5 with Django 1.9.9. To build the API, the Django Rest Framework was used.

This very API calls other API to gather information and deliver it on Twitter. These API are described later on.

The bot in itself is using Twitter Streaming API to interact with users referring to the account.
The streaming API is consumed using Tweepy which makes it easy to stream incoming tweets.

### Important

You have to get your own API keys to use this program (OpenWeatherMap, Google API, Buffer API and Twitter API).

You also need to enter your Twitter credentials to use the Twitter Streaming API. Fill the keys.py file and service.py as well to have full functionalities. 
For more information on how to find such credentials, go on https://apps.twitter.com/.

## General architecture

Currently, the project is divided in two main parts:
- The Rest API part, developed with Django Rest Framework, with the following tasks:
    - Concentrate information required by the Twitter bot so that the bot only calls this API
    - Record logs of all tweets related to the Twitter bot
    - Provide an easy way to change all processes related to the acquisition of data
- The Twitter interface, developed mainly using Tweepy, with the following tasks:
    - Stream every tweet related to @albot_pennyfred
    - Analyze the content of every tweet and determine if a reply should be posted
    - Calls the API previously described and update a reply on Twitter based on it if required

This architecture was made out of flexibility to allow easy iterations on this (very) initial work.
This choice is mainly based on the fact that you have to get information on one side and deliver it in specific cases on the other.
The Twitter interface is mainly about analyzing tweets content and require a lot of work in natural language processing while the Rest API is more about building a solid base to gather information.


## Run it locally

You have to run both parts if you want to fully use Albot.
Should you have Alfred running locally on your machine, here is the way to set it up:

### Rest API part

- You should have Python 3 installed on your machine. If need be, install it using a command line
```bash
sudo apt-get install python3
```

- You also need to have Django, the Django Rest Framework, Tweepy, Datefinder and Geotext. You may install it using a command line.
You may have to use a `sudo` and/or make sure you have Python 3 files installed using `pip3` instead of `pip`
```bash
pip install django
pip install djangorestframework
pip install tweepy
pip install geotext
pip install datefinder
```

- To record tweets, you also have to set up your local database (see the point below).


- You can know run Albot Pennyfred locally using these commands.
You may have to use `python3` instead of `python` if your machine has Python 2 as default
Remember to set up your database (currently in SQLite3) if you haven't done it already:
```bash
cd albotpennyfred
python manage.py makemigrations
python manage.py migrate
```
Run the server locally:
```bash
python manage.py runserver
```

- You can know access Albot API with requests such as http://127.0.0.1:8000/weather/brussels (in your browser or a terminal)

### Twitter interface part

To start streaming Twitter and react appropriately, simply run `read.py` from the `twitter-interface` folder in a separate terminal (you may need to use `python3` there again):

```bash
cd twitter-interface
python read.py
```

Tweets streamed will be printed in their .json format in the terminal, along with errors and exceptions if some occur.

## Features

### Read your tweets

Whenever a Twitter user refers to Alfred, the tweet will be read and Alfred will react properly. He may acknowledge other users interactions.

Every tweet seen in the process is recorded in a database (currently in SQLite3) as a Log model with the following attributes:
- Tweet ID
- Username of the writer
- Full content
- Date and time

### Help you

As a butler, Alfred will try to help you in these simple matters:

#### Tell you what's the weather

- Upon receiving a tweet directed @albot_pennyfred and containing the word weather, a reply containing the location, the temperature and a description of the weather will be submitted
- To get this information, the Rest API part uses OpenWeatherMap API to provide required information.
These information are not recorded in database since they are deemed as not useful on the long-run.
The location is parsed in the tweet content using Geotext which returns the name of a city.

**Possible improvements in this part:**
- User may ask for forecast?

#### Remind you of your tasks

- Upon receiving a tweet direct @albot_pennyfred containing the word remind, a reply will acknowledge (if successful) the creation of a reminder.
- To remind a user of a task, the Rest API part uses Buffer API to post a tweet scheduled for a certain datetime.
Buffer is a platform where users can link their social media accounts and schedule posts.
This implementation allows a greater flexibility and security (for instance, if a problem occurs when running the streaming script, the scheduled tweet still exists since it has been posted on Buffer)
The reminder is also recorded in database as a way to track them in a Reminder model.
The parsing of the time and the task is done using a module called datefinder (see Useful links if necessary). It's working most of the time but still needs some work, parsing the task is currently not optimal.

Another way to implement a reminder could be to record them in the API database and regularly check for task to remind.
For instance, we would have a GET request every 15 minutes to check if there are upcoming task to remind and, if so, remind user of this.
This approach was deemed less flexible and secure than using Buffer, hence the current implementation which is easy to set up.

**Possible improvements in this part:**
- Improve parsing of message (currently using datefinder which is not optimal)

#### Help you when you plan to move

- To get this information, the Rest API part uses Google Directions to provide required information.
These information are not recorded in database since they are deemed as not useful on the long-run.
The location is parsed in the tweet content using Geotext which returns the name of a city.

**Possible improvements in this part:**
- Find a way around the inaccurate position given by Twitter (IF there is one)
- Offer options (driving, walking, cycling, public transportation)

## Possible improvements

This Twitter bot still requires some work. Here are the possible improvements currently considered:
- Improve security by designing a specific private Keys class which would contain API keys and tokens and restricting access to POST requests
- Improve parsing when reading tweets to react in a better way (manage typos, synonyms, etc.) using all natural language processing available.
    - NLTK library seems a good way to start.
    - Wit.ai also provides way to understand the sense of a phrase and would be a powerful tool if it can be used.
- Manage exceptions when services are down
- Migrate to MySQL/Postgres. There is no need for it to have the bot run smoothly currently but it may be useful in the long-run.
- Write down tests (there are only a few in `twitter-interface`) to make it easier to develop more features.
- Increase the variety of Alfred replies by completing a file with numerous lines that would be called randomly (see phrases.txt). 
For instance, Alfred could adapt his reply according to the weather (don't forget your coat/Use sunscreen/etc.).
It's very easy to add new answers but tedious to find and write nice phrases triggered by keywords. :)
- Develop more features! Only three main features are implemented but there could be a lot more such as:
    - Recommend touristic places of interest to see in a city (with Google Places API)
    - Challenge you with questions of general knowledge (there may be a database of such questions on the Internet)
    - Suggest random playlists according to your musical taste (with Spotify API)
    - etc.

## Useful links

- Django Rest Framework tutorial: http://www.django-rest-framework.org/#tutorial
- OpenWeatherMap API: https://openweathermap.org/api
- Google Directions API: https://developers.google.com/maps/documentation/directions/
- Twitter Streaming API: https://dev.twitter.com/streaming/userstreams
- Buffer API: https://buffer.com/developers/api
- Tweepy documentation: http://docs.tweepy.org/en/v3.5.0/index.html
- Tweepy example ("Introduction to text mining using Twitter"): http://adilmoujahid.com/posts/2014/07/twitter-analytics/
- Geotext page: https://pypi.python.org/pypi/geotext
- Datefinder page: https://github.com/akoumjian/datefinder

## Contact

Email address: paul.de.nonancourt (at) hotmail.fr
