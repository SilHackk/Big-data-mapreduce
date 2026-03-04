#!/usr/bin/env python3
import sys

def flush(current_key, s_sum, k_sum):
    if current_key is None:
        return

    if "||" in current_key:
        zona, diena = current_key.split("||", 1)
    else:
        zona, diena = current_key, ""

    print(f"{zona:<25}{diena:<20}{s_sum:>15}{k_sum:>15}")

def main():
    current_key = None
    s_sum = 0
    k_sum = 0

    print(f"{'geografine zona':<25}{'savaites diena':<20}{'siuntu_suma':>15}{'klientu_suma':>15}")

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        key, val = line.split("\t", 1)
        parts = val.strip().split()
        if len(parts) < 2:
            continue

        try:
            siuntos = int(float(parts[0]))
        except:
            siuntos = 0

        try:
            klientai = int(float(parts[1]))
        except:
            klientai = 0

        if current_key is None:
            current_key = key

        if key != current_key:
            flush(current_key, s_sum, k_sum)
            current_key = key
            s_sum = 0
            k_sum = 0

        s_sum += siuntos
        k_sum += klientai

    flush(current_key, s_sum, k_sum)

if __name__ == "__main__":
    main()