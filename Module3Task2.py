import random 

def get_numbers_ticket(min, max, quantity):
    if min < 1:
        return [] #if <1 -> empty list
    if max > 1000:
        return [] #if >1000 -> empty list
    
    numbers = random.sample(range(min, max + 1), quantity) #random.sample, bc want unique population

    numbers.sort() 
    
    return numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)