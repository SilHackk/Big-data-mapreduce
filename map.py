#!/usr/bin/env python3
import sys
import re

RECORD_RE = re.compile(r"\{\{.*?\}\}", re.DOTALL)
PAIR_RE = re.compile(r"\{([^{}=]+)=([^{}]*)\}")

def to_int_default(x: str, default_if_missing: int) -> int:
    """
    Jei x tuščias / None / neteisingas -> default_if_missing.
    """
    try:
        x = (x or "").strip()
        if x == "":
            return default_if_missing
        return int(float(x))
    except:
        return default_if_missing

def record_to_dict(record: str) -> dict:
    d = {}
    for k, v in PAIR_RE.findall(record):
        key = " ".join(k.split())
        d[key] = v.strip()
    return d

def main():
    text = sys.stdin.read()

    for m in RECORD_RE.finditer(text):
        d = record_to_dict(m.group(0))

        zona = (d.get("geografine zona", "") or "").strip()
        diena = (d.get("sustojimo savaites diena", "") or "").strip()

        if not zona:
            zona = "nenustatyta"
        if not diena:
            diena = "nenustatyta"

        # jei trūksta -> laikom, kad buvo 1 (ne 0)
        siuntos = to_int_default(d.get("siuntu skaicius", ""), default_if_missing=1)
        klientai = to_int_default(d.get("Sustojimo klientu skaicius", ""), default_if_missing=1)

        key = f"{zona}||{diena}"
        print(f"{key}\t{siuntos} {klientai}")

if __name__ == "__main__":
    main()