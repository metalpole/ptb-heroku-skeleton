## Progress
**[@stablegeniusbot](https://web.telegram.org/#/im?p=@stablegeniusbot)**

1) Only basic bot is currently deployed on Heroku
2) Next steps:
   * Use python-telegram-bot API to create my own custom message handling functions
   * Integrate with default GPT-2 language model
   * Fine-tune language model

Using version 11.1.0

-------------------------------------------------------------------------------------------------------------------------
**Forked from forked from Eldinnie/ptb-heroku-skeleton**

## [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot/) on [Heroku](https://www.heroku.com/)

So you want to deploy a python-telegram-bot on Heroku?

In this repository you'll find a skeleton for an app on Heroku using the python-telegram-bot library.

Things to read/know:
* [Heroku getting started with Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
* [Heroku CLI](https://devcenter.heroku.com/categories/command-line) - Not required but very usefull
* Basic knowledge with git

Things you need:
* A token for your bot from [@BotFather](https://t.me/botfather)
* The name for your app. Either gathered from the web-interface or given when running

```
$ heroku create <appname>
```

Fill these in in the right place in the script you're using.

## Two versions
This Repo contains two different skeletons:
* herokubot.py - Using the builtin webhookserver
* herokubotcp.py - Using cherrypy. It even also runs a welcome webpage.

Mind that If you want to use the second example, you'll have to add `cherrypy` to the `requirements.txt`.

## Procfile
The Procfile in this repository is currently set to run the first version (with the simple http server) Change it to whatever you need.



For questions regarding python-telegram-bot please use our [telegram group](https://t.me/pythontelegrambotgroup).
