import secrets


def roll_dice():
    d20 = range(1,21)
    return secrets.choice(d20)


def stats(number_of_times):
    rolls = {}
    for i in range(0, number_of_times):
        die_roll = roll_dice()
        rolls[die_roll] = rolls.get(die_roll, 0) +1

    return rolls


def ascii_histogram(data):
    output = []
    for index in sorted(data):
        output.append('{0:5d} {1}'.format(index, '+' * (data[index]//10)))
    
    print('\n'.join(output))
    return output

if __name__ == "__main__":
    ascii_histogram(stats(100000))

