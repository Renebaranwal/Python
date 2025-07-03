def split_bill(total_amount, num_people):
    if num_people <= 0:
        return "Number of people must be greater than zero."
    return round(total_amount / num_people, 2)

print(split_bill(1000, 4))  
