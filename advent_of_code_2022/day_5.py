from collections import deque
from dataclasses import dataclass
from typing import Iterator

from aocd import get_data


@dataclass(frozen=True)
class StackMove:
    quantity: int
    src: int
    dest: int


def create_stacks(input: str) -> list[deque[str]]:
    stacks: list[deque] = [deque() for _ in range(9)]

    for line in input.splitlines():
        if "[" not in line:
            continue

        line = line[1::4]
        for i, val in enumerate(line):
            if val == " ":
                continue
            stacks[i].appendleft(val)
    return stacks


def parse_moves(input: str) -> Iterator[StackMove]:
    for line in input.splitlines():
        if "move" not in line:
            continue
        instruction = [int(ch) for ch in line.split() if ch.isnumeric()]

        yield StackMove(
            quantity=instruction[0], src=instruction[1], dest=instruction[2]
        )


def perform_moves(stacks: list[deque[str]], move: StackMove):
    for _ in range(move.quantity):
        stacks[move.dest - 1].append(stacks[move.src - 1].pop())


def crane_9001(stacks: list[deque[str]], move: StackMove):
    buffer = deque()
    for _ in range(move.quantity):
        buffer.appendleft(stacks[move.src - 1].pop())
    stacks[move.dest - 1].extend(buffer)


def part_1(input: str):
    stacks = create_stacks(input)
    for move in parse_moves(input):
        perform_moves(stacks, move)

    return "".join(stack[-1] for stack in stacks if stack)


def part_2(input: str):
    stacks = create_stacks(input)
    for move in parse_moves(input):
        crane_9001(stacks, move)

    return "".join(stack[-1] for stack in stacks if stack)


if __name__ == "__main__":
    print(f"part 1 answer {part_1(get_data(day=5))}")
    print(f"part 2 answer {part_2(get_data(day=5))}")
