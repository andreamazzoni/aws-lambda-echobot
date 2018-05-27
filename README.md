# aws-lambda-echobot
A simple template to deploy a **serverless telegram bot** on **AWS Lambda**.

### Dependencies:

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot): python wrapper for Telegram Bot API's.
- [Zappa](https://github.com/Miserlou/Zappa): framework to easy deploy and manage serverless AWS Lambda functions.
- [Flask](http://flask.pocoo.org/): python framwork

Contacts: andreamazzoni78@gmail.com

## Run your own bot
In order to run your own bot you have to provide:

- AWS Account (https://aws.amazon.com)
- A Telegram bot token (https://core.telegram.org/bots#3-how-do-i-create-a-bot)

### Step 1 - AWS credentials
Put your AWS credentials and default region on ```~/.aws/config``` file:
```bash
[default]
aws_access_key_id=<access_key_id>
aws_secret_access_key=<secret_access_key>
region=<your default region> (es: eu-central-1, us-east-1...)
```

### Step 2 - clone and setup
Clone this repo locally and setup dependencies:
```bash
git clone https://github.com/andreamazzoni/aws-lambda-echobot
cd aws-lambda-echobot
virtualenv ~/virtualenvs/aws-lambda-echobot-env
source ~/virtualenvs/aws-lambda-echobot-env/bin/activate
```
At the time I write Zappa it's not fully compatible with last pip version, so you have to downgrade to 9.0.3 and then install dependencies:
```bash
pip install pip==9.0.3
pip install -r requirements.txt
```
Provide your private bot token in ```config.py``` file.

Initialize zappa with ```zappa init``` command. You can keep all defaults. Check ```zappa_settings.json```.

Deploy your bot on AWS Lambda with this zappa command: ```zappa deploy dev```. Use endpoint that zappa give to you to properly set telegram webhook. For example fire this URL with your browser:
```
http://api.telegram.org/bot<your_bot_token>/setWebhook?url=<your_aws_api_endpoint>
```

Have fun!