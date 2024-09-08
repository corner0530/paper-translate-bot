import requests
from pprint import pprint


def fetch_paper_info(
    paper_url,
    fields=(
        "paperId",
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

    print(f"Request for Semantic Scholor failed ({response.status_code}).")
    print(f"Detail: {response.text}")


def recommend_paper(paper_info, limit_num=5):
    paper_id = paper_info["paperId"]
    ENDPOINT_URL = f"https://api.semanticscholar.org/recommendations/v1/papers/forpaper/{paper_id}"
    response = requests.get(
        url=ENDPOINT_URL,
        params={"limit": limit_num},
    )
    if response.status_code == 200:  # ok
        recommend_papers = response.json()["recommendedPapers"]
        return recommend_papers

    print(f"Request for Semantic Scholor failed ({response.status_code}).")
    print(f"Detail: {response.text}")


def _main():
    paper_url = input()
    paper_info = fetch_paper_info(paper_url)
    pprint(paper_info)
    recommendation = recommend_paper(paper_info)
    pprint(recommendation)


if __name__ == "__main__":
    _main()
