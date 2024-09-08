import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

from utils.semantic_scholor_utils import fetch_paper_info, recommend_paper
from utils.slack_utils import retrieve_url
from utils.format_utils import format_paper_info, format_recommendation

load_dotenv()
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN_PAPER")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN_PAPER")
slack_app = App(token=SLACK_BOT_TOKEN)


@slack_app.event("message")
def handle_message_events(body):
    try:
        channel = body["event"]["channel"]
        user_id = body["event"]["user"]
        text_elements = body["event"]["blocks"][0]["elements"][0]["elements"]
        user_info = slack_app.client.users_info(user=user_id)
        if user_info["user"]["is_bot"]:  # ignore bot message
            return
    except KeyError:
        return

    urls = retrieve_url(text_elements)

    for url in urls:
        print(f"URL: {url}")
        paper_info = fetch_paper_info(url)
        if paper_info is None:
            continue
        message, message_blocks = format_paper_info(paper_info, url)
        response = slack_app.client.chat_postMessage(
            blocks=message_blocks,
            text=message,
            channel=channel,
        )
        recommendation_links = recommend_paper(paper_info)
        message, message_blocks = format_recommendation(recommendation_links)
        slack_app.client.chat_postMessage(
            blocks=message_blocks,
            text=message,
            channel=channel,
            thread_ts=response["message"]["ts"],
        )


if __name__ == "__main__":
    handler = SocketModeHandler(slack_app, SLACK_APP_TOKEN)
    handler.start()
