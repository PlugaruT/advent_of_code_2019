from math import floor
import fileinput


def required_fuel(mass: int) -> int:
    return floor(mass / 3) - 2


def total_fuel_needed(m: int) -> int:
    while (m := required_fuel(m)) > 0:
        yield m


def total_for_module(mass):
    return sum(total_fuel_needed(mass))


def fuel_counter(masses) -> int:
    return sum([required_fuel(mass) for mass in masses])


def recursive_fuel_counter(masses):
    return sum([total_for_module(mass) for mass in masses])


def read_file() -> None:
    with open("input") as f:
        # print(fuel_counter(int(v) for v in f.readlines()))
        print(recursive_fuel_counter(int(v) for v in f.readlines()))


if __name__ == "__main__":
    read_file()
