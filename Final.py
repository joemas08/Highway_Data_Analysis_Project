import csv
import matplotlib.pyplot as plt


def switch(argument):
    exit_num = {
        0: 0,
        1: 20,
        2: 45,
        3: 60,
        4: 70,
        5: 100,
        6: 130,
        7: 155,
        8: 190,
        9: 210,
    }
    return exit_num.get(argument)


def get_mph(miles, time):
    return (miles / time) * 60


all_miles = 0
speeders = 0
drivers = 0
all_speeds = 0

with open('vehicles.csv', mode='r', newline='') as input_stream:
    reader = csv.reader(input_stream)
    for line in reader:
        start_time = 0
        end_time = 0
        start_mile = 0
        end_mile = 0
        times = []
        index = -1

        for i in line:
            times.append(int(i))
        start = 0
        end = 0
        for n in times:
            index += 1
            if n != -1:
                start = index
                break
        for p in range(start, len(times)):
            if times[-1] != -1:
                end = 9
                break
            if times[p] == -1:
                end = p - 1
                break

        start_time = times[start]
        end_time = times[end]
        start_mile = switch(start)
        end_mile = switch(end)
        all_miles += end_mile - start_mile
        drivers += 1
        speed = get_mph(end_mile - start_mile, end_time - start_time)
        if speed > 70:
            speeders += 1
        all_speeds += speed

print('Total Drivers: ' + str(drivers))
print('Speeders: ' + str(speeders))
print('% of drivers speeding: ' + str(round(speeders / drivers * 100)) + ' %')
print('Non-Speeders: ' + str(drivers - speeders))
print('% of drivers not speeding: ' + str(round((drivers - speeders) / drivers * 100)) + ' %')
print('Average Speed: ' + str(round(all_speeds / drivers)) + ' mph')

total_mph_segment = [0] * 9
num_cars_segment = [0] * 9
num_cars_speeding_segment = [0] * 9
num_cars_not_speeding_segment = [0] * 9

with open('vehicles.csv', mode='r', newline='') as input_stream:
    reader = csv.reader(input_stream)
    for line in reader:
        start_time = 0
        end_time = 0
        start_mile = 0
        end_mile = 0
        times = []
        index = -1

        for i in line:
            times.append(int(i))
        start = 0
        end = 0
        # print(times)
        for n in times:
            index += 1
            # print(n)
            if n != -1:
                start = index
                break
        for p in range(start, len(times)):
            if times[-1] != -1:
                end = 9
                break
            if times[p] == -1:
                end = p - 1
                break

        for p in range(start, end):
            num_cars_segment[p] = num_cars_segment[p] + 1
            start_time = times[p]
            end_time = times[p + 1]

            start_mile = switch(p)
            end_mile = switch(p + 1)

            # all_miles += end_mile - start_mile
            # drivers += 1
            speed = get_mph(end_mile - start_mile, end_time - start_time)
            total_mph_segment[p] += round(speed)

            if speed > 70:
                num_cars_speeding_segment[p] += 1
            else:
                num_cars_not_speeding_segment[p] += 1

    # --Drivers' Speed graph--
    # x-coordinates of left sides of bars
    left = [1, 2]

    # heights of bars
    height = [speeders, (drivers - speeders)]

    # labels for bars
    tick_label = ['Speeders', 'Non-Speeders']

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label,
            width=0.8, color=['red', 'blue'])

    # naming the y-axis
    plt.ylabel('Drivers')
    # plot title
    plt.title('Drivers\' Speed')
    # function to show the plot
    plt.show()

    # --Speeder per Segment graph--
    left = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    height = [num_cars_speeding_segment[0], num_cars_speeding_segment[1], num_cars_speeding_segment[2],
              num_cars_speeding_segment[3], num_cars_speeding_segment[4],
              num_cars_speeding_segment[5], num_cars_speeding_segment[6], num_cars_speeding_segment[7],
              num_cars_speeding_segment[8]]

    tick_label = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    plt.barh(left, height, tick_label=tick_label,
             color=['red'])

    plt.xlabel('Amount of Speeders')
    plt.ylabel('Segments')
    plt.title('Speeders per Segment')
    plt.show()

    # --Non-Speeders per Segment graph--
    left = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    height = [num_cars_not_speeding_segment[0], num_cars_not_speeding_segment[1], num_cars_not_speeding_segment[2],
              num_cars_not_speeding_segment[3],
              num_cars_not_speeding_segment[4], num_cars_not_speeding_segment[5], num_cars_not_speeding_segment[6],
              num_cars_not_speeding_segment[7],
              num_cars_not_speeding_segment[8]]

    tick_label = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    plt.barh(left, height, tick_label=tick_label,
             color=['blue'])

    plt.xlabel('Cars not Speeding')
    plt.ylabel('Segments')
    plt.title('Non-Speeders per Segment')
    plt.show()

    # --Total MPH per Segment graph--
    left = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    height = [total_mph_segment[0], total_mph_segment[1], total_mph_segment[2], total_mph_segment[3],
              total_mph_segment[4], total_mph_segment[5], total_mph_segment[6], total_mph_segment[7],
              total_mph_segment[8]]

    tick_label = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    plt.bar(left, height, tick_label=tick_label,
            width=0.8, color=['purple'])

    plt.xlabel('Segments')
    plt.ylabel('Total MPH')
    plt.title('Total MPH per Segment')
    plt.show()

    # --Speeders v Non-Speeders graph--
    labels = 'Speeders', 'Non-Speeders'
    sizes = [round(speeders / drivers * 100), round(((drivers - speeders) / drivers) * 100)]
    explode = (0.1, 0)  # only "explode" the 2nd slice

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
