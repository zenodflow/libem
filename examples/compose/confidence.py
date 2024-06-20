import libem


def main():
    e1 = "Dyson Hot+Cool AM09 Jet Focus heater and fan, White/Silver"
    e2 = "Dyson AM09 Hot + Cool Jet Focus Fan Heater - W/S"

    libem.calibrate({"libem.match.parameter.confidence": True})
    result = libem.match(e1, e2)

    print("Entity 1:", e1)
    print("Entity 2:", e2)

    print("Confidence:", result['confidence'])
    print("Match:", result['answer'])


if __name__ == "__main__":
    main()
