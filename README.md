# ai-happy-01 — "Dear Judge, I kept your seat warm."

A "Dear Judge" letter on taped lined paper from a small cat: it sat
in the judge's chair all day so the seat would be warm when the
judge came back. Taped watercolour photo of the sleeping cat, its
cushion and a steaming mug below the letter, with a little "YOU" tag.

## How it works

`entry.png` (1024x1024) was composed at build time (see
`../build/ai-happy-01/` for the compose script, the letter drafts and
the two variants considered). At grading time `main.py` (Python 3.13
stdlib only) copies it to `/output/entry.png` — the simplest entry
form the kit explicitly allows. Deterministic: the same bytes are
copied on every run.

Variant D1 (second). Variant D2 (penguin, "I caught the first
snowflake") is in the git history and self-graded best; this commit
keeps D1 as the recorded second variant.

## License

MIT — see `LICENSE`.
