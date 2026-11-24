# alien-review

[![make.fun · u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/nmlyz/alien-review/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/nmlyz/alien-review/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

alien-review is a tiny program that writes one alien tourist's review of planet Earth to a file: the locals live in boxes, travel in boxes, and are buried in boxes — and the reviewer rates the boxes.

The review is built in two beats — the observation, then the verdict — and the program checks the finished line before writing it: exactly 119 characters, one line, four mentions of boxes, and a SHA-256 fingerprint that must match. If any check fails, nothing is written.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The program reads the file back after writing and refuses to report success unless the bytes match the line exactly.

---

<sub>See the line on [make.fun](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)</sub>
