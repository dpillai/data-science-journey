import pandas as pd
import csv
from datetime import datetime
from matplotlib import pyplot as plt

DATE_FORMAT = "%Y-%m-%d"

class CSVMANAGER:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        with open(cls.CSV_FILE, "a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
            print("Entry added successfully.")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        total_income = 0
        total_expense = 0

        df = pd.read_csv(cls.CSV_FILE)

        start_date = datetime.strptime(start_date, DATE_FORMAT)
        end_date = datetime.strptime(end_date, DATE_FORMAT)
        df['date'] = pd.to_datetime(df['date'])    

        filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

        #Get Transaction Summary
        total_income = filtered_df[filtered_df['category'] == 'Income']['amount'].sum()    
        total_expense = filtered_df[filtered_df['category'] == 'Expense']['amount'].sum()

        print(f'''
              \n{filtered_df}

              Total Income  : ${total_income}
              Total Expense : ${total_expense}''')
        
                                 
        if input("Do you want to see a plot (y/n)").lower() == "y":
        # Ensure 'date' is the index for resampling
            filtered_df.set_index("date", inplace=True)
            
            # Resample data by day for plotting
            income_plt_df = (
                filtered_df[filtered_df['category'] == 'Income']
                .resample("D")
                .sum()
            )
            expense_plt_df = (
                filtered_df[filtered_df['category'] == 'Expense']
                .resample("D")
                .sum()
            )

            # Create the plot
            plt.figure(figsize=(10, 5))
            plt.plot(income_plt_df.index, income_plt_df["amount"], label="Income", color="green")
            plt.plot(expense_plt_df.index, expense_plt_df["amount"], label="Expense", color="red")

            # Add plot details
            plt.xlabel("Date")
            plt.ylabel("Amount")
            plt.title("Income and Expense Over Time")
            plt.legend()
            plt.grid(True)
            plt.show()