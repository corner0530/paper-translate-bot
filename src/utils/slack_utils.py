import os
from slack_sdk.web import WebClient


def slack_auth_test(api_token):
    client = WebClient(token=api_token)
    response = client.auth_test()
    return response


def retrieve_url(text_elements):
    urls = []
    for element in text_elements:
        if element["type"] == "link":
            url = element["url"]
            urls.append(url)
    return urls


def _main():
    SLACK_API_TOKEN = os.environ["SLACK_BOT_TOKEN_PAPER"]
    slack_auth_test(SLACK_API_TOKEN)


if __name__ == "__main__":
    _main()
