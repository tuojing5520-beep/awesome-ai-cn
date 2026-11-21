# -*- coding: utf-8 -*-
import json, time, urllib.request, urllib.parse, os

OUT = os.path.join(os.environ.get("TMPDIR", "."), "ai_repos.json")
UA = {"User-Agent": "Mozilla/5.0", "Accept": "application/vnd.github+json"}

QUERIES = [
    "stars:>8000 topic:ai",
    "stars:>8000 topic:llm",
    "stars:>8000 topic:artificial-intelligence",
    "stars:>8000 topic:generative-ai",
    "stars:>8000 topic:agents",
    "stars:>8000 topic:chatgpt",
    "stars:>8000 topic:deep-learning",
    "stars:>15000 ai in:name,description",
]

repos = {}
def fetch(q, page):
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode({
        "q": q, "sort": "stars", "order": "desc", "per_page": 100, "page": page})
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode("utf-8"))

for q in QUERIES:
    for page in (1, 2):
        try:
            d = fetch(q, page)
        except Exception as e:
            print("ERR", q, page, e); time.sleep(8); continue
        items = d.get("items", [])
        print(q, page, "got", len(items), "total", d.get("total_count"))
        for it in items:
            repos[it["full_name"]] = {
                "full_name": it["full_name"],
                "name": it["name"],
                "url": it["html_url"],
                "desc": (it.get("description") or "").strip(),
                "stars": it["stargazers_count"],
                "forks": it["forks_count"],
                "lang": it.get("language") or "",
                "topics": it.get("topics", []),
                "homepage": (it.get("homepage") or "").strip(),
                "updated": it.get("pushed_at", "")[:10],
                "created": it.get("created_at", "")[:10],
                "archived": it.get("archived", False),
            }
        if len(items) < 100:
            break
        time.sleep(7)
    time.sleep(7)

data = sorted(repos.values(), key=lambda x: -x["stars"])
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("TOTAL UNIQUE", len(data))
print("top10", [(d["full_name"], d["stars"]) for d in data[:10]])
print("OUT", OUT)
