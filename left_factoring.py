# A->aiB/ae
# B->c
# exit
# Answer
# A->aA'/aA'
# A'->iB/e
# B->c

from itertools import groupby

from functools import reduce


def get_key(element):
    if len(element) >= 1:
        return element[0]
    else:
        return ""

def left_factor(non_terminal, production):
    grouped_data = groupby(production, get_key)
    grouped_data_dict = {}

    for data in grouped_data:
        grouped_data_dict[data[0]] = [d for d in data[1]]

    if len(grouped_data_dict.keys()) == len(production):
        return {non_terminal: production}

    new_productions = {non_terminal: []}

    count = 0
    for element in grouped_data_dict:
        if len(grouped_data_dict[element]) > 1:
            productions = [i[1:] for i in grouped_data_dict[element] if len(i) >= 1]
        else:
            productions = grouped_data_dict[element]
            new_productions[non_terminal].extend(productions)
            continue
        count += 1
        new_non_terminal = non_terminal + "'" * count
        new_productions[non_terminal].extend([element + new_non_terminal])
        new_productions.setdefault(new_non_terminal, productions)
    return new_productions


def get_left_factored(productions):
    """Group the rules for each terminal according to the common characters
        remove the uncommon parts and add it to a new non-terminal. Repeat for each non terminal.
    """
    non_terminals = list(productions.keys())
    flags = [False for _ in range(len(non_terminals))]
    while not reduce(lambda x, y: x and y, flags, True):
        for non_terminal in productions:
            new_productions = left_factor(non_terminal, productions[non_terminal])
            for new_non_terminal in new_productions:
                if new_non_terminal not in productions:
                    flags.append(False)
                    non_terminals.append(new_non_terminal)
            productions = {**productions, **new_productions}

            if new_productions[non_terminal] == productions[non_terminal]:
                flags[non_terminals.index(non_terminal)] = True

    return productions


def get_productions(lines):
    production = {}
    for line in lines:
        a, b = line.split("->")
        b = b.split("/")
        if a in production.keys():
            production[a].extend(b)
        else:
            production[a] = b
    return production


def get_input():
    input_lines = []
    i = input()
    while i != "exit":
        input_lines.append(i)
        i = input()
    return input_lines


if __name__ == '__main__':
    input_lines = get_input()
    productions = get_productions(lines=input_lines)
    try:
        left_factored_grammar = get_left_factored(productions)
        print("\n".join([key + "->" + "/".join(left_factored_grammar[key]) for key in left_factored_grammar.keys()]))
    except RuntimeError as e:
        print(e)
