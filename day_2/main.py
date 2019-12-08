import itertools

ADD = 1
MUL = 2
HALT = 99


def get_operation(opcode):
    if opcode == ADD:
        return lambda x, y: x + y
    elif opcode == MUL:
        return lambda x, y: x * y
    elif opcode == HALT:
        raise StopIteration()

    raise ValueError(f"Unknown operation {opcode}!")


def apply_operation(head, tape):
    position_a, position_b, position_r = tape[head + 1 : head + 4]

    # return values from those positions
    return tape[position_a], tape[position_b], position_r


def parse_tape(input):
    return list(map(int, input.split(",")))


def run_on_tape(tape):
    tape = list(tape)
    head = 0
    while True:
        try:
            operation = get_operation(tape[head])
            a, b, r = apply_operation(head, tape)
            tape[r] = operation(a, b)
            head += 4
        except StopIteration:
            return tape[0]


if __name__ == "__main__":
    tape = []
    with open("input") as f:
        tape = parse_tape(f.readline())

    # as per requirement
    noun = 12
    verb = 2
    tape[1] = noun
    tape[2] = verb
    
    # print(run_on_tape(tape))
    
    possible_nouns = list(range(100))
    possible_verbs = list(range(100))
    for combination in itertools.combinations(possible_nouns[::-1], 2):
        tape[1] = combination[0]
        tape[2] = combination[1]
        r = run_on_tape(tape)
        if r == 19690720:
            print(combination)