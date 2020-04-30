<a  href="https://www.twilio.com">
<img  src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg"  alt="Twilio"  width="250"  />
</a>
 
# Twilio Sample App Template

[![Actions Status](https://github.com/twilio-labs/sample-template-nodejs/workflows/Node%20CI/badge.svg)](https://github.com/twilio-labs/sample-appointment-reminders/actions)

## About

This library will give you the today's top head lines.

<!--
**TODO: UML Diagram**

We can render UML diagrams using [Mermaid](https://mermaidjs.github.io/).


**TODO: Describe how it works**
-->

## Features

1. Using Newsapi to gather news
2. Twilio Whatsapp API to display it.



## Set up

### Requirements

- Python3 (https://www.python.org/downloads/)
- A Twilio account - [sign up](https://www.twilio.com/try-twilio)
- News API Account (https://newsapi.org/)

### Twilio Account Settings

Just extract the Twilio whatsapp api key and client ID,

### Local development

After the above requirements have been met:

1. Clone this repository and `cd` into it

```bash
git clone git@github.com:ishmeet1995/Twilio-Submission
cd src
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Setup the config.ini file with

``a. Whatsapp API Key
  b. Twilio Client Key
  c. Newsapi Key
``

4. Run the application

```bash
python3 app.py
```


5. Setup Ngrok

```bash
ngrok http 5000
```

6. Paste the link in twilio's whatsapp sandbox.

That's it!

                                                                 |

## Resources

https://github.com/ishmeet1995/Twilio-Submission

