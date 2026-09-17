#!/usr/bin/env python3
"""Build the Sunnyvale Swim Club / Pool Relay preview pages.

The chrome — ribbon, utility strip, nav, brand bar, footer — is identical on all three
pages, so it lives here rather than being pasted three times. Edit this file (or
style.css), then:

    python3 build.py
    python3 -m http.server 8825
"""

import pathlib

OUT = pathlib.Path(__file__).parent

EMBED_PRACTICE = "https://www.poolrelay.com/embed/ZSbAtgIYQSFVMjyzC4XKzB"
EMBED_AGEGROUP = "https://www.poolrelay.com/embed/UZrsFGzcBskHMfugHZ3q8y"
EMBED_SENIOR = "https://www.poolrelay.com/embed/LcgK3yF8v6kO6hNXy4zmH1"

VIEW_PRACTICE = "https://www.poolrelay.com/v/ZSbAtgIYQSFVMjyzC4XKzB"
VIEW_AGEGROUP = "https://www.poolrelay.com/v/UZrsFGzcBskHMfugHZ3q8y"
VIEW_SENIOR = "https://www.poolrelay.com/v/LcgK3yF8v6kO6hNXy4zmH1"

NAV = [
    ("HOME", "index.html", False),
    ("ABOUT SUNN", "index.html", True),
    ("PROGRAMS", "index.html", True),
    ("SAFE SPORT", "index.html", True),
    ("PRACTICE SCHEDULES", "index.html", True),
    ("EVENTS", "agegroup-meets.html", True),
    ("FOR PARENTS", "index.html", True),
    ("FOR SWIMMERS", "index.html", True),
]


SUBNAV = [
    ("2026 Fall/Winter Practice Schedule", "index.html"),
    ("Age Group Meet Schedule", "agegroup-meets.html"),
    ("Senior Meet Schedule", "senior-meets.html"),
]


def chrome(title, active, page, body):
    """Wrap a page body in the shared site chrome."""
    items = []
    for label, href, caret in NAV:
        cls = ' class="on"' if label == active else ""
        tail = '<span class="caret">&#9660;</span>' if caret else ""
        items.append(
            '<li' + cls + '><a href="' + href + '">' + label + tail + "</a></li>"
        )
    nav = "\n        ".join(items)

    subs = []
    for label, href in SUBNAV:
        cls = ' class="on"' if href == page else ""
        subs.append('<li' + cls + '><a href="' + href + '">' + label + "</a></li>")
    sub = "\n        ".join(subs)

    return (
        TEMPLATE.replace("{{TITLE}}", title)
        .replace("{{NAV}}", nav)
        .replace("{{SUBNAV}}", sub)
        .replace("{{BODY}}", body)
    )


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<div class="ribbon">
  <b>Preview, not the real thing.</b> This is a mock-up of a
  <a href="https://www.sunn.org">sunn.org</a> page with a live
  <a href="https://www.poolrelay.com">Pool Relay</a> calendar on it. Not affiliated with
  Sunnyvale Swim Club.
</div>

<div class="utility">
  <span>Site Map</span>
  <span class="spacer">Sign In</span>
</div>

<div class="sheet">

  <nav class="main">
    <ul>
        {{NAV}}
    </ul>
  </nav>

  <div class="brandbar">
    <a class="mark" href="index.html">
      <span class="a">SUNN</span>
      <span class="b">SWIMMING</span>
    </a>
    <div class="badge">USA Swimming<span class="big">SAFE SPORT</span>Recognized Club</div>
    <div class="partners"><span>Speedo</span><span>USA Swimming</span><span>Level 2 Club</span></div>
  </div>

  <nav class="sub">
    <ul>
        {{SUBNAV}}
    </ul>
  </nav>

{{BODY}}

</div>

<footer>
  <div class="wrap">
    <p><b>For questions, please email <a href="mailto:office@sunn.org">office@sunn.org</a>
      or call 877-786-6794</b></p>
    <p>Sunnyvale Swim Club (a.k.a. SUNN Swimming) &middot; P.O. Box A, Sunnyvale, CA 94087</p>
    <p class="small">This preview page was built by Pool Relay from schedules published on
      sunn.org on 17 September 2026. The calendars are live &mdash; they are reading the
      same schedule the club would edit.</p>
  </div>
</footer>

</body>
</html>
"""

# ── The practice schedule page ──────────────────────────────────────────────

PRACTICE = """
  <section>
    <div class="wrap">
      <h1>SUNN Fall/Winter Practice Schedule</h1>
      <p class="sub">August 10 &ndash; December 31, 2026</p>
    </div>

    <div class="cal">
      <iframe src="__EMBED__" title="SUNN practice and meet calendar" loading="lazy"></iframe>
    </div>
    <div class="wrap">
      <p class="capt">Every practice below, on one calendar.
        Use <b>Facilities</b> to pick a pool, <b>Practice Groups</b> to pick a group, or the
        colored chips underneath to show two or three groups side by side.
        <a href="__VIEW__">Open it full size</a>.</p>
    </div>
  </section>

  <div class="trail">
    <div class="wrap">
      <p class="kicker" style="text-align:left;color:#7fc4ff">What this page is showing</p>
      <p class="q">One schedule. Five pages. They do not agree with each other.</p>
      <p>A SUNN parent who wants to know where their swimmer is this Thursday has to read
        all five, in the right order, and know which one wins:</p>
      <ol>
        <li><b>2026 Fall/Winter Practice Schedule</b> &mdash; the table below. Times and a
          four-letter pool code.</li>
        <li><b>Latest Practice Updates</b> &mdash; a different page, under the same menu.
          Eight dates in September and October when Fremont High School hosts water polo and
          most of the club moves to Columbia or Sunnyvale Middle School, at different times.</li>
        <li><b>SUNN Observed Holidays</b> &mdash; a third page. Ten dates with no practice.</li>
        <li><b>Competitive Team</b> &mdash; the group descriptions, which set attendance as
          &ldquo;4 out of 6 practices&rdquo; or &ldquo;5 out of 8 workouts&rdquo;. Every one of
          them has a <b>Location:</b> heading with nothing after it.</li>
        <li><b>Events &rarr; Calendar</b> &mdash; a practices calendar that already exists and
          holds 313 entries for September alone. It is kept by hand, alongside the table rather
          than from it, and the two have drifted: Junior Silver is in it as
          &ldquo;Junior Silver&nbsp;-&nbsp;415-545&rdquo; starting at <b>4:54&nbsp;pm</b>, and
          Junior Gold&nbsp;1 sits at <b>3:10&nbsp;pm</b> every day including Saturday.</li>
      </ol>
      <p style="margin-top:16px"><b>Today is Thursday 17 September.</b> Page 2 says there is no
        practice tonight &mdash; it is the Fall Parent Meeting. Page 5 shows eleven practices.
        Both are published, right now, on sunn.org. Neither page is careless; they are simply
        two places, and two places is one too many.</p>
      <div class="answer">
        <b>The calendar above is the only page.</b> The tables, the water polo moves, the
        holidays and the meets are all in it, so they cannot drift apart &mdash; there is
        nowhere for them to drift to. Scroll it to Thursday: one line, the 5:45&nbsp;am Senior
        workout, and a band across all four pools saying why the evening is empty.
      </div>
    </div>
  </div>

  <section>
    <div class="wrap">
      <h2>The four pools</h2>
      <div class="scroller">
      <table class="sched">
        <tr><th>Code</th><th>Pool</th><th>Address</th></tr>
        <tr><td class="n"><b>FHS</b></td><td>Fremont High School</td>
          <td>1283 Sunnyvale/Saratoga Road, Sunnyvale, CA 94087</td></tr>
        <tr><td class="n"><b>WCSC</b></td><td>Washington Park Pool
          <span style="color:#5c666d">(Washington Community Swim Center)</span></td>
          <td>255 S Pastoria Ave, Sunnyvale, CA 94086</td></tr>
        <tr><td class="n"><b>SMS</b></td><td>Sunnyvale Middle School</td>
          <td>1080 Mango Ave, Sunnyvale, CA 94087</td></tr>
        <tr><td class="n"><b>CMS</b></td><td>Columbia Middle School</td>
          <td>739 Morse Ave, Sunnyvale, CA 94085</td></tr>
      </table>
      </div>

      <h2>Elementary school groups</h2>
      <div class="scroller">
      <table class="sched">
        <tr><th>Group</th><th>Location</th><th>Days</th><th>Practice time</th><th>Coach</th></tr>
        <tr><td>Novice Silver 1</td><td class="n">FHS &rarr; WCSC</td><td>M W F</td><td>4:00 &ndash; 4:45 pm</td><td>Jen / Assistant</td></tr>
        <tr><td>Novice Silver 2</td><td class="n">FHS &rarr; WCSC</td><td>M W F</td><td>4:45 &ndash; 5:30 pm</td><td>Jen / Assistant</td></tr>
        <tr><td>Novice Silver 3</td><td class="n">FHS &rarr; WCSC</td><td>M W F</td><td>5:30 &ndash; 6:15 pm</td><td>Jen / Assistant</td></tr>
        <tr><td>Novice Silver 4</td><td class="n">FHS &rarr; WCSC</td><td>M W F</td><td>6:15 &ndash; 7:00 pm</td><td>Jen / Assistant</td></tr>
        <tr><td>Age Group Bronze 1</td><td class="n">SMS</td><td>Mon &ndash; Fri</td><td>5:00 &ndash; 6:00 pm</td><td>Kylie</td></tr>
        <tr><td>Age Group Bronze 2</td><td class="n">SMS</td><td>Mon &ndash; Fri</td><td>6:00 &ndash; 7:00 pm</td><td>Kylie</td></tr>
        <tr><td>Age Group Silver 1</td><td class="n">SMS</td><td>Mon &ndash; Fri</td><td>4:00 &ndash; 5:15 pm</td><td>Bob / Kylie</td></tr>
        <tr><td>Age Group Silver 2</td><td class="n">SMS</td><td>Mon &ndash; Fri</td><td>6:45 &ndash; 8:00 pm</td><td>Kylie / Ocean</td></tr>
        <tr><td>Age Group Gold</td><td class="n">FHS</td><td>Mon &ndash; Fri<br>Saturday</td>
          <td>5:45 &ndash; 7:15 pm<br>7:30 &ndash; 9:00 am</td><td>Bob</td></tr>
      </table>
      </div>
      <p class="capt" style="text-align:left">The four Novice Silver groups moved from Fremont
        High School to the Washington Community Swim Center on Monday 14 September. The calendar
        shows FHS before that date and Washington after it &mdash; page back a week and watch it
        change.</p>

      <h2>Middle school groups</h2>
      <div class="scroller">
      <table class="sched">
        <tr><th>Group</th><th>Location</th><th>Days</th><th>Practice time</th><th>Coach</th></tr>
        <tr><td>Novice Gold</td><td class="n">FHS &rarr; WCSC</td><td>M W F</td><td>7:00 &ndash; 7:45 pm</td><td>Jen / Assistant</td></tr>
        <tr><td>Junior Bronze 1</td><td class="n">SMS</td><td>Mon &ndash; Fri</td><td>4:00 &ndash; 5:00 pm</td><td>Ocean</td></tr>
        <tr><td>Junior Bronze 2</td><td class="n">SMS</td><td>Mon &ndash; Fri</td><td>7:00 &ndash; 8:00 pm</td><td>Ocean</td></tr>
        <tr><td>Junior Silver</td><td class="n">FHS</td><td>Mon &ndash; Fri</td><td>4:15 &ndash; 5:45 pm</td><td>Jason</td></tr>
        <tr><td>Junior Gold 1 <span style="color:#5c666d">(11&ndash;12)</span></td><td class="n">FHS</td>
          <td>Mon &ndash; Fri<br>Saturday</td><td>5:45 &ndash; 8:00 pm<br>9:00 &ndash; 11:00 am</td><td>Jason</td></tr>
        <tr><td>Junior Gold 2 <span style="color:#5c666d">(13&ndash;14)</span></td><td class="n">FHS</td>
          <td>Mon &ndash; Fri<br>Saturday</td><td>5:45 &ndash; 8:00 pm<br>9:00 &ndash; 11:00 am</td><td>Jason / Austin</td></tr>
      </table>
      </div>
      <p class="capt" style="text-align:left">Dry land is the first 25 minutes of the Junior Gold
        weekday practice.</p>

      <h2>High school groups</h2>
      <div class="scroller">
      <table class="sched">
        <tr><th>Group</th><th>Location</th><th>Days</th><th>Practice time</th><th>Coach</th></tr>
        <tr><td>Senior Bronze</td><td class="n">SMS</td><td>Mon &ndash; Fri</td><td>5:00 &ndash; 6:30 pm</td><td>Ocean</td></tr>
        <tr><td>Senior Silver</td><td class="n">FHS</td><td>Mon &ndash; Fri<br>Tue &amp; Thu<br>Saturday</td>
          <td>4:15 &ndash; 7:00 pm<br>5:45 &ndash; 7:15 am<br>9:00 &ndash; 11:00 am</td><td>Austin<br>Alex<br>Austin</td></tr>
        <tr><td>Senior Gold</td><td class="n">FHS</td><td>Mon &ndash; Fri<br>Tue &amp; Thu<br>Saturday</td>
          <td>4:00 &ndash; 7:00 pm<br>5:45 &ndash; 7:15 am<br>7:00 &ndash; 9:00 am</td><td>Alex</td></tr>
      </table>
      </div>
      <p class="capt" style="text-align:left">Dry land is the last 45 minutes of the Senior weekday
        practice. The Tuesday and Thursday morning workouts began the week of 14 September &mdash;
        the calendar starts them on Tuesday the 15th and not before.</p>

      <h2>Count the practices without leaving the page</h2>
      <p>The group descriptions on <b>Programs &rarr; Competitive Team</b> set attendance as a
        fraction: Junior Gold is &ldquo;4 out of 6 practices per week&rdquo;, Senior Silver is
        &ldquo;5 out of the 8 workouts&rdquo;, Senior Gold is &ldquo;7 out of 8&rdquo;. Nowhere on
        that page is there a 6 or an 8 to count. You have to come here, find the group, and add
        the rows up yourself:</p>
      <div class="scroller">
      <table class="sched">
        <tr><th>Group</th><th>Weekdays</th><th>Mornings</th><th>Saturday</th><th>Total</th><th>Description says</th></tr>
        <tr><td>Junior Gold 1 &amp; 2</td><td class="n">5</td><td class="n">&mdash;</td><td class="n">1</td><td class="n"><b>6</b></td><td>4 out of 6</td></tr>
        <tr><td>Senior Silver</td><td class="n">5</td><td class="n">2</td><td class="n">1</td><td class="n"><b>8</b></td><td>5 out of 8</td></tr>
        <tr><td>Senior Gold</td><td class="n">5</td><td class="n">2</td><td class="n">1</td><td class="n"><b>8</b></td><td>7 out of 8</td></tr>
        <tr><td>Junior Silver</td><td class="n">5</td><td class="n">&mdash;</td><td class="n">&mdash;</td><td class="n"><b>5</b></td><td>3 minimum, 4&ndash;5 encouraged</td></tr>
      </table>
      </div>
      <p>They reconcile exactly, which is worth saying plainly: <b>the two pages are right, they
        are just apart.</b> Filter the calendar above to Senior Gold and the eight are in front of
        you, in a week, with the pool on each one.</p>

      <h2>What the calendar adds over the table</h2>
      <ul>
        <li><b>The eight water polo dates.</b> 10, 17, 19 and 24 September and 6, 13, 20 and 22
          October are already in it &mdash; the moves to Columbia and Sunnyvale Middle School, the
          Senior morning-only days, the Saturday the Junior Gold groups split across two pools, and
          the Tuesdays the SMS groups stand down to make room. On the table they are invisible.</li>
        <li><b>The holidays.</b> Labor Day, Thanksgiving and the Christmas break are simply not
          there, because a day with no practice should look like a day with no practice.</li>
        <li><b>The meets.</b> Both home meets sit on the calendar beside the practices, so the
          26 September clash below is visible rather than discoverable.</li>
        <li><b>A group filter a parent can actually use.</b> Novice Silver 2 and nothing else,
          for the month, with the pool printed on each entry.</li>
      </ul>

      <h2>Questions for the office</h2>
      <p>These came up while entering the schedule. They are marked on the calendar entries
        themselves as well.</p>
      <ul class="qa">
        <li><span class="q"><span class="tag clash">Conflict</span>Saturday 26 September, Fremont
          High School.</span>
          <span class="a">The Gerald Macedo Classic Relay Invitational runs 7:30&nbsp;am &ndash;
          12:30&nbsp;pm in the FHS pool, and four Saturday practices are published in the same
          water at the same time: Senior Gold 7:00&ndash;9:00, Age Group Gold 7:30&ndash;9:00,
          Junior Gold 1 &amp; 2 9:00&ndash;11:00 and Senior Silver 9:00&ndash;11:00. Saturday
          24 October is the same shape, with the SUNN Fall Classic. Are those practices canceled
          on meet days, or do they happen in a corner of the pool?</span></li>
        <li><span class="q"><span class="tag clash">Conflict</span>Two addresses for Fremont High
          School.</span>
          <span class="a">The practice schedule says <b>1283 Sunnyvale/Saratoga Road</b>. The
          26 September meet listing on the team calendar says <b>575 W Fremont Ave</b>. A visiting
          family following the meet listing is sent somewhere else. Which is the pool?</span></li>
        <li><span class="q"><span class="tag gap">Gap</span>Lane allocations.</span>
          <span class="a">On a normal Monday, five groups are in the Fremont High School pool
          between 4:00 and 8:00&nbsp;pm, and three are in Sunnyvale Middle School at 5:00. The
          schedule never says how many lanes each group gets. That is the one thing Pool Relay
          would draw and cannot, because it is not published anywhere. Send the lane plan and
          these become lane charts instead of time blocks.</span></li>
        <li><span class="q"><span class="tag gap">Gap</span>Columbia Middle School.</span>
          <span class="a">CMS is in the abbreviation key at the top of the practice schedule and
          then never used in any table &mdash; it only turns up on the Practice Updates page. Is it
          a regular pool or only a water polo overflow?</span></li>
        <li><span class="q"><span class="tag ours">Ours</span>Two names for one pool.</span>
          <span class="a">The key reads &ldquo;WCSC &ndash; Washington Park Pool&rdquo; and the
          footnote reads &ldquo;Washington Community Swim Center&rdquo;. We entered one pool at
          255 S Pastoria Ave under the second name. Correct if wrong.</span></li>
        <li><span class="q"><span class="tag ours">Ours</span>Juneteenth 2029.</span>
          <span class="a">The observed holidays page lists &ldquo;Juneteenth &ndash; June 19,
          2029&rdquo; in a 2026&ndash;2027 season list. Almost certainly 2027, and outside the
          window we entered either way.</span></li>
      </ul>
    </div>
  </section>
"""

# ── The age group meet schedule page ────────────────────────────────────────

AGEGROUP = """
  <section>
    <div class="wrap">
      <h1>2026 &ndash; 2027 Age Group Meet Schedule</h1>
    </div>

    <div class="cal short">
      <iframe src="__EMBED__" title="SUNN age group meet schedule" loading="lazy"></iframe>
    </div>
    <div class="wrap">
      <p class="capt">Every meet on the age group schedule, in order, with the venue on each one.
        The arrows move between 2026 and 2027; <b>Month</b> and <b>Week</b> put the meets back
        among the practices. Meets read <b>12am&ndash;11:59pm</b> because SUNN publishes meet dates
        and not meet hours &mdash; the two whose hours are published show them.
        <a href="__VIEW__">Open it full size</a>.</p>
    </div>
  </section>

  <div class="trail">
    <div class="wrap">
      <p class="kicker" style="text-align:left;color:#7fc4ff">What this page is showing</p>
      <p class="q">Nine of these meets are also on the Senior schedule. They are the same
        meet &mdash; under four different names.</p>
      <p>The club publishes two meet schedules, and the overlap between them is not marked on
        either. The 26 September home meet is called:</p>
      <ul>
        <li><b>Gerald Mecado Relay Classic Invitational</b> &mdash; on this page</li>
        <li><b>Gerald Macedo Relay Classic Invitational</b> &mdash; on the Senior page</li>
        <li><b>GERALD MACEDO CLASSIC RELAY INVITATIONAL</b> &mdash; on the team calendar,
          where it is the only one of the three with a start time on it</li>
      </ul>
      <p style="margin-top:14px">So does <b>Joyce Lanfere</b> / <b>Joyce Lanphere</b>, and so do
        <b>SC Far Western Championships</b> / <b>SCY Far Westerns</b>, <b>DACA CBA Meet</b> /
        <b>DACA CBA+ Meet</b>, and <b>SUNN Silicon Valley LCM Meet</b> /
        <b>SUNN Silicon Valley Open</b> &mdash; which this page dates 25&ndash;27 June and the
        Senior page dates 26&ndash;27 June.</p>
      <div class="answer">
        <b>In the calendar there is one of each.</b> A meet that both squads attend is one entry
        with both audiences on it, which is why the list above groups them under
        <b>Both Schedules</b>. Rename it once and it is renamed on every page that shows it.
      </div>
    </div>
  </div>

  <section>
    <div class="wrap">
      <h2>How to read the meet types</h2>
      <ul>
        <li><b>Open</b> &mdash; open to all members of the team. Going to these meets helps swimmers
          improve technique and gain the experience to qualify for faster meets.</li>
        <li><b>Team</b> &mdash; the entire SUNN team is expected to compete.</li>
        <li><b>Qualifying</b> &mdash; only swimmers who qualify may enter. If you qualify, you are
          expected to compete.</li>
        <li><b>Travel</b> &mdash; there are two team travel meets on this year's schedule.</li>
        <li><b>Focus Meet</b> &mdash; each season's target meet.</li>
      </ul>
      <p>Meets with a <b>$</b> beside them carry a $50 or $100 travel fee per swimmer attending,
        added to your monthly statement, depending on distance. This helps the club cover coach
        costs.</p>

      <div class="scroller">
      <table class="sched">
        <caption>Fall / Winter meets</caption>
        <tr><th>Date</th><th>Meet</th><th>Location</th><th>Type</th></tr>
        <tr><td class="n">09/26</td><td>Gerald Mecado Relay Classic Invitational</td><td>Sunnyvale, CA</td><td>Team</td></tr>
        <tr><td class="n">09/27</td><td>SUNN Blue &amp; Gold Intrasquad Meet</td><td>Sunnyvale, CA</td><td>Team</td></tr>
        <tr><td class="n">10/03 &amp; 10/04</td><td>DACA CBA Meet</td><td>Saratoga, CA</td><td>Open</td></tr>
        <tr><td class="n">10/24 &amp; 10/25</td><td>SUNN Fall Classic CBA Meet</td><td>Sunnyvale, CA</td><td>Team</td></tr>
        <tr><td class="n">11/07 &amp; 11/08</td><td>Joyce Lanfere Trials &amp; Finals Invitational</td><td>Palo Alto, CA</td><td>Qualifying</td></tr>
        <tr><td class="n">11/14 &amp; 11/15</td><td>DACA CBA Meet</td><td>Saratoga, CA</td><td>Open</td></tr>
        <tr><td class="n">12/05 &amp; 12/06</td><td>ALTO CBA Meet</td><td>Palo Alto, CA</td><td>Focus / Open</td></tr>
        <tr><td class="n">12/11 &ndash; 12/13</td><td>Winter Age Group Championships</td><td>San Ramon, CA</td><td>Focus / Qualifying</td></tr>
      </table>
      </div>

      <div class="scroller">
      <table class="sched">
        <caption>Winter / Spring meets</caption>
        <tr><th>Date</th><th>Meet</th><th>Location</th><th>Type</th></tr>
        <tr><td class="n">01/16 &amp; 01/17</td><td>SSF CBA Meet</td><td>Pacifica, CA</td><td>Open</td></tr>
        <tr><td class="n">01/30 &amp; 01/31</td><td>Zone 1 North Championships</td><td>Morgan Hill, CA</td><td>Qualifying</td></tr>
        <tr><td class="n">02/12 &ndash; 02/15</td><td>Lost Dutchman Invitational</td><td>Mesa, AZ</td><td>Travel</td></tr>
        <tr><td class="n">02/20 &amp; 02/21</td><td>DACA CBA Meet</td><td>Saratoga, CA</td><td>Open</td></tr>
        <tr><td class="n">03/05 &ndash; 03/07</td><td>Spring Age Group Championships</td><td>Pleasanton, CA</td><td>Qualifying</td></tr>
        <tr><td class="n">03/14 &amp; 03/15</td><td>LAMV CBA Meet</td><td>Mountain View, CA</td><td>Open</td></tr>
        <tr><td class="n">03/18 &ndash; 03/21</td><td>SC Far Western Championships</td><td>Morgan Hill, CA</td><td>Focus / Qualifying</td></tr>
      </table>
      </div>

      <div class="scroller">
      <table class="sched">
        <caption>Spring / Summer meets</caption>
        <tr><th>Date</th><th>Meet</th><th>Location</th><th>Type</th></tr>
        <tr><td class="n">04/03</td><td>SUNN LCM Block Party</td><td>Sunnyvale, CA</td><td>Team</td></tr>
        <tr><td class="n">04/24</td><td>SUNN LCM Block Party</td><td>Sunnyvale, CA</td><td>Team</td></tr>
        <tr><td class="n">05/09</td><td>10 &amp; Under Championships</td><td>Sunnyvale, CA</td><td>Focus / Qualifying</td></tr>
        <tr><td class="n">05/22 &amp; 05/23</td><td>DACA LCM CBA Meet</td><td>Saratoga, CA</td><td>Open</td></tr>
        <tr><td class="n">06/12 &amp; 06/13</td><td>DACA LCM CBA Meet <span style="color:#5c666d">(non travel athletes)</span></td><td>Saratoga, CA</td><td>Open</td></tr>
        <tr><td class="n">06/18 &ndash; 06/20</td><td>Reno Gamble Age Group LCM Meet</td><td>Reno, CA</td><td>Travel</td></tr>
        <tr><td class="n">06/25 &ndash; 06/27</td><td>SUNN Silicon Valley LCM Meet</td><td>Sunnyvale, CA</td><td>Team</td></tr>
        <tr><td class="n">07/09 &ndash; 07/11</td><td>Senior / Age Group Championships</td><td>TBD</td><td>Qualifying</td></tr>
        <tr><td class="n">07/17 &amp; 07/18</td><td>SSF SCY CBA Meet</td><td>South San Francisco, CA</td><td>Focus / Open</td></tr>
        <tr><td class="n">07/29 &ndash; 08/01</td><td>LC Far Western Championships</td><td>Concord, CA</td><td>Focus / Qualifying</td></tr>
      </table>
      </div>

      <h2>Questions for the office</h2>
      <ul class="qa">
        <li><span class="q"><span class="tag clash">Conflict</span>SUNN Silicon Valley &mdash;
          25&ndash;27 or 26&ndash;27 June?</span>
          <span class="a">This page says 25&ndash;27 June, the Senior page says 26&ndash;27. We
          entered the wider span. It is a home meet, so the answer also decides whether Friday
          26 June practices happen.</span></li>
        <li><span class="q"><span class="tag clash">Conflict</span>The DACA meets &mdash; Saratoga
          or Cupertino?</span>
          <span class="a">This page says Saratoga. The entry on the team calendar names
          <b>De Anza College, 21250 Stevens Creek Blvd, Cupertino</b> &mdash; but that entry is
          headed &ldquo;October 3&ndash;4, <b>2024</b>&rdquo;, so it is two seasons old. Entered as
          Saratoga.</span></li>
        <li><span class="q"><span class="tag ours">Ours</span>Reno is in Nevada.</span>
          <span class="a">The 18&ndash;20 June meet is printed as &ldquo;Reno, CA&rdquo;. Entered
          as Reno, NV.</span></li>
        <li><span class="q"><span class="tag gap">Gap</span>Which Sunnyvale pool hosts the home
          meets?</span>
          <span class="a">Seven meets say only &ldquo;Sunnyvale, CA&rdquo;. Only one of them &mdash;
          26 September &mdash; names a pool anywhere on the site. We put all seven at Fremont High
          School on that basis and marked the assumption on each entry. Two of them are
          long-course-meters meets, which needs a 50&nbsp;m pool; is that FHS?</span></li>
        <li><span class="q"><span class="tag gap">Gap</span>A short course yards meet in
          July.</span>
          <span class="a">17&ndash;18 July is listed as the <b>SSF SCY</b> CBA Meet, in the middle
          of the long course summer, between two LCM meets. Deliberate?</span></li>
      </ul>
    </div>
  </section>
"""

# ── The senior meet schedule page ───────────────────────────────────────────

SENIOR = """
  <section>
    <div class="wrap">
      <h1>2026 &ndash; 2027 Senior Meet Schedule</h1>
    </div>

    <div class="cal short">
      <iframe src="__EMBED__" title="SUNN senior meet schedule" loading="lazy"></iframe>
    </div>
    <div class="wrap">
      <p class="capt">Every meet a Senior Silver or Senior Gold swimmer is expected to consider,
        with a venue on each one. <b>Both Schedules</b> marks the meets the age group squads
        attend too. Meets read <b>12am&ndash;11:59pm</b> because SUNN publishes meet dates and not
        meet hours. <a href="__VIEW__">Open it full size</a>.</p>
    </div>
  </section>

  <div class="trail">
    <div class="wrap">
      <p class="kicker" style="text-align:left;color:#7fc4ff">What this page is showing</p>
      <p class="q">Fourteen of the twenty-three meets below have no location printed on them.</p>
      <p>The senior schedule gives a city only for the meets that are a flight away &mdash;
        Portland, Austin, Sarasota, Indianapolis, Huntsville &mdash; and for the four in northern
        California that carry one in brackets. For the other fourteen, a parent working out
        whether to book a hotel has nothing to go on.</p>
      <p><b>Nine of those fourteen do have a location.</b> It is on the Age Group Meet Schedule,
        one menu item away: the Macedo relay and the Blue &amp; Gold are in Sunnyvale, DACA is in
        Saratoga, Joyce Lanphere is in Palo Alto, Zone 1 North and SCY Far Westerns are in Morgan
        Hill, LCM Far Westerns is in Concord. They are the same meets.</p>
      <p>The remaining five &mdash; <b>TERA Senior Open</b>, <b>OAPB Senior Open</b>, <b>PLS Senior
        Championship P&amp;F</b>, <b>CCS High School Championship</b> and <b>Z1S CCS Walk-On</b>
        &mdash; have no location anywhere on sunn.org.</p>
      <div class="answer">
        <b>A location is not a line of text on a meet; it is where the meet is.</b> In the calendar
        above the nine are filled in from the other schedule automatically, because it is one
        entry, and the five that are genuinely unknown say <b>Venue not published</b> rather than
        saying nothing at all. That is a to-do list, and it is five items long.
      </div>
    </div>
  </div>

  <section>
    <div class="wrap">
      <p class="season">Fall / Winter 2026</p>
      <ul class="meets">
        <li><b>Sep 26:</b> Gerald Macedo Relay Classic Invitational <span class="loc">&mdash; Sunnyvale, from the Age Group schedule</span></li>
        <li><b>Sep 27:</b> SUNN Blue &amp; Gold Intrasquad <span class="loc">&mdash; Sunnyvale, from the Age Group schedule</span></li>
        <li><b>Oct 3&ndash;4:</b> DACA CBA+ Meet <span class="loc">&mdash; Saratoga, from the Age Group schedule</span></li>
        <li><b>Oct 24&ndash;25:</b> SUNN Fall Classic CBA+ <span class="loc">&mdash; Sunnyvale, from the Age Group schedule</span></li>
        <li><b>Nov 7&ndash;8:</b> Joyce Lanphere PASA Invitational <span class="loc">&mdash; Palo Alto, from the Age Group schedule</span></li>
        <li><b>Nov 20&ndash;22:</b> TERA Senior Open <span class="loc">&mdash; venue not published</span></li>
        <li><b>Dec 4&ndash;6:</b> Corvallis Oregon Senior Open <span class="loc">&mdash; (Portland, OR)</span></li>
        <li><b>Dec 9&ndash;12:</b> Speedo Winter Juniors <span class="loc">&mdash; (Austin, TX)</span></li>
      </ul>

      <p class="season">Winter / Spring 2027</p>
      <ul class="meets">
        <li><b>Jan 23&ndash;24:</b> OAPB Senior Open <span class="loc">&mdash; venue not published</span></li>
        <li><b>Jan 30&ndash;31:</b> Zone 1 North Championship Meet <span class="loc">&mdash; Morgan Hill, from the Age Group schedule</span></li>
        <li><b>Feb 13&ndash;15:</b> PLS Senior Championship P&amp;F Meet <span class="loc">&mdash; venue not published</span></li>
        <li><b>Feb 25&ndash;28:</b> CA/NV Spring Sectionals <span class="loc">&mdash; (Roseville, CA)</span></li>
      </ul>

      <p class="season">Spring 2027</p>
      <ul class="meets">
        <li><b>Mar 18&ndash;21:</b> SCY Far Westerns <span class="loc">&mdash; Morgan Hill, from the Age Group schedule</span></li>
        <li><b>Apr 2&ndash;4:</b> Open Water Nationals / Junior Nationals <span class="loc">&mdash; (Sarasota, FL)</span></li>
        <li><b>May 7&ndash;8:</b> CCS High School Championship <span class="loc">&mdash; venue not published</span></li>
        <li><b>May 9:</b> Z1S CCS Walk-On <span class="loc">&mdash; venue not published</span></li>
      </ul>

      <p class="season">Summer 2027</p>
      <ul class="meets">
        <li><b>Jun 8&ndash;12:</b> 2027 Toyota National Championships <span class="loc">&mdash; (Indianapolis, IN)</span></li>
        <li><b>Jun 11&ndash;13:</b> Summer Sanders LCM Invitational <span class="loc">&mdash; (Roseville, CA)</span></li>
        <li><b>Jun 26&ndash;27:</b> SUNN Silicon Valley Open <span class="loc">&mdash; Sunnyvale, from the Age Group schedule</span></li>
        <li><b>Jul 15&ndash;18:</b> CA/NV Summer Sectionals <span class="loc">&mdash; (Novato, CA)</span></li>
        <li><b>Jul 28&ndash;31:</b> TYR Futures Championships <span class="loc">&mdash; (Sacramento, CA)</span></li>
        <li><b>Jul 29 &ndash; Aug 1:</b> LCM Far Westerns <span class="loc">&mdash; Concord, from the Age Group schedule</span></li>
        <li><b>Aug 2&ndash;6:</b> 2027 Speedo Junior Nationals <span class="loc">&mdash; (Huntsville, AL)</span></li>
      </ul>

      <div class="note">
        <span class="hd">Senior Gold and Senior Silver already know how many workouts a week</span>
        The group descriptions ask for 7 out of 8 and 5 out of 8. Switch the calendar above to
        <b>Week</b> and those eight are in front of you &mdash; five afternoons, two 5:45&nbsp;am
        Tuesday and Thursday workouts that began the week of 14 September, and a Saturday morning.
      </div>

      <h2>Questions for the office</h2>
      <ul class="qa">
        <li><span class="q"><span class="tag clash">Conflict</span>Corvallis or Portland?</span>
          <span class="a">The 4&ndash;6 December meet reads &ldquo;CORVALLIS OREGON SENIOR OPEN
          (PORTLAND, OR)&rdquo;. The two cities are about 85 miles apart. Entered as
          Portland.</span></li>
        <li><span class="q"><span class="tag clash">Conflict</span>SUNN Silicon Valley &mdash;
          26&ndash;27 June here, 25&ndash;27 on the Age Group schedule.</span>
          <span class="a">Entered on the wider span. It also has two names: <b>Open</b> here,
          <b>LCM Meet</b> there.</span></li>
        <li><span class="q"><span class="tag gap">Gap</span>Five meets with no location
          anywhere.</span>
          <span class="a">TERA Senior Open, OAPB Senior Open, PLS Senior Championship P&amp;F, CCS
          High School Championship and the Z1S CCS Walk-On. They appear on the calendar under
          <b>Venue not published</b> so that they are countable rather than quietly blank.</span></li>
        <li><span class="q"><span class="tag gap">Gap</span>Speedo Junior Nationals falls inside
          the August break.</span>
          <span class="a">2&ndash;6 August 2027 sits inside the club's own August Break,
          2&ndash;8 August. Presumably intended &mdash; the swimmers there are not the ones on
          break &mdash; but the two pages never meet, so nobody has had to decide.</span></li>
      </ul>
    </div>
  </section>
"""


def main():
    pages = [
        (
            "index.html",
            "Sunnyvale Swim Club - 2026 Fall/Winter Practice Schedule",
            "PRACTICE SCHEDULES",
            PRACTICE.replace("__EMBED__", EMBED_PRACTICE).replace("__VIEW__", VIEW_PRACTICE),
        ),
        (
            "agegroup-meets.html",
            "Sunnyvale Swim Club - Age Group Meet Schedule",
            "EVENTS",
            AGEGROUP.replace("__EMBED__", EMBED_AGEGROUP).replace("__VIEW__", VIEW_AGEGROUP),
        ),
        (
            "senior-meets.html",
            "Sunnyvale Swim Club - Senior Meet Schedule",
            "EVENTS",
            SENIOR.replace("__EMBED__", EMBED_SENIOR).replace("__VIEW__", VIEW_SENIOR),
        ),
    ]
    for name, title, active, body in pages:
        (OUT / name).write_text(chrome(title, active, name, body), encoding="utf-8")
        print("wrote", name)


if __name__ == "__main__":
    main()
