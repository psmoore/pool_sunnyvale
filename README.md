# Sunnyvale Swim Club — Pool Relay embed preview

A three-page replica of [sunn.org](https://www.sunn.org): the 2026 Fall/Winter practice
schedule and both meet schedules, each carrying a live [Pool Relay](https://www.poolrelay.com)
calendar **scoped to exactly what that page is about**.

Not an official Sunnyvale Swim Club page. It says so in a ribbon across the top.

## The thing being demonstrated

SUNN publishes its schedule in five places, and they do not agree with each other.

| # | Page | What it holds |
|---|---|---|
| 1 | Practice Schedules → 2026 Fall/Winter Practice Schedule | 19 groups, times, a four-letter pool code |
| 2 | Practice Schedules → Latest Practice Updates | 8 dates when Fremont High School hosts water polo and most of the club moves pools, at different times |
| 3 | Practice Schedules → SUNN Observed Holidays | 10 dates with no practice |
| 4 | Programs → Competitive Team | group descriptions setting attendance as "4 out of 6" — with an empty `Location:` heading on every one |
| 5 | Events → Calendar | a practices calendar that already exists, 313 entries in September alone |

**Thursday 17 September 2026 is the example.** Page 2 says nobody practices that evening —
it is the Fall Parent Meeting. Page 5 shows eleven practices. Both were published at the
same time.

That is not carelessness; it is what five places does. One calendar removes the places.

### The arithmetic that closes

The group descriptions set attendance as a fraction and never supply the denominator:

```
Junior Gold 1 & 2   5 weekdays + 1 Saturday                = 6   "4 out of 6 practices"
Senior Silver       5 weekdays + 2 mornings + 1 Saturday   = 8   "5 out of the 8 workouts"
Senior Gold         5 weekdays + 2 mornings + 1 Saturday   = 8   "7 out of 8"
Junior Silver       5 weekdays                             = 5   "3 minimum, 4–5 encouraged"
```

They reconcile exactly. **Both pages are right — they are just apart**, and the only way to
check is to open two tabs and count rows. One filtered calendar answers it by looking.

## The three pages

| Page | Calendar it carries | Scoped to |
|---|---|---|
| `index.html` — Practice schedule | [`ZSbAtgIY…`](https://www.poolrelay.com/v/ZSbAtgIYQSFVMjyzC4XKzB) | all four pools and all 19 groups, opens on the month, **Facilities** and **Practice Groups** both open |
| `agegroup-meets.html` | [`UZrsFGzc…`](https://www.poolrelay.com/v/UZrsFGzcBskHMfugHZ3q8y) | the 25 meets on the age group schedule, a year at a time, as a list |
| `senior-meets.html` | [`LcgK3yF8…`](https://www.poolrelay.com/v/LcgK3yF8v6kO6hNXy4zmH1) | the 23 meets on the senior schedule, same shape |

Nine meets are on **both** published schedules, under four different names between them
(`Gerald Mecado` / `Gerald Macedo`, `Joyce Lanfere` / `Joyce Lanphere`, `SC Far Western
Championships` / `SCY Far Westerns`, `SUNN Silicon Valley LCM Meet` / `SUNN Silicon Valley
Open`). In Pool Relay each is **one event with two audiences**, which is why both meet pages
show a `Both Schedules` section. 25 + 23 − 9 = **39 distinct meets**.

### Why the meet pages are lists of a year

An embed always opens on the current period, and a meet schedule that runs September 2026 to
August 2027 is one or two meets per month. A **year** page filter plus the **list** preset
puts a whole season on the screen and reduces "find next February" to one click on `›`.

### Why the practice page opens on a month

A week of SUNN is five groups in the Fremont High School pool between 4 and 8 pm, and the
week grid gives each of them about 35 px. The month grid prints every session as a labeled
row — time, group, in the group's own color — so a whole month of the club is legible at
once, including the water polo relocations and the blank holidays. `Week` and `Day` are one
click away.

## Conflicts — all real, none are transcription errors

- **Saturday 26 September and Saturday 24 October, Fremont High School.** The Gerald Macedo
  Classic Relay Invitational (7:30 am – 12:30 pm) and the SUNN Fall Classic both run in the
  FHS pool on a Saturday when four practices are published in the same water at the same
  time — Senior Gold 7:00–9:00, Age Group Gold 7:30–9:00, Junior Gold 1 & 2 9:00–11:00 and
  Senior Silver 9:00–11:00.
- **Two addresses for Fremont High School.** The practice schedule says *1283
  Sunnyvale/Saratoga Road*; the 26 September meet listing on the team calendar says *575 W
  Fremont Ave*.
- **SUNN Silicon Valley — 25–27 June or 26–27 June?** The two meet schedules disagree.
  Entered on the wider span.
- **DACA — Saratoga or Cupertino?** The meet schedule says Saratoga; the calendar entry names
  De Anza College in Cupertino and is headed *October 3–4, **2024***.
- **Corvallis or Portland?** "CORVALLIS OREGON SENIOR OPEN (PORTLAND, OR)" — 85 miles apart.

## Questions for the office

| | Question |
|---|---|
| **Gap** | **Lane allocations.** Five groups share the FHS pool on a weekday afternoon and three share SMS at 5:00 pm. Nothing published says who gets which lanes. That is the one thing Pool Relay draws best and cannot draw here. |
| **Gap** | **Columbia Middle School** is in the abbreviation key and in no table — it appears only on the Practice Updates page. Regular pool, or water polo overflow? |
| **Gap** | **Five senior meets have no location anywhere on the site**: TERA Senior Open, OAPB Senior Open, PLS Senior Championship P&F, CCS High School Championship, Z1S CCS Walk-On. Nine more have one only on the *other* schedule. |
| **Gap** | **Which Sunnyvale pool hosts the home meets?** Seven say only "Sunnyvale, CA". Two are long-course-meters meets, which needs 50 m. |
| **Ours** | **WCSC** is "Washington Park Pool" in the key and "Washington Community Swim Center" in the footnote. Entered once, under the second name. |
| **Ours** | **Reno, CA** on the 18–20 June travel meet. Entered as Reno, NV. |
| **Ours** | **Juneteenth — June 19, 2029** in a 2026–2027 holiday list. Outside our window either way. |
| **Ours** | **Home-meet venues.** All seven Sunnyvale meets placed at Fremont High School because that is the only SUNN pool named on any meet listing. Marked as an assumption on each entry. |

## What is in Pool Relay behind these pages

**84 event records**, entered 17 September 2026: 27 recurring practice series, 39 meets, and
18 one-off entries for the water polo relocations and the Fall Parent Meeting.

- **Four pools** — Fremont High School, Washington Community Swim Center, Sunnyvale Middle
  School, Columbia Middle School — plus an *Away Meet Venues* list holding the 21 places SUNN
  competes, from Saratoga to Huntsville, including `Venue not published` and `Venue TBD`.
- **27 recurring practice series** covering 10 August – 31 December 2026, including the split
  that moves the four Novice Silver groups and Novice Gold from FHS to Washington on Monday
  14 September, and the Tuesday/Thursday 5:45 am senior workouts that start the week of the
  14th and not before.
- **Every exception applied occurrence by occurrence** — Labor Day, Thanksgiving, the
  Christmas break, and all eight water polo dates: the moves to Columbia and Sunnyvale Middle
  School, the senior morning-only days, the Saturday the Junior Gold groups split across two
  pools, and the Tuesdays the SMS groups stand down.
- **39 meets** across both published schedules.
- **20 groups** under a *Sunnyvale Swim Club* org: Elementary, Middle School and High School
  bands holding the 19 practice groups, plus a *Meet Schedules* team holding **Age Group
  Schedule**, **Senior Schedule** and **Both Schedules**.

Sources: sunn.org — the 2026 Fall/Winter practice schedule, Latest Practice Updates, SUNN
Observed Holidays, Competitive Team, the team events calendar, and both meet schedule pages.

## Building

The chrome — ribbon, utility strip, nav, brand bar, sub-nav, footer — is identical on all
three pages and lives in `build.py` rather than being pasted three times. Edit `build.py` (or
`style.css`), then:

```
python3 build.py
python3 -m http.server 8825
```

Then open <http://localhost:8825/>. Commit the generated `.html` files; GitHub Pages serves
them as plain static files.
