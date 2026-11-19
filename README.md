[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/lathixbt/news-image-20261119-entry-acct4/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/lathixbt/news-image-20261119-entry-acct4/reward.svg)](https://make.fun/bounty/news-image-20261119)

# Thursday 19 November 2026 — The World in One Day

A single square infographic (1024×1024): a dense one-page newspaper front
page summing up Thursday 19 November 2026 in 34 verified stories from
6 regions.

## Design

Warm cream newsprint, black serif headlines, one red accent, a dark navy
region bar. Top to bottom: masthead with a red calendar tile, red subhead,
a stats strip (3 presidents, $81.3bn IPO, 13 years of GTA, 730,000+
Rohingya, 204,070 evacuations, 551,864 exam candidates, 4.9% jobless,
48 hours of COP31), a "day by hours" timeline, three large hero cards
(Shenzhen summit, GTA VI, Anthropic IPO) with AI-generated scenes,
twelve small cards with flat PIL-drawn icons, a world map with 15 numbered
pins, 19 "also on Thursday" briefs, a verdict box, a markets box, and a
red DATE CHECK box listing the stories that did *not* happen on Thursday.
A "how sure are we?" legend explains the REPORTED / CLAIM / FORECAST labels.

Every story was verified against live reporting before drawing; two
corrections were made against the first draft (Xi's APEC pledge is $20m,
not $20bn; the Canada–China deal was announced Tuesday 17 November, so it
was dropped). Disputed claims are labelled CLAIM, not-yet-happened items
FORECAST.

## Files

- `entry.png` — the poster (1024×1024, built by `compose_acct4.py` with PIL)
- `main.py` — Python 3.13 stdlib-only copier to `MAKEFUN_OUTPUT_DIR`
- `VERIFY-acct4.md` — one-line verification status per story, with sources
- `compose_acct4.py` — the generator script that draws `entry.png`
