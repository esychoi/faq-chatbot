import json

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://shirsh94.medium.com/top-100-python-interview-questions-and-answers-4c4e9301d9b6"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    content = soup.find_all(["h2"])

    qa = []
    for question in content:
        q = question.get_text(separator=" ", strip=True)
        if q and q[0].isdigit() and "." in q:
            q = q.split(".", 1)[1].strip()

            pretty_answer = ""
            answer_part = question.next_sibling
            while answer_part:
                if answer_part.name == "pre":
                    pretty_answer += (
                        "```\n" + answer_part.get_text(separator="\n") + "\n```\n"
                    )
                elif answer_part.name == "p":
                    pretty_answer += (
                        answer_part.get_text(separator=" ", strip=True) + "\n"
                    )
                answer_part = answer_part.next_sibling

            qa.append({"question": q, "answer": pretty_answer.strip()})

    print(f"Extracted {len(qa)} Q&A pairs.")

    with open("../data/python_faq.json", "w", encoding="utf-8") as f:
        json.dump(qa, f, ensure_ascii=False, indent=4)
