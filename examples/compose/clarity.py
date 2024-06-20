import libem

from libem.match.prompt import rules


def main():
    # Low clarity leads to low confidence
    libem.calibrate({"libem.match.parameter.clarity": True})
    libem.calibrate({"libem.match.parameter.confidence": True})
    libem.calibrate({"libem.match.parameter.cot": True})

    e1 = "Dyson Hot+Cool AM09 Jet Focus heater and fan, White/Silver"
    e2 = "Jet Fan Heater - W/S"

    result = libem.match(e1, e2)

    print("Entity 1:", e1)
    print("Entity 2:", e2)

    print("Explanation:", result['explanation'])
    print("Clarity:", result['clarity'])
    print("Confidence:", result['confidence'])
    print("Match:", result['answer'])


if __name__ == "__main__":
    main()
