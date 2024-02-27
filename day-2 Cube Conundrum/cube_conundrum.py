## This attempted solution is unsucessful

file_path = "day-2 Cube Conundrum\input.txt"  # Replace with the actual path to your file
target = [12, 13, 14]
# Initializing the set to store results
results = set()

with open(file_path, 'r') as file:
    # Reading each line in the file
    for line in file:
        red = 0
        green = 0
        blue = 0
        flag = True
        # Extracting game name and results
        game_info = line.split(":")
        game_id = str(game_info[0]).split()[1]
        cubes_info = str(game_info[1]).split(";")
        for game_data in cubes_info:
            flag = True
            # Removing leading and trailing whitespaces
            game_data = game_data.strip()
            # Extracting counts for each color
            color_counts = game_data.split(",")
            for i in color_counts:
                if 'red' in i and (int(i.split()[0]) >= target[0]):
                    red += int(i.split()[0])
                elif 'blue' in i and (int(i.split()[0]) >= target[1]):
                    blue += int(i.split()[0])
                elif 'green' in i and (int(i.split()[0]) >= target[2]):
                    green += int(i.split()[0])
                else:
                    flag = False
                    break
            if not flag:
                break
        # Adding game_id to the set if it meets the conditions
        if flag:
            results.add(game_id)

print(len(results))
