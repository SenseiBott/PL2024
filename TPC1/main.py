from queries import calculate_age_distribution, calculate_fitness_percentages, get_sports_list
from datahandler import read_data
from menu import display_menu, get_user_choice

def main():
    athletes = read_data("emd.csv")
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == 1:
            sports_list = get_sports_list(athletes)
            for sport in sports_list:
                print(sport)
        elif choice == 2:
            able_percentage, unfit_percentage = calculate_fitness_percentages(athletes)
            print(f"Able: {able_percentage:.2f}%")
            print(f"Unfit: {unfit_percentage:.2f}%")
        elif choice == 3:
            age_distribution = calculate_age_distribution(athletes)
            for age_group, count in age_distribution.items():
                print(f"{age_group}: {count}")
        elif choice == 4:
            break

if __name__ == "__main__":
    main()