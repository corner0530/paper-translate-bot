import requests
from pprint import pprint


def fetch_paper_info(
    paper_url,
    fields=(
        "title",
        "authors",
        "venue",
        "year",
        "citationCount",
        "tldr",
        "abstract",
    ),
):
    ENDPOINT_URL = "https://api.semanticscholar.org/graph/v1/paper"
    response = requests.get(
        url=f"{ENDPOINT_URL}/URL:{paper_url}",
        params={"fields": ",".join(fields)},
    )
    if response.status_code == 200:  # ok
        return response.json()

    print(
        f"Request for Semantic Scholor failed ({response.status_code}). Calling again..."
    )
    print(f"Detail: {response.text}")


def _main():
    paper_url = input()
    paper_info = fetch_paper_info(paper_url)
    pprint(paper_info)


if __name__ == "__main__":
    _main()
