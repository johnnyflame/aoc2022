import pytest

from advent_of_code_2022.day_6 import part_1, part_2

test_data = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]


@pytest.mark.parametrize("test_input,expected", zip(test_data, (7, 5, 6, 10, 11)))
def test_part_1(test_input, expected):
    assert part_1(test_input) == expected


@pytest.mark.parametrize("test_input,expected", zip(test_data, (19, 23, 23, 29, 26)))
def test_part_2(test_input, expected):
    assert part_2(test_input) == expected
