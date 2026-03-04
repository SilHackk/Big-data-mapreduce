#!/usr/bin/env python3
import sys

def main():
    current_key = None
    s_sum = 0
    w_sum = 0.0
    zonos = set()
    sustojimu_kiekis = 0  # <-- nauja

    print(
        f"{'marsrutas':<12}"
        f"{'siuntu_suma':>15}"
        f"{'svorio_suma':>15}"
        f"{'zonu_skirt':>12}"
        f"{'sustojimu_zonose':>18}"
    )

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        key, val = line.split("\t", 1)
        parts = val.split()

        if len(parts) < 3:
            continue

        try:
            siuntos = int(float(parts[0]))
        except:
            siuntos = 0

        try:
            svoris = float(parts[1].replace(",", "."))
        except:
            svoris = 0.0

        zona = " ".join(parts[2:]).strip()

        if current_key is None:
            current_key = key

        # nauja grupė -> atspausdinam seną
        if key != current_key:
            print(
                f"{current_key:<12}"
                f"{s_sum:>15}"
                f"{w_sum:>15.3f}"
                f"{len(zonos):>12}"
                f"{sustojimu_kiekis:>18}"
            )
            current_key = key
            s_sum = 0
            w_sum = 0.0
            zonos = set()
            sustojimu_kiekis = 0

        # agregavimas
        s_sum += siuntos
        w_sum += svoris

        # zonų skaičiavimas
        if zona:
            zonos.add(zona)
            sustojimu_kiekis += 1   # <-- kiek kartų buvo sustota zonose (įrašų skaičius)

    # paskutinė grupė
    if current_key is not None:
        print(
            f"{current_key:<12}"
            f"{s_sum:>15}"
            f"{w_sum:>15.3f}"
            f"{len(zonos):>12}"
            f"{sustojimu_kiekis:>18}"
        )

if __name__ == "__main__":
    main()