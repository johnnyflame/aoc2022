from enum import Enum
from typing import Tuple
from aocd import get_data


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


class Outcome(Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3


def decide_outcome(their_move: Move, our_move: Move) -> Outcome:
    if our_move == their_move:
        return Outcome.DRAW

    match their_move:
        case Move.PAPER:
            return Outcome.WIN if our_move == Move.SCISSOR else Outcome.LOSE
        case Move.ROCK:
            return Outcome.WIN if our_move == Move.PAPER else Outcome.LOSE
        case Move.SCISSOR:
            return Outcome.WIN if our_move == Move.ROCK else Outcome.LOSE


def decode_moves(them: str, us: str) -> Tuple[Move, Move]:
    elvian_encoding = {"A": Move.ROCK, "B": Move.PAPER, "C": Move.SCISSOR}
    human_encoding = {"Y": Move.PAPER, "X": Move.ROCK, "Z": Move.SCISSOR}

    return (elvian_encoding[them], human_encoding[us])


def find_winning_move(move: Move) -> Move:
    match move:
        case Move.PAPER:
            return Move.SCISSOR
        case Move.ROCK:
            return Move.PAPER
        case Move.SCISSOR:
            return Move.ROCK
        case _:
            raise ValueError("Invalid Move")


def find_losing_move(move: Move) -> Move:
    match move:
        case Move.PAPER:
            return Move.ROCK
        case Move.ROCK:
            return Move.SCISSOR
        case Move.SCISSOR:
            return Move.PAPER
        case _:
            raise ValueError("Invalid Move")


def decode_moves_part_2(them: str, us: str) -> Tuple[Move, Move]:
    elvian_encoding = {"A": Move.ROCK, "B": Move.PAPER, "C": Move.SCISSOR}
    their_move = elvian_encoding[them]

    if us == "Y":
        our_move = their_move
    else:
        match us:
            case "X":
                our_move = find_losing_move(their_move)
            case "Z":
                our_move = find_winning_move(their_move)
            case _:
                raise ValueError("invalid move")

    return (their_move, our_move)


def round_score(our_move: Move, outcome: Outcome) -> int:
    move_scoring = {Move.PAPER: 2, Move.ROCK: 1, Move.SCISSOR: 3}
    outcome_scoring = {Outcome.WIN: 6, Outcome.DRAW: 3, Outcome.LOSE: 0}

    return move_scoring[our_move] + outcome_scoring[outcome]


def part_1(input: str) -> int:
    total = 0
    for line in input.splitlines():
        if not line:
            continue
        their_move, our_move = decode_moves(*line.split())
        outcome = decide_outcome(their_move, our_move)
        total += round_score(our_move, outcome)
    return total


def part_2(input: str) -> int:
    total = 0
    for line in input.splitlines():
        if not line:
            continue
        their_move, our_move = decode_moves_part_2(*line.split())
        outcome = decide_outcome(their_move, our_move)
        total += round_score(our_move, outcome)
    return total


if __name__ == "__main__":
    print(f"part 1 answer {part_1(get_data(day=2))}")
    print(f"part 2 answer {part_2(get_data(day=2))}")
