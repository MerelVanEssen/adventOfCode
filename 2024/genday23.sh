#!/bin/bash

YEAR=2024

# day variable has no leading 0 and must be between 1 and 25
day=${1##+(0)}
if ((day < 1 || day > 25)); then
    echo "Invalid day input: $1. Must be between 1 and 25."
    return
fi

# project vartiable is "dayXX" where XX is the day variable
project=$(printf "day%02d" $1)

# get session cookie from file if .session exists
if [[ -f ".session" ]]; then
  AOC_SESSION=$(<".session")
fi

# validate session cookie
if [ -z "$AOC_SESSION" ]; then
    echo "AOC_SESSION isn't set. Cannot continue."
    return
fi
VALIDSESSION=$(curl -s "https://adventofcode.com/${YEAR}/day/1/input" --cookie "session=${AOC_SESSION}")
if [[ $VALIDSESSION =~ "Puzzle inputs differ by user." ]] || [[ $VALIDSESSION =~ "500 Internal Server" ]]; then
    echo "Invalid AOC_SESSION. Cannot continue. ${AOC_SESSION}"
    return
fi

# start rust project if second argument is rust
if [ "$2" = "rust" ]; then

    if [[ -d "${project}-rs" ]]; then
        cd ${project}-rs
        return
    fi

    cargo new ${project}-rs

    cd ${project}-rs

    curl -s "https://adventofcode.com/${YEAR}/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

    echo -n 'fn main() {
    let data = include_str!("../input.txt").trim();
    println!(
        "Part 1: {}",
        ""
    );

    println!(
        "Part 2: {}",
        ""
    );
}' > src/main.rs

# python directory structure
else

    mkdir ${project}

    cd ${project}

    curl -s "https://adventofcode.com/${YEAR}/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

    echo -n "import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter
import heapq
from functools import cache
import sys

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [[\".\" for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		self.map = input.split(\"\n\")

	def part1(self):
		total = 0

		return total

	def part2(self):
		total = 0

		return total

def main():
	# CHANGE INPUTFILE
	input = open(sys.argv[1], \"r\").read()

	sol = Solution(input)
	print(\"Part 1:\", sol.part1())
	print(\"Part 2:\", sol.part2())

if __name__ == \"__main__\":
	main()" > day${day}.py

    touch ex

fi