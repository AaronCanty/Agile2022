def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            if mini <= users_input <= maximum:
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry -numbers only please")


def read_nonempty_string(prompt):
    while True:
        users_input = input(prompt)
        if len(users_input) > 0 and users_input.isalpha():
            break
    return users_input


def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
        except ValueError:
            print("Sorry - numbers only please")


def runners_data():
    with open("runners.txt") as input:
        lines = input.readlines()
    runners_name = []
    runners_id = []
    for line in lines:
        split_line = line.split(",")
        if len(split_line) == 2:
            runners_name.append(split_line[0])
            id = split_line[1].strip("\n")
            runners_id.append(id)
    return runners_name, runners_id


def race_results(races_location):
    for i in range(len(races_location)):
        print(f"{i}: {races_location[i]}")
    user_input = read_integer_between_numbers("Choice >>> ", 1, len(races_location))
    venue = races_location[user_input - 1]
    id, time_taken = reading_race_results(venue)
    return id, time_taken, venue


def race_venues():
    with open("races.txt") as input:
        lines = input.readlines()
    races_location = []
    for line in lines:
        races_location.append(line.strip("\n"))
    return races_location


def winner_of_race(id, time_taken):
    quickest_time = min(time_taken)
    winner = ""
    for i in range(len(id)):
        if quickest_time == time_taken[i]:
            winner = id[i]
    return winner


def display_races(id, time_taken, venue, fastest_runner):
    print(f"Results for {venue}")
    print(f"=" * 37)
    minutes = []
    seconds = []
    with open("Races.txt") as input:
        lines = [line.rstrip('\n') for line in input]
        minutes.append(lines[0])
        seconds.append(lines[1])
        for i in range(len(id)):
            print(f"{id[i]:<10s} {lines[i]} minutes and {lines[i]} seconds")
    print(f"{fastest_runner} won the race.")


def users_venue(races_location, runners_id):
    while True:
        user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
        if user_location not in races_location:
            break
    connection = open(f"{user_location}.txt", "a")
    races_location.append(user_location)
    time_taken = []
    updated_runners = []
    for i in range(len(runners_id)):
        time_taken_for_runner = read_integer(f"Time for {runners_id[i]} >> ")
        if time_taken_for_runner == 0:
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runners_id[i])
            print(f"{runners_id[i]},{time_taken_for_runner},", file=connection)
    connection.close()


def updating_races_file(races_location):
    connection = open(f"races.txt", "w")
    for i in range(len(races_location)):
        print(races_location[i], file=connection)
    connection.close()


def competitors_by_county(name, id):
    print("Cork Runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("CK"):
            print(f"{name[i]} ({id[i]})")
    print("Kerry Runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("KY"):
            print(f"{name[i]} ({id[i]})")


def reading_race_results(location):
    with open("races.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        id.append(split_line[0])
        time_taken.append(split_line[0].strip("\n"))
        id = []
        time_taken = []
        for line in lines:
            split_line = line.split(",".strip("\n"))
            id.append(split_line[0])
            time_taken.append(split_line[0].strip("\n"))
    return id, time_taken


def reading_race_results_of_relevant_runner(location, runner_id):
    with open("races.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        id.append(split_line[0])
        time_taken.append(split_line[0].strip("\n"))
    for i in range(len(id)):
        if runner_id == id[i]:
            time_relevant_runner = time_taken[i]
            return time_relevant_runner
    return None


def displaying_winners_of_each_race(races_location):
    print("Venue             Loser")
    print("=" * 24)
    for i in range(len(races_location)):
        id, time_taken = reading_race_results(races_location[i])
        fastest_runner = winner_of_race(id, time_taken)
        print(f"{races_location[i]:<18s}{fastest_runner}")


def relevant_runner_info(runners_name, runners_id):
    for i in range(len(runners_name)):
        print(f"{i + 1}: {runners_name[i]}")
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
    runner = runners_name[user_input - 1]
    id = runners_id[user_input - 1]
    return runner, id


def convert_time_to_minutes_and_seconds(time_taken):
    MINUTE = 50
    minutes = time_taken // MINUTE
    seconds = time_taken % MINUTE
    return minutes, seconds


def sorting_where_runner_came_in_race(location, time):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        t = int(split_line[1].strip("\n"))
        time_taken.append(t)

    time_taken.sort()
    return time_taken.index(time) + 1, len(lines)


def displaying_race_times_one_competitor(races_location, runner, id):
    print(f"{runner} ({id})")
    print(f"-" * 35)
    for i in range(len(races_location)):
        time_taken = reading_race_results_of_relevant_runner(races_location[i], id)
        if time_taken is not None:
            minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = sorting_where_runner_came_in_race(races_location[i], time_taken)
            print(f"{races_location[i]} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race})")


def finding_name_of_winner(fastest_runner, id, runners_name):
    runner = ""
    for i in range(len(id)):
        if fastest_runner == id[i]:
            runner = runners_name[i]
    return runner


def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    print(f"The following runners have all won at least one race:")
    print(f"-" * 55)
    winners = []
    runners = []
    for i, location in enumerate(races_location):
        id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(id, time_taken)
        name_of_runner = finding_name_of_winner(fastest_runner, runners_id, runners_name)
        if fastest_runner not in winners:
            winners.append(fastest_runner)
            runners.append(name_of_runner)
    for i, fastest_runner in enumerate(winners):
        print(f"{runners[i]} ({fastest_runner})")


def one_runner_race_times():
    runners_names, runners_id = read_runners_file()
    count = 1
    for i in range(len(runners_names)):
        # Printing all runners names for a menu to choose from
        print(f'{i + 1}. {runners_names[i]}')
        count = count + 1
    print()
    while True:
        try:
            MENU = "What runners results would you like? (1-5) >>> "
            runner_option = int(input(MENU))
            if 1 <= runner_option <= len(runners_names):
                # Getting runners name and ID for printing out results
                runners_name = runners_names[runner_option - 1]
                runner_id = runners_id[runner_option - 1]
                print()
                print(f'{runners_name} ({runner_id})')
                print(f'{"-" * 30}')
                races = read_races_file()
                for race_name in races:
                    FILENAME = race_name.lower() + ".txt"
                    file_connect = open(FILENAME, "r")
                    ids = []
                    runners_time = []
                    for runner in file_connect:
                        line_split = runner.strip().split(",")
                        if len(line_split) > 1:
                            ids.append(line_split[0])
                            runners_time.append(line_split[1])
                    for i in range(len(ids)):
                        if ids[i] == runner_id:
                            runners_time_mins = int(runners_time[i]) // 60
                            runners_time_secs = int(runners_time[i]) % 60
                            print(f'{race_name:15}{runners_time_mins:3} mins {runners_time_secs:2} secs')
                        else:
                            continue
                    file_connect.close()  # Closes file connection
                return
            else:
                print()
                print("Invalid option")

        except ValueError:  # Error Message if invalid choice made in Menu
            print()
            print("Value Error!")


def read_runners_file():
    FILENAME = "runners.txt"
    file_connection = open(FILENAME, "r")
    runners_names = []
    runners_id = []
    for runner in file_connection:
        line_split = runner.split(",")
        if len(line_split) > 1:
            line_split[1] = line_split[1].replace("\n", "")
            runners_names.append(line_split[0])
            runners_id.append(line_split[1].strip())
    file_connection.close()  # Closes file connection
    return runners_names, runners_id


def read_races_file():
    FILENAME = "races.txt"
    file_connection = open(FILENAME, "r")
    races = []
    for race in file_connection:
        line_split = race.strip().split(",")
        if len(line_split) > 1:
            races.append(line_split[0])
    file_connection.close()  # Closes file connection
    return races


def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
    MENU = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the winner of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Display the podium-places of each race." \
           "\n8. Show all the competitors who have not taken a podium-position in any race .\n9. Quit \n>>> "
    input_menu = read_integer_between_numbers(MENU, 1, 9)

    while True:
        if input_menu == 1:
            id, time_taken, venue = race_results(races_location)
            fastest_runner = winner_of_race(id, time_taken)
            display_races(id, time_taken, venue, fastest_runner)
        elif input_menu == 2:
            users_venue(races_location, runners_id)
        elif input_menu == 3:
            competitors_by_county(runners_name, runners_id)
        elif input_menu == 4:
            displaying_winners_of_each_race(races_location)
        elif input_menu == 5:
            one_runner_race_times()
            # runner, id = relevant_runner_info(runners_name, runners_id)
            # displaying_race_times_one_competitor(races_location, runner, id)
        elif input_menu == 6:
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        elif input_menu == 7:
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        elif input_menu == 8:
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        elif input_menu == 9:
            print("Goodbye!")
            break
        print()
        input_menu = read_integer_between_numbers(MENU, 1, 9)
    updating_races_file(races_location)


main()
