def analyze_data(sales):
    total = sum(sales)
    average =  total/len(sales)
    highest = max(sales)
    return total, average, highest

sales = [1000,1200,800,1500]
total, avg, best = analyze_data(sales)
print(f'''
    Total: ${total}
    Average: ${avg}
    Best Month: ${best}''')