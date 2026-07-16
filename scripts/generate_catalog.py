#!/usr/bin/env python3
"""Generate data/tools.json and data/tools.csv from README Markdown tables."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
DATA = ROOT / "data"
AVAILABILITY = {
    "🟢": "open-source",
    "🟠": "open-weights",
    "🔵": "open-core",
    "🔒": "commercial",
    "📖": "public-resource",
}
LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")


def clean(value):
    value = LINK_RE.sub(r"\1", value)
    value = value.replace("**", "").replace("_", "").replace("`", "")
    return " ".join(value.split())


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def artifact_type(section):
    value = section.casefold()
    if "histor" in value or "discontinued" in value: return "historical"
    if "leaderboard" in value or "arena" in value: return "leaderboard"
    if "benchmark" in value: return "benchmark"
    if "dataset" in value or "corpora" in value or "corpus" in value: return "dataset"
    if "standard" in value or "taxonom" in value or "frameworks and regulations" in value: return "standard-or-resource"
    if "platform" in value: return "platform"
    if "model" in value: return "model"
    if "framework" in value or "librar" in value: return "framework-or-library"
    return "tool"


def parse(markdown):
    rows, section = [], None
    for line in markdown.splitlines():
        heading = re.match(r"^##\s+(.+)$", line)
        if heading:
            section = clean(heading.group(1))
            continue
        if not section or section.startswith("Find Tools by") or section == "Contents":
            continue
        if not (line.startswith("|") and line.count("|") >= 3):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3 or not LINK_RE.search(cells[0]):
            continue
        match = LINK_RE.search(cells[0])
        marker = next((name for emoji, name in AVAILABILITY.items() if emoji in cells[1]), None)
        historical = "histor" in section.casefold() or "discontinued" in section.casefold()
        if marker is None and historical:
            marker = "discontinued"
        if marker is None:
            raise ValueError(f"Missing availability marker in {section}: {line}")
        description_cell = cells[-1] if historical else cells[2]
        secondary = [{"label": label, "url": url} for label, url in LINK_RE.findall(description_cell)]
        name = clean(match.group(1))
        rows.append({
            "id": f"{slug(section)}--{slug(name)}",
            "name": name,
            "artifact_type": artifact_type(section),
            "category": section,
            "availability": marker,
            "status": "discontinued" if historical else "active",
            "primary_url": match.group(2),
            "description": clean(description_cell),
            "secondary_links": secondary,
        })
    return rows


def cff_value(text, key):
    match = re.search(rf"(?m)^{re.escape(key)}:\s*[\"']?(.+?)[\"']?\s*$", text)
    return match.group(1).strip('"\'') if match else None


def main():
    markdown = README.read_text(encoding="utf-8")
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    rows = parse(markdown)
    reviewed = re.search(r"\*\*Last reviewed:\*\*\s*(\d{4}-\d{2}-\d{2})", markdown)
    categories = {}
    for row in rows:
        categories[row["category"]] = categories.get(row["category"], 0) + 1
    catalog = {
        "title": cff_value(cff, "title"),
        "source": cff_value(cff, "repository-code"),
        "license": "CC0-1.0",
        "last_verified": reviewed.group(1) if reviewed else None,
        "entry_count": len(rows),
        "category_count": len(categories),
        "categories": categories,
        "tools": rows,
    }
    DATA.mkdir(exist_ok=True)
    (DATA / "tools.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (DATA / "tools.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["id", "name", "artifact_type", "category", "availability", "status", "primary_url", "description"])
        for row in rows:
            writer.writerow([row[key] for key in ("id", "name", "artifact_type", "category", "availability", "status", "primary_url", "description")])
    print(f"Wrote {len(rows)} entries across {len(categories)} catalog sections")

if __name__ == "__main__":
    main()
