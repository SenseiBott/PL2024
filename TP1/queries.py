def get_sports_list(athletes):
    sports = set()
    for athlete in athletes.values():
        sports.add(athlete.sport)
    return sorted(sports)

def calculate_fitness_percentages(athletes):
    total_count = len(athletes)
    able_count = sum(1 for athlete in athletes.values() if athlete.result == "true")
    unfit_count = total_count - able_count
    able_percentage = (able_count / total_count) * 100
    unfit_percentage = (unfit_count / total_count) * 100
    return able_percentage, unfit_percentage

def calculate_age_distribution(athletes):
    age_groups = {"20-24": 0, "25-29": 0, "30-34": 0, "35-39": 0}
    for athlete in athletes.values():
        age = int(athlete.age)
        if 20 <= age <= 24:
            age_groups["20-24"] += 1
        elif 25 <= age <= 29:
            age_groups["25-29"] += 1
        elif 30 <= age <= 34:
            age_groups["30-34"] += 1
        elif 35 <= age <= 39:
            age_groups["35-39"] += 1
    return age_groups
