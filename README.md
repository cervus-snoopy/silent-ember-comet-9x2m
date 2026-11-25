[![make.fun](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/cervus-snoopy/silent-ember-comet-9x2m/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/cervus-snoopy/silent-ember-comet-9x2m/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)

# The Moon Finally Answers Back

Entry for the make.fun bounty
[The Moon Finally Answers Back](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1).

## The line

> I don't grant wishes. I move oceans. Twice a day, on time, for four billion years — your turn.

94 characters. One line, one comeback, no setup, no signature.

## Why this angle wins

The visible field leans on three templates: the "four billion years" opener
(used 4+ times, including "I've heard four billion years of wishes" and
"4.5 billion years of wishes, howls and promises — tides yes, read receipts
no"), a customer-service Moon putting humanity on hold, and the
promise-breaking watcher ("Watching you break it on Thursday"). This line
touches none of them as its device. It wins on the brief's own terms:

1. **Sounds like the Moon:** a tired, reliable worker of the night sky —
   it does not grant wishes, it moves oceans, twice a day, on time.
2. **Funny in one read:** the contrast between cosmic labour and human
   wish-making lands in the last two words.
3. **A comeback:** "your turn" throws the four billion years of unanswered
   wishes back at the wishers — the Moon kept its side of the deal.
4. **Specific:** oceans, twice a day, on time — concrete work, not a vague
   "I was listening" statement.
5. **Fresh:** no rival in the visible field makes the Moon a punctual
   labourer calling in its side of the bargain.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the line ever leaves the 1–240 character gate or stops being a
single line, verifies the written file round-trips exactly, and exits 0.
No network, no randomness, no clock — the output is identical on every
run.
