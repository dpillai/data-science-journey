import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# def get_balance(winnings):

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]

        for _ in columns[line]:
            if symbol != columns[line]:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbol_count.items():
        for _ in range(count):
            all_symbols.append(symbol)
    
    columns = []

    for col in range(cols):
        column = []
        curr_symbols = all_symbols[:]

        for _ in range(rows):
            value = random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row])

def deposit():
    while True:
        amount = input("What would you like to depost? $")

        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Enter an amount greater than 0")
        else:
            print("Enter a number")
    return amount
   

def get_number_of_lines():
    while True:
        number_of_lines = input(f"Enter of number of lines between 1 - {MAX_LINES} ")
        if number_of_lines.isdigit():
            number_of_lines = int(number_of_lines)
            if 1 <= number_of_lines <= 3:
                break
            else:
                print(f"Enter number of lines between 1 - {MAX_LINES} ")
        else:
            print("Enter a number")
    return number_of_lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Enter a bet an amount between ${MIN_BET} - ${MAX_BET} for each line $")
        else:
            print("Enter a number")
    return amount


def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f" You do not enough to bet that amount, you current balance is ${balance}")
        else:
            break
    
    print(f"""
          You are betting: ${bet} on {lines} lines 
          Total bet: ${bet * lines}
          """)
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print(slots)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}")
    print (f"you won on lines: ", *winning_lines )

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        run = input("Press Enter to spin (q to quit)")
        if run == "q":
            break
        print(f"Current balance is ${balance}")

        balance += spin(balance) 
    print(f"You are left with ${balance}")

main()


# using `_`
# using enumerate in a for loop
#else option for for loop