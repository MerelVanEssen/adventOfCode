import sys
from enum import Enum
from functools import cache
from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int


NUMPAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [" ", "0", "A"],
]

NUMPAD_POSITIONS = {char: Position(x, y) for y, row in enumerate(NUMPAD) for x, char in enumerate(row)}


DIRPAD = [
    [" ", "^", "A"],
    ["<", "v", ">"],
]

DIRPAD_POSITIONS = {char: Position(x, y) for y, row in enumerate(DIRPAD) for x, char in enumerate(row)}


class KeypadType(Enum):
    NUMPAD = 0
    DIRPAD = 1

    def key_positions(self):
        return NUMPAD_POSITIONS if self == KeypadType.NUMPAD else DIRPAD_POSITIONS


@cache
def find_shortest_sequence(code: str, proxies: int, keypad_type: KeypadType = KeypadType.NUMPAD) -> int:
    sequences = keypad_control_sequences(code, keypad_type)
    if proxies == 0:
        return min(sum(len(part) for part in sequence) for sequence in sequences)
    else:
        return min(sum(find_shortest_sequence(dircode, proxies - 1, KeypadType.DIRPAD) for dircode in sequence) for sequence in sequences)


def keypad_control_sequences(code: str, keypad_type: KeypadType, start: str = "A") -> list[list[str]]:
    if code == "":
        return [[]]
    keypad_positions = keypad_type.key_positions()
    position = keypad_positions[start]
    gap = keypad_positions[" "]
    next_position = keypad_positions[code[0]]
    options = []
    horizontal_arrow = "<" if next_position.x < position.x else ">"
    vertical_arrow = "^" if next_position.y < position.y else "v"
    horizontal_distance = abs(position.x - next_position.x)
    vertical_distance = abs(position.y - next_position.y)
    if position == next_position:
        options.append("A")
    elif position.x == next_position.x:
        options.append(vertical_arrow * vertical_distance + "A")
    elif position.y == next_position.y:
        options.append(horizontal_arrow * horizontal_distance + "A")
    else:
        if not (
            (gap.x == next_position.x and gap.y in nonempty_range(position.y, next_position.y))
            or (gap.y == position.y and gap.x in nonempty_range(next_position.x, position.x))
        ):
            options.append(horizontal_arrow * horizontal_distance + vertical_arrow * vertical_distance + "A")
        if not (
            (gap.x == position.x and gap.y in nonempty_range(next_position.y, position.y))
            or (gap.y == next_position.y and gap.x in nonempty_range(position.x, next_position.x))
        ):
            options.append(vertical_arrow * vertical_distance + horizontal_arrow * horizontal_distance + "A")

    return [
        [option, *sequence]
        for sequence in keypad_control_sequences(code[1:], keypad_type, start=code[0])
        for option in options
    ]


def nonempty_range(start, end) -> range:
    assert start != end
    if start < end:
        return range(start, end)
    else:
        return range(start, end, -1)


def main():
    codes = ["029A", "980A", "179A", "456A", "379A"]
    print(sum(int(code[:-1]) * find_shortest_sequence(code, proxies=2) for code in codes))
    print(sum(int(code[:-1]) * find_shortest_sequence(code, proxies=25) for code in codes))


if __name__ == '__main__':
    main()