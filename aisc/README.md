# AISC community website

A responsive, dependency-free static website published beneath `/aisc/` in `neolaf2/neolaf2.github.io`. The existing NEOLAF homepage and CNAME are preserved. The repository's existing GitHub Pages deployment serves the site; no new hosting account or build workflow is required.

## Build and preview

Requires Python 3.9+ for the content builder. Browsers need JavaScript only for search/filter and mobile navigation.

```sh
python3 aisc/scripts/build.py
python3 -m http.server 8000
```

Open `http://localhost:8000/aisc/`. Run from repository root. Generated HTML is committed, so GitHub Pages needs no Python runtime. All internal URLs use `/aisc/`; change `BASE` in `scripts/build.py` to relocate the site, then rebuild. Fonts load from Google Fonts with local sans-serif fallbacks.

## Content ownership

- `content/ieee/committee.json`: manually verified official IEEE scope and officers, with retrieval date and URL.
- `content/aisc/portfolio.json`: 38 selected dated records from the September 9 liaison report. Not a complete catalog and not automatically refreshed. Each record carries source, status date, canonical URL, and editorial mapping note.
- `content/aisc/framework.json`: September position paper for discussion, not adopted committee policy.
- `content/aisc/initiatives.json`: cross-project coordination themes, not formal independent IEEE programs.
- `content/aisc/events.json`: organizer-supplied event confirmation. Building address and agenda remain pending.
- `scripts/build.py`: templates, editorial page text and HTML generation.
- `assets/`: shared responsive styles, accessible menu, URL-based portfolio search and filters.

Original supplied liaison and presentation documents are not uploaded or redistributed. The website uses their approved-by-user public narrative and selected portfolio facts. Badges distinguish formal project stage from editorial initiative status.

## Refresh IEEE information

```sh
python3 aisc/scripts/refresh_ieee.py --output /tmp/aisc-ieee-review
```

This retrieves the committee homepage and catalogs into a review-only directory with source URLs, UTC timestamps, hashes, extracted table rows and source text. It **does not publish or overwrite content**. Inspect source availability and compare with the JSON records; verify designations, exact titles, approval vs publication status, and source dates. Update the appropriate source JSON and rebuild. A 403, bot challenge or parsing failure is not an empty portfolio. Preserve previous verified records. Do not use stale liaison dates as live publication dates.

The initial build could verify the official homepage but could not retrieve the full live standards and active-PAR catalogs. Therefore all portfolio status labels remain explicitly dated September 9, 2026. The report's P2863 ongoing reference is represented by its more specific approved-draft record, avoiding duplicate conflicting entries. The 12-PAR milestone has eight named highlights, not twelve fabricated records. 2807.6 is not listed as a verified catalog record because its exact designation/status is not established in the supplied material.

## Publication

Commit the generated `/aisc/` directory to the existing Pages source branch (`main`). Preserve root files and `CNAME`. The existing domain is `www.neolaf.com`, so the public path is `/aisc/`. GitHub determines the final redirect and certificate behavior. No credentials belong in this repository.

## Verification

Check internal page/asset links, detail routes, mobile navigation, combined search/status/level filters, no-results reset, direct URL filter persistence and the calendar file. Event UTC times are 2026-11-03 00:00–04:00, corresponding to Korea 09:00–13:00 and New York November 2, 19:00–23:00 EST.
