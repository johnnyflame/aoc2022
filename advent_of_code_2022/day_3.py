from aocd import get_data


def part_1(input: str):
    total = 0
    for line in input.splitlines():
        if not line:
            continue
        boundry = int(len(line) / 2)
        first_half = line[:boundry]
        second_half = line[boundry:]
        shared_items = set(first_half).intersection(set(second_half))
        for ch in shared_items:
            total += priority(ch)

    return total


def part_2(input: str):
    total = 0
    lines = input.splitlines()
    for i in range(0, len(lines), 3):
        shared_items = (
            set(lines[i])
            .intersection(set(lines[i + 1]))
            .intersection(set(lines[i + 2]))
        )
        for ch in shared_items:
            total += priority(ch)

    return total


def priority(ch: str) -> int:
    assert len(ch) == 1 and ch.isalpha()
    LOWER_CASE_OFFSET = 96
    UPPERCASE_OFFSET = 38
    return ord(ch) - LOWER_CASE_OFFSET if ch.islower() else ord(ch) - UPPERCASE_OFFSET


if __name__ == "__main__":
    print(f"part 1 answer {part_1(get_data(day=3))}")
    print(f"part 2 answer {part_2(get_data(day=3))}")
