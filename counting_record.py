def read_records(end_time, start_time):
    f = open("records.txt", "r+")
    wrong_records = f.readlines()#ВМЕСТЕ С \n
    right_records = []#БЕЗ \n
    f.write(f"{end_time - start_time}\n")
    for i in range(len(wrong_records)):
        symbol = wrong_records[i][:-1]
        symbol = float(symbol)
        right_records.append(symbol)
    min_element = 1000000000000000000000000000000000000
    for i in range(len(right_records)):
        if end_time - start_time < min_element:
            min_element = end_time - start_time    
        elif right_records[i] < min_element:
            min_element = right_records[i]
    return min_element