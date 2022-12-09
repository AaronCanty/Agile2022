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


def read_all_files(FILENAME):
    file_connection = open(FILENAME.lower(), "r")
    race_runners_id = []
    race_runners_time_mins = []
    race_runners_time_secs = []
    for runner in file_connection:
        line_split = runner.strip().split(",")
        if len(line_split) > 1:
            race_runners_id.append(line_split[0])
            race_runners_time = line_split[1]
            # Converting time to minutes and seconds for output
            race_runners_min = int(race_runners_time) // 60
            race_runners_sec = int(race_runners_time) % 60
            race_runners_time_mins.append(race_runners_min)
            race_runners_time_secs.append(race_runners_sec)
    file_connection.close()  # Closes file connection
    return race_runners_id, race_runners_time_mins, race_runners_time_secs


def show_results_race():
    races = read_races_file()
    count = 1
    for race in races:
        print(f'{count}. {race}')
        count = count + 1
    MENU = "Type what race you would like (Check Spelling) >>> "
    race_option = int(input(MENU).lower())
    if 1 <= race_option < count:
        FILENAME = races[race_option - 1] + ".txt"
        race_runners_id, race_runners_time_mins, race_runners_time_secs = read_all_files(FILENAME)
        print()
        print(f'{"-" * 30}')
        print(f'{races[race_option - 1]} Results')
        print(f'{"-" * 30}')
        fastest_time = 999999
        fastest_runner = ""
        for i in range(len(race_runners_id)):
            # Convert time back for easier calculations
            total_time = (race_runners_time_mins[i] * 60) + race_runners_time_secs[i]
            print(
                f'{race_runners_id[i]:7}{race_runners_time_mins[i]:3}{" Mins "}{race_runners_time_secs[i]:2}{" Seconds"}')
            if total_time < fastest_time:
                fastest_time = total_time
                fastest_runner = race_runners_id[i]
            else:
                continue
        print()
        print(f'{fastest_runner} won the race.')
        return
    elif race_option >= count:
        print()
        print("Invalid option")


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


def displaying_winners_of_each_race():
    races = read_races_file()
    winners_IDS, winners_names = read_all_races_winners()
    print(f'Race{" " * 14}ID')
    print(f'{"-" * 30}')
    for i in range(len(winners_names)):
        print(f'{races[i]:16}{winners_IDS[i]}')
    return


def read_all_races_winners():
    races = read_races_file()
    runners_id = []
    winners_IDS = []
    winners_names = []
    for race_name in races:
        FILENAME = race_name.lower() + ".txt"
        file_connection = open(FILENAME, "r")
        fastest_time = 999999
        winning_runner_id = ""
        for runner in file_connection:
            line_split = runner.strip().split(",")
            if len(line_split) > 1:
                runners_id.append(line_split[0].strip(","))
                runners_time = line_split[1]
                if int(runners_time) < fastest_time:
                    fastest_time = int(runners_time)
                    winning_runner_id = line_split[0].strip(",")
                else:
                    continue
        winners_IDS.append(winning_runner_id)
        all_runners_names, all_runners_id = read_runners_file()
        for i in range(len(all_runners_id)):
            if all_runners_id[i] == winning_runner_id:
                winners_names.append(all_runners_names[i])
            else:
                continue
    file_connection.close()  # Closes file connection
    return winners_IDS, winners_names


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


def finding_name_of_winner(fastest_runner, id, runners_name):
    runner = ""
    for i in range(len(id)):
        if fastest_runner == id[i]:
            runner = runners_name[i]
    return runner


def displaying_runners_who_have_won_at_least_one_race():
    winning_ids_checked = []
    winning_names_checked = []
    winners_IDS, winners_names = read_all_races_winners()
    for i in range(len(winners_names)):
        [winning_ids_checked.append(i) for i in winners_IDS if i not in winning_ids_checked]
        [winning_names_checked.append(y) for y in winners_names if y not in winning_names_checked]

    for i in range(len(winning_names_checked)):
        print(f'{winning_names_checked[i]:15} ({winning_ids_checked[i]})')
    return


def displaying_race_times_one_competitor():
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


# def get_podium_places(races_locations):
#     first_place = races_locations[0]
#     second_place = races_locations[1]
#     third_place = races_locations[2]
#     return first_place, second_place, third_place
#
#
# def display_podium_places(first_place, second_place, third_place):
#     print("First place: ", first_place)
#     print("Second place: ", second_place)
#     print("Third place: ", third_place)
#
#
# def get_non_podium_finishers(races_locations):
#     podium_finishers = set(races_locations[:3])
#     non_podium_finishers = []
#     for finisher in races_locations:
#         if finisher not in podium_finishers:
#             non_podium_finishers.append(finisher)
#             return non_podium_finishers
#
#
# def display_non_podium_finishers(non_podium_finishers):
#     print("Non-podium positions: ", non_podium_finishers)


def display_podium_places():
    races = read_races_file()
    for race in races:
        FILENAME = race.lower() + ".txt"
        ids, times = race_file(FILENAME)
        sorted_times = sorted(times)
        podium_indexs = []
        for x in range(3):
            runner_time = sorted_times[x]
            index = times.index(runner_time)
            podium_indexs.append(index)

        print(f'{race} Podium')
        print(f'{"-" * 20}')
        print(f'{ids[podium_indexs[0]]}')
        print(f'{ids[podium_indexs[1]]}')
        print(f'{ids[podium_indexs[2]]}\n')


def race_file(FILENAME):
    file_connection = open(FILENAME.lower(), "r")
    race_runners_ids = []
    race_runners_times = []
    for runner in file_connection:
        line_split = runner.strip().split(",")
        if len(line_split) > 1:
            race_runners_ids.append(line_split[0])
            race_runners_time = line_split[1]
            race_runners_times.append(race_runners_time)
    file_connection.close()  # Closes file connection
    return race_runners_ids, race_runners_times


def display_non_podium_finishers():
    races = read_races_file()
    podium_ids = []
    for race in races:
        FILENAME = race.lower() + ".txt"
        ids, times = race_file(FILENAME)
        sorted_times = sorted(times)
        for x in range(3):
            runner_time = sorted_times[x]
            index = times.index(runner_time)
            podium_ids.append(ids[index])

    names, ids = read_runners_file()
    ids = set(ids)
    non_podium_ids = ids.difference(podium_ids)
    non_podium_ids = list(non_podium_ids)

    print(f'Non Podium Finishers')
    print(f'{"-" * 20}')
    for i in range(len(non_podium_ids)):
        print(f'{non_podium_ids[i]}')


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
            show_results_race()
        elif input_menu == 2:
            users_venue(races_location, runners_id)
        elif input_menu == 3:
            competitors_by_county(runners_name, runners_id)
        elif input_menu == 4:
            displaying_winners_of_each_race()
        elif input_menu == 5:
            displaying_race_times_one_competitor()
        elif input_menu == 6:
            displaying_runners_who_have_won_at_least_one_race()
        elif input_menu == 7:
            display_podium_places()
        elif input_menu == 8:
            # non_podium_finishers = get_non_podium_finishers(races_location)
            # display_non_podium_finishers(non_podium_finishers)
            display_non_podium_finishers()
            print()
        elif input_menu == 9:
            print("Goodbye!")
            break
        print()
        input_menu = read_integer_between_numbers(MENU, 1, 9)
    updating_races_file(races_location)


main()
