"""
Slack service

"""

import os
import time
import config
from clients import GPIOClient
from slackclient import SlackClient

# starterbot's ID as an environment variable
BOT_ID = config.get_value('bot_id')

# constants
AT_BOT = "<@" + BOT_ID + ">"
COMMAND = "switch"

# instantiate Slack 
slack_client = SlackClient(config.get_value('token'))
#automation_client = MockClient()
automation_client = GPIOClient()

def handle_command(command, channel):
    """
        Command directed at bot, decide what to do
    """
    response = "Not sure what you mean. Here is an example to help you: switch braai light on"
    if command.lower().startswith(COMMAND):
        automation_client.handle_message(command.lower())
        response = "Sure..."
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Bob connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
