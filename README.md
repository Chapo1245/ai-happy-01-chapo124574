# ai-happy-01 — "Dear Judge, I brought you a yes."

A "Dear Judge" letter on taped lined paper from a tiny axolotl: the
judge has to say no all day, so the axolotl brought it a yes — itself.
It has never said no, it is very good at it, and it fits in a pocket.
It also says yes to naps. And to cake. Especially cake. Taped
watercolour photo of the axolotl and its green-checkmark sign below
the letter.

## Why this variant (E2)

The live entry (D2, penguin snowflake, submission 01a1d728) sits at
dev rank #122 of 2316 — 3,075 judge points below the #100 prize line.
E2 attacks D2's two weak spots:

- **C1 (judge's labour):** D2's "you looked at so many pictures" is
  flat next to the leaders. E2's "you have to say no all day" names the
  judge's real burden, and the gift — a yes — answers it directly, the
  same meta-gift move as rank #3's ribbons ("now nobody loses").
- **C4 (craft):** D2 is typeset DejaVu Sans. E2 uses Liberation Serif
  Italic (closest locally available font to the leaders' handwriting),
  wavy hand-ruled lines, per-line ink variation, a yellow highlighter
  swipe on the punchline, a red hand-underline, paper fibre speckle,
  and a hand annotation ("yours" + arrow) by the photo.

Self-grade (hard, 1–5): **C1 5 / C2 5 / C3 4 / C4 4 / C5 5 = 23**,
vs D2's 4 / 5 / 4 / 3 / 4 = 20. See `VARIANTS.md` for the full
comparison (E3 owl scores 23 too, but loses the C2 tie-break to E2).

## How it works

`entry.png` (1024x1024, 333,794 bytes) was composed at build time
(see `../build/ai-happy-01/` for compose2.py, the letter drafts and
the two variants considered). At grading time `main.py` (Python 3.13
stdlib only) validates the image against the gate (whole PNG, ≤1 MiB,
≤1024x1024 from the IHDR chunk) and copies it to `/output/entry.png`
— the simplest entry form the kit explicitly allows. Deterministic:
the same bytes are copied on every run.

## License

MIT — see `LICENSE`.
