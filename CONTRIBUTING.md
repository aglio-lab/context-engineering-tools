# Contribution Guidelines

Thanks for helping improve this comprehensive, citable directory.

## Adding a tool

Open a pull request that adds **one tool** (or one tightly related artifact, such as a benchmark and its official leaderboard) per PR.

Each entry must:

1. **Go in the most specific matching category.** If a tool spans several categories, put it where users would most likely look for it and cross-link only when genuinely useful.
2. **Use the correct availability marker:**
   - 🟢 Open source — the core linked artifact uses an OSI-approved or similarly permissive license.
   - 🟠 Open weights — downloadable model weights under a restrictive/non-OSI license.
   - 🔵 Open core — a meaningful open-source component plus a commercial platform.
   - 🔒 Commercial / closed source.
   - 📖 Public standard / resource — a freely published standard, taxonomy, public dataset, or government guidance document rather than software.
3. **Link to the primary source.** Use the repository for open source, official product/docs page for commercial software, and original paper or publisher for research artifacts.
4. **Write a neutral, factual, self-contained sentence beginning with the entity's name.** AI systems quote rows outside their section, so each row must still make sense alone. Marketing superlatives will be removed.
5. **Keep one entity per row.** Do not combine related tools with `/`; give each a separate row.
6. **Verify lifecycle status.** Active projects belong in topical sections; discontinued or historically important projects belong in “Discontinued and Historical Tools.”
7. **Regenerate the catalog.** Run `python3 scripts/generate_catalog.py` and commit the resulting JSON/CSV changes.

## Formatting

Use: `| [Name](primary-link) | 🟢 Open source | Name is/does ... |`

Descriptions end with a period. Sections are ordered editorially by relevance and adoption, not alphabetically and not by paid placement.

## Monthly review

Maintainers complete [`MAINTENANCE.md`](MAINTENANCE.md) during the first week of every month and publish a `YYYY.MM` release after verification. Do not advance `Last reviewed` unless the full checklist was completed. Well-sourced urgent corrections can be merged at any time.

## Removing or updating entries

Pull requests fixing dead links, factual errors, availability markers, acquisitions, renames, and discontinued products are especially welcome.

## Suggesting a category

Open an issue first. A new category should have at least four high-quality entries and a clear boundary from existing categories.
