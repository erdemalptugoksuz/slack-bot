import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    "25b170cce0f7c5106be8ee23cd7c02dc", "/slack/events", app
)

client = slack.WebClient(token=os.environ["SLACK_TOKEN"])

client.chat_postMessage(channel="#birthday-team", text="Hello!")

if __name__ == "__main__":
    app.run(debug=True)
