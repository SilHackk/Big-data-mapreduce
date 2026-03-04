#!/usr/bin/env python3
import sys
import re

RECORD_RE = re.compile(r"\{\{.*?\}\}", re.DOTALL)
PAIR_RE = re.compile(r"\{([^{}=]+)=([^{}]*)\}")

def to_int(x: str) -> int:
    try:
        val = x.strip()
        if val == "":
            return 1
        return int(float(val))
    except:
        return 1

def to_float(x: str) -> float:
    try:
        val = x.strip()
        if val == "":
            return 0.0
        return float(val.replace(",", "."))
    except:
        return 0.0

def record_to_dict(record: str) -> dict:
    d = {}
    for k, v in PAIR_RE.findall(record):
        d[" ".join(k.split())] = v.strip()
    return d

def main():
    text = sys.stdin.read()

    for m in RECORD_RE.finditer(text):
        d = record_to_dict(m.group(0))

        marsrutas = d.get("marsrutas", "").strip()
        if not marsrutas:
            continue

        siuntos = to_int(d.get("siuntu skaicius", ""))
        svoris = to_float(d.get("svoris", ""))
        zona = d.get("geografine zona", "").strip()

        if not zona:
            zona = "nenustatyta"

        print(f"{marsrutas}\t{siuntos} {svoris} {zona}")

if __name__ == "__main__":
    main()