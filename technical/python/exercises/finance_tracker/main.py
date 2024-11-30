from data_entry import CSVMANAGER
from datetime import datetime

COLUMNS = ["date", "amount", "category", "description"]
DATE_FORMAT = "%Y-%m-%d"
CATEGORIES = {
    "I": "Income", 
    "E": "Expense"
}

def get_date(prompt=""):

    if not prompt.strip():
        user_date = input("Please enter a date [yyyy-mm-ddd] or just hit enter for today's date ")
    else:
        user_date = input (prompt)
        
    try:
        if not user_date.strip():
            return datetime.today().strftime(DATE_FORMAT)
        
        user_date = datetime.strptime(user_date, DATE_FORMAT)
        return user_date.strftime(DATE_FORMAT)
    except ValueError:
        print("Invalid date format. Please try again.")
        return get_date(prompt)

def get_amount():
    user_entry = input ("Please enter amount $")
    try:
        amount = float(user_entry)
        
        if amount <= 0:
            print ("Please enter an amount greater than 0 ")
            return get_amount()
        return amount        
    except ValueError:
        print("Please enter an amount greater than 0 ")
        return get_amount()


def get_category():
    user_entry = input ("Please enter category (I)ncome or (E)xpense ")

    if user_entry.upper() in CATEGORIES:
        return CATEGORIES[user_entry.upper()]
    return get_category()

def get_description():
    user_entry = input ("Please enter description ")

    if not user_entry.strip():
        return get_description()
    return user_entry



def add_new_entry():
        #Get and validate the inputs
        date = get_date()
        amount = get_amount()
        category = get_category()
        description = get_description()

        # Initialize the CSV file
        CSVMANAGER.initialize_csv()

        # Add a test entry
        CSVMANAGER.add_entry(date, amount, category, description)

def get_transactions():
    start_date = get_date("Please enter start date [yyyy-mm-dd] or just hit enter for today's date ")
    end_date = get_date("Please enter end date [yyyy-mm-dd] or just hit enter for today's date ")

    CSVMANAGER.get_transactions(start_date, end_date)
    # CSVMANAGER.get_transactions("2024-11-20","2024-11-25")

def main():
    while True:
        print(f'''
              Please select an option
              -----------------------
              Press 1 to add an entry
              Press 2 to get transaction summary
              Press q to quit
                   ''')
        option = input("Your selection ")

        if option != "q":
            try:
                match int(option):
                    case 1:
                        add_new_entry()
                    case 2: 
                        get_transactions()
                    case _:
                        return main()
            except ValueError:
                print("Please select one of the options below...")
                return main()
        else:
            break

if __name__ == "__main__":
    main()
