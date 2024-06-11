import libem


def positive():
    e1 = "mighty strike freedom gundam"
    e2 = "ZGMF/A-262PD-P"

    print("No browse:")
    libem.calibrate({
        "libem.match.parameter.tools": [],
    })
    is_match = libem.match(e1, e2)
    print(f"Entity 1: {e1}\nEntity 2: {e2}\n"
          f"Match: {is_match['answer']}")

    print("With browse:")
    libem.calibrate({
        "libem.match.parameter.tools": ["libem.browse"],
        # "libem.match.parameter.cot": True,
    })
    # libem.debug_on()
    is_match = libem.match(e1, e2)
    print(f"Entity 1: {e1}\nEntity 2: {e2}\n"
          f"Match: {is_match['answer']}")


if __name__ == '__main__':
    positive()
