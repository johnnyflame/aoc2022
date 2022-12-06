from aocd import get_data, submit


def part_1(input: str):
    left = 0
    for right in range(3, len(input)):
        if len(set(input[left : right + 1])) == right + 1 - left:
            return right + 1
        left += 1


def part_2(input: str):
    left = 0
    for right in range(13, len(input)):
        if len(set(input[left : right + 1])) == right + 1 - left:
            return right + 1
        left += 1


if __name__ == "__main__":
    part_1_answer = part_1(get_data(day=6))
    print(f"part 1 answer {part_1_answer}")
    submit(part_1_answer)

    part_2_answer = part_2(get_data(day=6))
    print(f"part 2 answer {part_2_answer}")
    submit(part_2_answer)
