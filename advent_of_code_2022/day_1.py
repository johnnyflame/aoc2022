from aocd import get_data


def get_calories(input: str):
    calories = []
    accum = 0
    for line in input.splitlines():
        if line == "":
            calories.append(accum)
            accum = 0
        else:
            accum += int(line)
    calories.append(accum)
    return calories


def part_1(input: str):
    return max(get_calories(input))


def part_2(input: str):
    sorted_calories = sorted(get_calories(input))
    return sum(sorted_calories[-3:])


if __name__ == "__main__":
    print(f"part 1 answer {part_1(get_data(day=1))}")
    print(f"part 1 answer {part_2(get_data(day=1))}")
