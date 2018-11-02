# PyMail #

[![License](https://img.shields.io/badge/License-MIT-orange.svg)](https://github.com/Charlkie/PyMail/blob/master/LICENSE)
![](https://img.shields.io/badge/Version-Beta%200.1.0-brightgreen.svg)

**If you need only gmail api library**

Simple example of use is in file `gmailApi-example.py`

You can remove folders SPA and Server

This is most complete gmail api python library on github

------------

**Future Plans:**

* 0.1.1 Update - Authenticate the user from the flask server, as a pose to checking credentials from a saved file. Add methods to delete specific messages/threads from users mailbox. Add parameter to enable compression of data before uploading to database.

Welcome to **PyMail** the mail module used in [AtSchool's](https://github.com/at-school) single page web application

This module is a python implementation of Google's Gmail API. It takes the key parts of an Email and uploads it to a GraphQL server. Solving the problem of slow 'fetching' from the Google servers by providing a faster was to query frequently used parts of the Gmail API.

## Features ##

* Get important parts of a email from Google servers: recipient, receiver, subject and body in plain text or HTML format.
* Through GraphQL API uploads message parts to MongoDB.
* Single page web application displaying the querying of email (significantly faster than querying from Google servers)

### How To Run Server

1. run `python3 -m venv venv`
2. run `source venv/bin/activate`
3. run `pip3 intall -r requirements.txt`
3. run `export FLASK_APP="app.py"`
4. run `flask run`

### How To Run SPA

> Before running Mobile application be sure to run the server

1. run `cd SPA`
1. run `npm install`, **twice**
2. run `yarn start`

## PyMail Documentation

To test all PyMail methods run:
`$ python3 mail_test.py`

### Methods

| **Gmail.** | Parameters | Description |
| ------------- |-------------| -----|
| GetMessages().list() | msgNum | Fetches 'msgNum' message ID's from Google servers. |
| getMessageData() | messages, format, log | Gets all message data from a list of message ID's.  |
| getPayload() | msgData | Gets the payload data from message data. |
| unpackPayload() | payloads, bodies, types, log | Gets important parts from payload: recipient, sender name, sender email, subject and body of email in plain text or html format.
| sendMessage() | to, from, subject, content | sends an email from users mailbox  |

****
### Parameters
****

| Parameters | Value | Description |
| ---------- | ----- | ----------- |
| MsgNum | integer | The number of messages to be queried. |
| Messages | list | list of messages returned from `getMessages.list` method. |
| format | string | text format either `default` or `raw` |
| log | boolean | True, creates a directory wherein the return of the function is written to log files. |
| msgData | list | list of message data returned from `getMessageData` method. |
| payloads | list | list of payload parts of messages returned from `getPayload` method. |
| bodies | boolean | True to collect html or plain text bodies from payload, false. for simply headers |
| types | list of strings | types of bodies to be returned, either `html` or `plain` |


