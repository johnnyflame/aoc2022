from dataclasses import dataclass
from aocd import get_data


@dataclass(frozen=True)
class Section:
    start: int
    end: int

    def contains(self, other: "Section"):
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: "Section"):
        return self.end >= other.start and self.start <= other.end

    @classmethod
    def from_string(cls, input: str) -> "Section":
        start, end = input.split("-")
        return cls(start=int(start), end=int(end))


def part_1(input: str):
    count = 0
    for line in input.splitlines():
        input_1, input_2 = line.split(",")
        section_1 = Section.from_string(input_1)
        section_2 = Section.from_string(input_2)

        if section_1.contains(section_2) or section_2.contains(section_1):
            count += 1

    return count


def part_2(input: str):
    count = 0
    for line in input.splitlines():
        input_1, input_2 = line.split(",")
        section_1 = Section.from_string(input_1)
        section_2 = Section.from_string(input_2)
        if section_1.overlaps(section_2):
            count += 1

    return count


if __name__ == "__main__":
    print(f"part 1 answer {part_1(get_data(day=4))}")
    print(f"part 2 answer {part_2(get_data(day=4))}")
