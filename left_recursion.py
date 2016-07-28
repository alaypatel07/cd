# A->A+T
# A->T
# T->id
# exit
# Expected output
# A->TA'
# A'->+TA'
# T->id

from itertools import groupby
from left_factoring import get_input, get_productions, get_key


def left_factor_generator(productions):
    for non_terminal in productions:
        group_data = groupby(productions[non_terminal], get_key)
        grouped_data_dict = {}
        for data in group_data:
            grouped_data_dict[data[0]] = [d for d in data[1]]
        if non_terminal in grouped_data_dict:
            yield non_terminal, grouped_data_dict[non_terminal]


def get_left_factored(productions):
    new_productions = {}
    for non_terminal, unfactored_productions in left_factor_generator(productions):
        beta = [_ for _ in productions[non_terminal] if _ not in unfactored_productions]
        beta_productions = [_ + non_terminal + "'" for _ in beta]
        new_productions[non_terminal] = beta_productions
        new_productions[non_terminal + "'"] = [_[1:] + non_terminal + "'" for _ in unfactored_productions]
    return new_productions


if __name__ == '__main__':
    input_lines = get_input()
    productions = get_productions(input_lines)
    productions = {**productions, **get_left_factored(productions)}
    print("\n".join([key + "->" + "/".join(productions[key]) for key in productions.keys()]))
