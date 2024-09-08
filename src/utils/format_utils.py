from utils.deepl_utils import translate_text


def format_paper_info(paper_info, url):
    message = ""
    text_elements = []
    context_elements = []

    # title
    if paper_info["title"]:
        title = paper_info["title"]
        title_ja = translate_text(title)
        message += f"{title}\n({title_ja})\n"
        text_elements.append(
            {"type": "text", "text": "タイトル: ", "style": {"bold": True}}
        )
        text_elements.append({"type": "link", "url": url, "text": title_ja})

    # TL;DR
    if paper_info["tldr"] and paper_info["tldr"]["text"]:
        tldr = paper_info["tldr"]["text"]
        tldr_ja = translate_text(tldr)
        message += f"TL;DR: {tldr_ja}\n"
        text_elements.append(
            {"type": "text", "text": "\nTL;DR: ", "style": {"bold": True}}
        )
        text_elements.append({"type": "text", "text": tldr_ja})

    # abstract
    if paper_info["abstract"]:
        abstract = paper_info["abstract"]
        abstract_ja = translate_text(abstract)
        message += f"概要: {abstract_ja}"
        text_elements.append(
            {"type": "text", "text": "\n概要: ", "style": {"bold": True}}
        )
        text_elements.append({"type": "text", "text": abstract_ja})

    # authors
    if paper_info["authors"]:
        authors = [author["name"] for author in paper_info["authors"]]
        context_elements.append(
            {
                "type": "mrkdwn",
                "text": f":writing_hand: *Author*: {', '.join(authors)}",
            }
        )

    # venue
    if paper_info["venue"] and paper_info["year"]:
        year = paper_info["year"]
        venue = paper_info["venue"]
        context_elements.append(
            {
                "type": "mrkdwn",
                "text": f":pushpin: *Venue*: {venue} {year}",
            }
        )

    # citation
    if paper_info["citationCount"]:
        citation_count = paper_info["citationCount"]
        context_elements.append(
            {
                "type": "mrkdwn",
                "text": f":bookmark: *Cited by*: {citation_count} (Semantic Scholar)",
            }
        )

    message_blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": title},
        },
        {
            "type": "context",
            "elements": context_elements,
        },
        {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_section",
                    "elements": text_elements,
                }
            ],
        },
    ]
    return message, message_blocks


def format_recommendation(recommend_papers):
    message = "Recommended Papers:\n"
    bullet_elements = []
    for paper in recommend_papers:
        paper_id = paper["paperId"]
        url = f"https://www.semanticscholar.org/paper/{paper_id}"
        title = paper["title"]
        message += title + "\n"
        bullet_elements.append(
            {
                "type": "rich_text_section",
                "elements": [{"type": "link", "url": url, "text": title}],
            }
        )
    message_blocks = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": "Recommended Papers:"},
        },
        {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_list",
                    "style": "bullet",
                    "elements": bullet_elements,
                },
            ],
        },
    ]
    return message, message_blocks
