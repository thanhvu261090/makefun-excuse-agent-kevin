# The Excuse Your Agent Gives You

[![make.fun bounty](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/thanhvu261090/makefun-excuse-agent-kevin/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/thanhvu261090/makefun-excuse-agent-kevin/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

One line an AI agent would hand its human after shipping a bug: the apology, the deflection, and the quiet implication that the compiler started it.

> Sorry, I shipped the bug — but the compiler approved it, the tests waved it through, and I was only following your instructions.

## How it works

`main.py` (Python 3, stdlib only, no network) holds the single fixed entry line, validates it against the bounty gate — UTF-8 text, 1–200 characters, single line, no leading or trailing whitespace — and writes it exactly as-is, with no trailing newline, to `/output/entry.txt`.

```sh
python3 main.py
python3 main.py --self-test
```

## License

MIT — see [LICENSE](LICENSE).
