import json
import random


def main() -> (dict, dict, dict, dict, ):
    # NOTE: Get all the parse commands
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    # using lisr list comprehension
    parse_commands = [row.copy() for row in data if 'function' in row and row['function'] == 'parse']
#    parse_commands = []
#    for row in data:
#        if 'function' in row and row['function'] == 'parse':
#            parse_commands.append(row.copy())
    print(f"parse_commands: {parse_commands}")

    # NOTE: Get all the copy commands
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
     #using lisr list comprehension
    copy_commands = [row.copy() for row in data if 'function' in row and row['function'] == 'copy']

    print(f"copy_commands: {copy_commands}")

    # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
    functional_commands = []
    counter = 0
    #convert multiples instructions into single instructions by using commas in bellow for loop
    for row in parse_commands:
        counter += 1
        new_row, new_row['_list'],new_row['_counter'] =row.copy(),'parse',counter
        functional_commands.append(new_row)
    counter = 0
    for row in copy_commands:
        counter += 1
        new_row, new_row['_list'], new_row['_counter'] = row.copy(),'copy',counter
        functional_commands.append(new_row)
    print(f"functional_commands: {functional_commands}")

    # NOTE: Get random sampling of data
    random_commands = []
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
        random_commands = random.sample(data, 2)
    print(f"random_commands: {random_commands}")

    return parse_commands, copy_commands, functional_commands, random_commands


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
