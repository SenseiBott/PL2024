from athlete import Athlete

def read_data(file_path):
    athletes = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        next(f) 
        for line in f:
            data = line.strip().split(",")
            athlete = Athlete(*data)
            athletes[athlete.id] = athlete
    return athletes